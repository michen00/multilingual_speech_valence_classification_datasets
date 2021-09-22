"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Variably Intense Vocalizations of Affect and Emotion Corpus.
"""

from os import walk

LANG = "eng"  # ISO 639-3 English
LANG2 = "en-us"  # ISO 639-1 English + ISO 3166-1 United States
DATASET = "vivae"

emotions = ("anger", "fear", "pain", "achievement", "pleasure", "surprise")
valence = dict(zip([emo[:3] for emo in emotions], (*(["-1"] * 3), *(["1"] * 3))))
speakers = {f"S{_:02}" for _ in range(1, 12)}

bad_files = set()
with open("vivae_data_files.tsv", "w") as f:
    for _, _, files in walk("."):
        for file_ in files:
            if file_.split(".")[-1] != "wav":
                continue
            # e.g., S04_surprise_peak_10.wav
            speaker_id, emotion, _ = file_.split("_", maxsplit=2)
            if emotion not in emotions or speaker_id not in speakers:
                bad_files.add((file_, "unexpected file name"))
            try:
                f.write(
                    "\t".join(
                        [
                            file_,
                            emo := emotion[:3],
                            valence[emo],
                            LANG,
                            LANG2,
                            f"{DATASET}+{speaker_id}",
                            "f",
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
