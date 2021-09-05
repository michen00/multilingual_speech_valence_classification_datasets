"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Emotional Voices Database.
"""

from os import walk

LANG = "eng"  # ISO 639-3 English
LANG2 = "en-us"  # ISO 639-1 English + ISO 3166-1 United States
DATASET = "EmoV-DB_sorted"

speaker_gender = {"bea": "f", "jenie": "f", "josh": "m", "sam": "m"}
valence = dict.fromkeys(["ang", "dis"], "-1")
valence["neu"], valence["amu"] = "0", "1"
with open("EmoV-DB_sorted_data_files.tsv", "w") as f:
    for folder in speaker_gender.keys():
        for root, dirs, files in walk(folder):
            emo = root.split("\\")[-1]
            if emo == "Sleepy":
                continue
            emo = emo[:3].lower()
            for filename in files:
                f.write(
                    "\t".join(
                        [
                            "{}/{}".format(root.replace("\\", "/"), filename),
                            emo,
                            valence[emo],
                            LANG,
                            LANG2,
                            f"{DATASET}+{folder}",
                            speaker_gender[folder],
                            f"{DATASET}\n",
                        ]
                    )
                )
print("done")
