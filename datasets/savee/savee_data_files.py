"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Surrey Audio-Visual Expressed Emotion Database.
"""

from os import walk

LANG = "eng"  # ISO 639-3 English
LANG2 = "en-gb"  # ISO 639-1 English + ISO 3166-1 United Kingdom of Great Britain and Northern Ireland
DATASET = "savee"

emotions = ("ang", "dis", "fea", "hap", "neu", "sad", "sur")
emotion_decoder = dict(
    zip([first if (first := emo[0]) != "s" else emo[:2] for emo in emotions], emotions)
)
valence = dict.fromkeys(emotions, "-1")
valence["hap"], valence["neu"] = "1", "0"

# (file, emotion, valence, speaker_gender, speaker_id)
manual_records = {
    ("anger02", "ang", "-1", "f", "f0"),
    ("disgust01", "unk", "-1", "m", "HaroldKumar"),
    ("fear01", "fea", "-1", "m", "m0"),
    ("fear04", "fea", "-1", "m", "HaroldKumar"),
    ("happiness01", "hap", "1", "m", "m1"),
    ("neutral01", "neu", "0", "m", "NicCage"),
    ("surprise02", "sur", "-1", "f", "f1"),
    ("surprise10", "sur", "-1", "f", "omg"),
}

bad_files = set()
with open("savee_data_files.tsv", "w") as f:
    for speaker in {"DC", "JE", "JK", "KL"}:
        for root, _, files in walk(f"AudioData/{speaker}"):
            for file_ in files:
                try:
                    f.write(
                        "\t".join(
                            [
                                path := f"{root}/{file_}",
                                emo := emotion_decoder[
                                    first if (first := file_[0]) != "s" else file_[:2]
                                ],
                                valence[emo],
                                LANG,
                                LANG2,
                                f"{DATASET}+{speaker}",
                                "m",
                                f"{DATASET}\n",
                            ]
                        )
                    )
                except Exception as e:
                    bad_files.add((path, e))
    # Manually add some files from MetaData folder
    for record in manual_records:
        try:
            # (file, emotion, valence, speaker_gender, speaker_id)
            f.write(
                "\t".join(
                    [
                        path := f"Metadata/{record[0]}.wmv",
                        record[1],
                        record[2],
                        LANG,
                        LANG2,
                        f"{DATASET}+{record[-1]}",
                        record[-2],
                        f"{DATASET}\n",
                    ]
                )
            )
        except Exception as e:
            bad_files.add((path, e))


if bad_files:
    print(f"{len(bad_files)} bad files:")
    for bad in bad_files:
        print(bad)

print("done")
