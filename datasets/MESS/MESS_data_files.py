"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Morgan Emotional Speech Set.
"""

from os import walk

LANG = "eng"  # ISO 639-3 English
LANG2 = "en"  # -us"  # ISO 639-1 English + ISO 3166-1 United States
# But there is one Canadian English speaker
DATASET = "MESS"

emotions = ("ang", "hap", "cal", "sad")
emotion_decoder = dict(zip([emotion[0].upper() for emotion in emotions], emotions))
valence = dict.fromkeys(emotions, "-1")
valence["hap"] = valence["cal"] = "1"

bad_files = set()
with open("MESS_data_files.tsv", "w") as f:
    for root, _, files in walk("."):
        for file_ in files:
            # Example: AF1M01_SCR.wav
            if file_[-3:] != "wav":
                continue
            try:
                f.write(
                    "\t".join(
                        [
                            file_,
                            emo := emotion_decoder[file_[0]],
                            valence[emo],
                            LANG,
                            LANG2,
                            f"{DATASET}+{file_[1:3]}",
                            file_[1].lower(),
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
