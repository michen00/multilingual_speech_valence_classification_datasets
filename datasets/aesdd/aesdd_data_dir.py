"""
This script lists the filepaths and metadata for records retained for model development in a tab-delimited csv.
The resultant csv is used to help aggregate all records for feature extraction from the audio signal.
Records are from the Acted Emotional Speech Dynamic Database.
"""

from os import walk

dirs = ["anger", "disgust", "fear", "happiness", "sadness"]
emo_encode = {k: v for k, v in zip(dirs, ["ang", "dis", "fea", "hap", "sad"])}
print(emo_encode)
lang = "ell"  # ISO 639-2/3 Greek
out = []

for root, _, files in walk("."):
    for filename in files:
        emo = root[2:]
        if emo in dirs:
            path = "\\".join(["aesdd", emo, filename])
            val = "1" if emo == "happiness" else "-1"
            out.append([path, emo_encode[emo], val, lang, "aesdd\n"])

with open("data_dir.tsv", "w") as f:
    [f.write("\t".join(record)) for record in out]
