"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Sharif Emotional Speech Database.
"""

from os import walk

LANG = "pes"  # ISO 639-3 Iranian Persian
LANG2 = "fa-ir"  # ISO 639-1 Persian + ISO 3166-1 Iran
DATASET = "ShEMO"

emotions = ("ang", "fea", "hap", "neu", "sad", "sur")
emotion_decoder = dict(
    zip([emo[0].upper() if emo != "sur" else "W" for emo in emotions], emotions)
)
valence = dict.fromkeys(emotions, "-1")
valence["hap"], valence["neu"] = "1", "0"

first_lower: str = lambda _: _[0].lower()

bad_files = set()
with open("ShEMO_data_files.tsv", "w") as f:
    for folder_gender in {"female", "male"}:
        for root, _, files in walk(folder_gender):
            for file_ in files:
                path = f"{root}/{file_}"
                if (
                    speaker_gender := first_lower(speaker_id := file_[:3])
                ) != first_lower(folder_gender) or (
                    emo_code := file_[3]
                ) not in emotion_decoder.keys():
                    bad_files.add(path)
                    continue
                f.write(
                    "\t".join(
                        [
                            path,
                            emo := emotion_decoder[emo_code],
                            valence[emo],
                            LANG,
                            LANG2,
                            f"{DATASET}+{speaker_id}",
                            speaker_gender,
                            f"{DATASET}\n",
                        ]
                    )
                )


if bad_files:
    print(f"{len(bad_files)} bad files:")
    for bad in bad_files:
        print(bad)

print("done")
