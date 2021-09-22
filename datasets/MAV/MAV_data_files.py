"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Montreal Affective Voices.
"""

from os import walk

LANG = "fra"  # ISO 639-3 French
LANG2 = "fr-ca"  # ISO 639-1 French + ISO 3166-1 Canada
DATASET = "MAV"

# anger, disgust, fear, pain, sadness, surprise, happiness, pleasure, neutral
emotions = (
    *(
        "anger",
        "disgust",
        "fear",
        "pain",
        "sadness",
        "surprise",
    ),
    *(
        "happiness",
        "pleasure",
    ),
    "neutral",
)
valence = dict(zip([emo[:3] for emo in emotions], (*(["-1"] * 6), *(["1"] * 2), "0")))
speaker_genders = {
    "6": "m",
    "42": "m",
    "45": "f",
    "46": "f",
    "53": "f",
    "55": "m",
    "58": "f",
    "59": "m",
    "60": "f",
    "61": "m",
}

bad_files = set()

with open(f"{DATASET}_data_files.tsv", "w") as f:
    for _, _, files in walk("."):
        for file_ in files:
            if file_[-3:] != "wav":
                continue
            speaker_num, emotion = file_.split("_")
            if (
                emotion[:-4] not in emotions
                or speaker_num not in speaker_genders.keys()
            ):
                bad_files.add((file_, "unexpected file name"))
                continue
            try:
                f.write(
                    "\t".join(
                        [
                            file_,
                            emo := emotion[:3],
                            valence[emo],
                            LANG,
                            LANG2,
                            f"{DATASET}+{speaker_num}",
                            speaker_genders[speaker_num],
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
