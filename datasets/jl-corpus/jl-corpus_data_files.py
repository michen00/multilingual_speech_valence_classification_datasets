"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the JL Corpus.
"""

from os import walk

LANG = "eng"  # ISO 639-3 English
LANG2 = "en-nz"  # ISO 639-1 English + ISO 3166-1 New Zealand
DATASET = "jl-corpus"

valence = {
    "neu": "0",
    **dict.fromkeys(["ang", "apo", "anx", "sad", "wor"], "-1"),
    **dict.fromkeys(["hap", "ent", "exc", "pen"], "1"),
}

folder = "Raw JL corpus (unchecked and unannotated)/JL(wav+txt)"
with open("jl-corpus_data_files.tsv", "w") as f:
    for _, _, files in walk(folder):
        for file_ in files:
            if file_.split(".")[-1] == "wav":
                speaker, emo, _ = file_.split("_", 2)
                emo = emo[:3]
                if emo in valence.keys():
                    f.write(
                        "\t".join(
                            [
                                f"{folder}/{file_}",
                                emo,
                                valence[emo],
                                LANG,
                                LANG2,
                                f"{DATASET}+{speaker}",
                                file_[0],
                                f"{DATASET}\n",
                            ]
                        )
                    )
print("done")
