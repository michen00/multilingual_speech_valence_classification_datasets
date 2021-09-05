"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Egyptian Arabic speech emotion database (EYASE).
"""

from os import walk

LANG = "arz"  # ISO 639-3 Egyptian Arabic
LANG2 = "ar-eg"  # ISO 639-1 Arabic + ISO 3166-1 Egypt
DATASET = "EYASE"

valence = dict.fromkeys(["ang", "sad"], "-1")
valence["hap"], valence["neu"] = "1", "0"

with open("EYASE_data_files.tsv", "w") as f:
    for gender in {"Female", "Male"}:
        for number in {"01", "02", "03"}:
            folder = f"{gender}{number}"
            for _, _, files in walk(folder):
                for file_ in files:
                    emo = file_.split()[0].split("_")[-1]
                    f.write(
                        "\t".join(
                            [
                                f"{folder}/{file_}",
                                emo,
                                valence[emo],
                                LANG,
                                LANG2,
                                f"{DATASET}+{folder}",
                                gender[0].lower(),
                                f"{DATASET}\n",
                            ]
                        )
                    )
print("done")
