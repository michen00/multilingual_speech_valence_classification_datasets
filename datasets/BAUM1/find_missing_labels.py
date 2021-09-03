# quick script to find labels missing from the annotations spreadsheets

from collections import namedtuple
from os import walk

speaker_gender = {}
preclean_info = {}
new_info = {}
with open("preclean.tsv", "r", encoding="utf-8-sig") as preclean:
    for line in preclean:
        line = line.strip().split("\t")
        try:
            file, preclean_info[file], line_gender = (
                line[0],
                (line[1], line[2]),
                line[-1],
            )
        except IndexError:
            continue
        speaker = file.split("_")[0].lower()
        gender = speaker_gender.get(speaker)
        if gender:
            if gender != line_gender:
                print("inconsistent gender:", file, line_gender, gender)
        else:
            speaker_gender[speaker] = line_gender

with open(
    "files_missing_from_annotations_spreadsheets", "r", encoding="utf-8-sig"
) as f_read:
    lines = f_read.readlines()
# I inserted a newline at the ninth line to separate acted from spontaneous files
FileSet = namedtuple("FileSet", "folder filelist")
acted = FileSet("BAUM1a_MP4_all", lines[:8])
spont = FileSet("BAUM1s_MP4 - All", lines[9:])
utterances = {}
counter = 0
for fileset in [acted, spont]:
    for file in fileset.filelist:
        file = file.strip()
        speaker = file.split("_")[0].lower()
        subtitle_path = f"{fileset.folder}/{speaker}/{file}.srt"
        try:
            with open(subtitle_path, "r") as subtitle:
                subtitle_lines = subtitle.readlines()
                while not subtitle_lines[-1].strip():
                    subtitle_lines.pop()
                utterance = subtitle_lines[-1].strip()
        except FileNotFoundError:
            print("couldn't find this subtitle:", subtitle_path)
        else:
            subtitle_folder = (
                "BAUM1a_subtitles"
                if fileset.folder == "BAUM1a_MP4_all"
                else "BAUM1s_subtitles"
            )
            for root, dirs, files in walk(fileset.folder):
                # print(root)
                comparison_file_in_preclean = False
                for comparison_file in files:
                    comparison_file, extension = comparison_file.split(".")
                    if extension != "srt" or comparison_file.split(".")[0] == file:
                        continue
                    if comparison_file not in preclean_info.keys():
                        # print(f"comparison file {comparison_file} not in preclean keys")
                        continue
                    else:
                        comparison_file_in_preclean = True
                    speaker = comparison_file.split("_")[0].lower()
                    # print(root, dirs, files, comparison_file)
                    with open(
                        f"{fileset.folder}/{speaker}/{comparison_file}.srt",
                        "r",
                        encoding="utf-8-sig",
                    ) as subtitle:
                        compare_subtitles = subtitle.readlines()
                        while not compare_subtitles[-1].strip():
                            compare_subtitles.pop()
                        if utterance == compare_subtitles[-1]:
                            new_info[file] = preclean_info[
                                comparison_file.split(".", 1)[0]
                            ]
                            break
                else:
                    if not comparison_file_in_preclean:
                        print(
                            "couldn't find a file in preclean with matching subs for",
                            file,
                        )
                    continue
                break
            else:
                print("Couldn't find a matching subtitle for", file)
for k, v in new_info.items():
    print(k, v, speaker_gender[k.split("_")[0].lower()])
