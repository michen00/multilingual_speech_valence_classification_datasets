"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Canadian French Emotional Speech Database (cafe).
"""

from os import walk


EMO_FOLDERS = ["Colère", "Dégoût", "Joie", "Neutre", "Peur", "Surprise", "Tristesse"]
EMO_ENCODE = {
    k: v
    for k, v in zip(
        EMO_FOLDERS,
        ["ang", "dis", "hap", "neu", "fea", "sur", "sad"],
    )
}
VALENCE = {k[0]: "-1" for k in EMO_FOLDERS}
VALENCE["N"], VALENCE["J"] = "0", "1"
PREFIX = "CaFE_192k_"
LANG = "fra"  # ISO 639-3 French
LANG2 = "fr-ca"  # ISO 639-1 French + ISO 3166-1 Canada
DATASET = "cafe"

OUTFILE = "cafe_data_files.tsv"

# Clear out file contents for rewriting
open(OUTFILE, "w").close()


def write_records(folder: str, emotion: str) -> list[str]:
    """Write a list of records to file given a folder."""
    with open(OUTFILE, "a") as f:
        # folder, [], files in folder
        for _, _, files in walk(folder):
            for file in files:
                speaker = file[:2]
                f.write(
                    "\t".join(
                        [
                            "".join([folder, file]),
                            EMO_ENCODE[emotion],
                            VALENCE[emotion[0]],
                            LANG,
                            LANG2,
                            f"{DATASET}+{speaker}",
                            "m" if int(speaker) % 2 else "f",
                            f"{DATASET}\n",
                        ]
                    )
                )


for folder_num in {"1", "2"}:
    for emotion in EMO_FOLDERS:
        prefix = f"{PREFIX}{folder_num}/{emotion}/"
        if emotion == "Neutre":
            write_records(prefix, emotion)
        else:
            for subfolder in {"Faible", "Fort"}:
                write_records(f"{prefix}{subfolder}/", emotion)

print("done")
