"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Urdu Language Speech Dataset.
"""

from os import walk

LANG = "urd"  # ISO 639-3 Urdu
LANG2 = "ur"  # ISO 639-1 Urdu
DATASET = "urdu"

emotions = ("ang", "hap", "neu", "sad")
emotion_decoder = dict(zip([emotion[0].upper() for emotion in emotions], emotions))
valence = dict.fromkeys(emotions, "-1")
valence["hap"], valence["neu"] = "1", "0"

bad_files = set()
with open("urdu_data_files.tsv", "w") as f:
    for emo_folder in {"Angry", "Happy", "Neutral", "Sad"}:
        for root, _, files in walk(f"{emo_folder}"):
            for file_ in files:
                speaker_id, _, emo_part = file_.split("_")
                if (emo_code := emo_part[0]) != emo_folder[0]:
                    # This does not print
                    bad_files.add(file_)
                    print(f"Unexpected emotion code for {file_}")
                    continue
                try:
                    f.write(
                        "\t".join(
                            [
                                f"{root}/{file_}",
                                emo := emotion_decoder[emo_code],
                                valence[emo],
                                LANG,
                                LANG2,
                                f"{DATASET}+{speaker_id}",
                                speaker_id[1].lower(),
                                f"{DATASET}\n",
                            ]
                        )
                    )
                except Exception as e:
                    bad_files.add((file_, e))

if bad_files:
    print(f"{len(bad_files)} bad files:")
    for bad in bad_files:
        print(bad)

print("done")
