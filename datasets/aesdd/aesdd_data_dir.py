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

LANG = "ell"  # ISO 639-2/3 Greek
out = []

for root, _, files in walk("."):
    for filename in files:
        emo = root[2:]
        if emo in DIRS:
            path = "\\".join([emo, filename])
            if not exists(path):
                print(f"uh oh, {path} doesn't exist!")
            # e.g. 'a03 (4).wav' is the 3rd utterance spoken by the 4th speaker with anger
            speaker_gender = SPEAKERS[int(filename.split(")")[0][-1])]
            val = "1" if emo == "happiness" else "-1"
            out.append([path, EMO_ENCODE[emo], val, LANG, speaker_gender, "aesdd\n"])

with open("data_dir.tsv", "w") as f:
    [f.write("\t".join(record)) for record in out]
print("done")
