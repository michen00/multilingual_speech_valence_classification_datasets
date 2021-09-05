"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Carnegie Mellon University Let's Go Spoken Dialogue Corpus.
"""

from os import walk

LANG = "eng"  # ISO 639-3 English
LANG2 = "en-us"  # ISO 639-1 English + ISO 3166-1 United States
DATASET = "LEGOv2"

speaker_gender = {}
with open("corpus/csv/calls.csv", "r") as f:
    for line in f:
        split_line = line.split(";")
        speaker_gender[split_line[1].rsplit("/", 1)[0][1:]] = split_line[-2][1]

with open("LEGOv2_data_files.tsv", "w") as f_write:
    with open("corpus/csv/interactions.csv", "r") as f_read:
        for line in f_read:
            if "Angry" in line:
                file_ = line.split(";")[-6].strip('"')
                folder = file_.rsplit("/", 1)[0]
                try:
                    gender = speaker_gender[folder]
                except KeyError:
                    print("gender unavailable for", folder)
                    gender = "u"
                f_write.write(
                    "\t".join(
                        [
                            f"{folder}/{file_}",
                            "ang",
                            "-1",
                            LANG,
                            LANG2,
                            f"{DATASET}+{folder}",
                            gender,
                            f"{DATASET}\n",
                        ]
                    )
                )
print("done")
