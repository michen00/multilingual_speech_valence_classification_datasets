"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Ryerson Audio-Visual Database of Emotional Speech and Song.
"""

from os import walk

LANG = "eng"  # ISO 639-3 English
LANG2 = "en-ca"  # ISO 639-1 French + ISO 3166-1 Canada
DATASET = "ravdess"

emotions = ("neu", "cal", "hap", "sad", "ang", "fea", "dis", "sur")
emotion_decoder = dict(zip([f"{i:02}" for i in range(1, 9)], emotions))
valence = dict.fromkeys(emotions, "-1")
valence["hap"] = "1"
valence["cal"] = valence["neu"] = "0"

bad_files = set()
with open("ravdess_data_files.tsv", "w") as f:
    for mode in {"Song", "Speech"}:
        for i in range(1, 25):
            for root, directory, files in walk(
                f"Audio_{mode}_Actors_01-24/Actor_{i:02}"
            ):
                for file_ in files:
                    split_file = file_.split("-")
                    speaker_id = split_file[-1][:2]
                    emo = emotion_decoder[split_file[2]]
                    if any(
                        [
                            split_file[0] != "03",
                            int(speaker_id) != i,
                            len(split_file) != 7,
                        ]
                    ):
                        bad_files.add(file_)
                    else:
                        f.write(
                            "\t".join(
                                [
                                    f"{root}/{file_}",
                                    emo,
                                    valence[emo],
                                    LANG,
                                    LANG2,
                                    f"{DATASET}+{speaker_id}",
                                    "m" if int(speaker_id) % 2 else "f",
                                    f"{DATASET}\n",
                                ]
                            )
                        )

if bad_files:
    print(f"{len(bad_files)} bad files:")
    for bad in bad_files:
        print(bad)

print("done")
