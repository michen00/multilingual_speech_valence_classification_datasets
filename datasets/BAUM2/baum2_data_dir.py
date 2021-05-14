"""
This script lists the filepaths and metadata for records retained for model development in a tab-delimited csv.
The resultant csv is used to help aggregate all records for feature extraction from the audio signal.
Records are from the BAUM2 dataset.
"""

with open("preclean.tsv", "r") as f:
    lines = f.readlines()

ranges = [
    ("001", "050"),
    ("051", "100"),
    ("101", "150"),
    ("151", "200"),
    ("201", "250"),
    ("251", "285"),
]

for i in range(len(lines)):
    line = lines[i]
    folder, wav = line[:8].split("_")
    for a, b in ranges:
        if a <= folder[1:] <= b:
            _ = "BAUM-2_S%s-S%s" % (a, b)
            break
    lines[i] = line.split("\t")
    lines[i][0] = "\\".join([_, folder, "wav", wav + ".wav"])

with open("data_dir.tsv", "w") as f:
    [f.write("\t".join(record)) for record in lines]
