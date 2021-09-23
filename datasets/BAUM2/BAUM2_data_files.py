"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the BAUM2 dataset.
"""
from os.path import exists

# I did extensive precleaning of annotations in Excel to map emotion labels into valence codes.
# Records with surprise emotion and records without useful audio were dropped.
# data_dir.xlsx was the base for preclean.tsv
# See also datasets/Notes.docx and datsets/dataset_details.xlsx for more notes on cleaning.
with open("preclean.tsv", "r") as f:
    lines = f.readlines()

ranges = [
    ("001", "050"),
    ("051", "100"),
    ("101", "150"),
    ("151", "200"),
    ("201", "250"),
    ("251", "286"),
]

for i in range(len(lines)):
    line = lines[i]
    folder, wav = line[:8].split("_")
    for a, b in ranges:
        if a <= folder[1:] <= b:
            _ = "BAUM-2_S%s_S%s" % (a, b)
            # directory BAUM-2_S001-S050 was manually renamed to BAUM-2_S001_S050 (underscore instead of dash)
            break
    lines[i] = line.split("\t")
    file = "/".join([_, folder, "wav", wav + ".wav"])
    if not exists(file):
        print("uh oh, %s doesn't exist!" % file)
    lines[i][0] = file

with open("BAUM2_data_files.tsv", "w") as f:
    [f.write("\t".join(record)) for record in lines]
print("done")
