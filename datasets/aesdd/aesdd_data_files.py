"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Acted Emotional Speech Dynamic Database (aesdd).
"""

from os import walk
from os.path import exists

SPEAKERS = [None, "f", "f", "m", "m", "f", "m"]
DIRS = ["anger", "disgust", "fear", "happiness", "sadness"]
EMO_ENCODE = {k: v for k, v in zip(DIRS, ["ang", "dis", "fea", "hap", "sad"])}
# no neutral in this dataset

DATASET = "aesdd"
LANG = "ell"  # ISO 639-3 Modern Greek
LANG2 = "el-gr"  # ISO 639-1 Modern Greek + ISO 3166-1 Greece
with open("aesdd_data_files.tsv", "w") as f:
    for root, _, files in walk("."):
        for filename in files:
            emo = root[2:]
            if emo in DIRS:
                if not exists(path := f"{emo}/{filename}"):
                    print(f"uh oh, {path} doesn't exist!")
                # e.g. 'a03 (4).wav' is the 3rd utterance spoken by the 4th speaker with anger
                speaker = int(filename.split(")")[0][-1])
                speaker_gender = SPEAKERS[speaker]
                val = "1" if emo == "happiness" else "-1"
                f.write(
                    "\t".join(
                        [
                            path,
                            EMO_ENCODE[emo],
                            val,
                            LANG,
                            LANG2,
                            f"{DATASET}+{speaker}",
                            speaker_gender,
                            f"{DATASET}\n",
                        ]
                    )
                )
print("done")
