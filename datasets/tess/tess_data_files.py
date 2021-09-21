"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Toronto Emotional Speech Set.
"""

from os import walk

LANG = "eng"  # ISO 639-3 English
LANG2 = "en-ca"  # ISO 639-1 English + ISO 3166-1 Canada
DATASET = "tess"

emotion_codes = {"angry", "disgust", "fear", "happy", "neutral", "ps", "sad"}
emotion_decoder = {
    code: (code[:3] if code != "ps" else "sur") for code in emotion_codes
}
valence = dict.fromkeys(emotion_decoder.values(), "-1")
# Surprise is pleasant surprise for this dataset
valence["hap"] = valence["sur"] = "1"
valence["neu"] = "0"

with open("MANIFEST.txt") as f:
    manifest_files = [line.split(maxsplit=1)[0] for line in f.readlines()]

actual_files = [
    file_
    for _, _, files in walk(".")
    for file_ in files
    if file_.split(".")[-1] == "wav"
]

# These do not print
if len(manifest_files) != len(set(manifest_files)):
    print("Uh oh! There are duplicates in MANIFEST.txt")
if set(manifest_files) != set(actual_files):
    print("Uh oh! MANIFEST.txt and actual files don't match")

bad_files = set()
with open("tess_data_files.tsv", "w") as f:
    for file_ in actual_files:
        try:
            f.write(
                "\t".join(
                    [
                        file_,
                        emo := emotion_decoder[
                            file_.rsplit("_", maxsplit=1)[-1].split(".")[0]
                        ],
                        valence[emo],
                        LANG,
                        LANG2,
                        f"{DATASET}+{file_[:3]}",
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
