"""
This script aggregates the prepared tsv files in each dataset folder and writes a new tsv.
The resultant tsv lists the all files that I manually identified for training a valence classifier.
"""

import os

outfile = "aggregate_data_files.tsv"

try:
    # Remove if it exists
    os.remove(outfile)
except OSError:
    pass

# Loop through a list of the directories in the current directory
with open("aggregate_data_files.tsv", "a") as f_out:
    for folder in filter(os.path.isdir, os.listdir(os.curdir)):
        with open(f"{folder}/{folder}_data_files.tsv") as f_in:
            f_out.writelines(f"{folder}/{line}" for line in f_in.readlines())

with open("aggregate_data_files.tsv", "r") as f:
    for line in f.readlines():
        if os.path.exists(path := line.split("\t", maxsplit=1)[0]):
            pass
        else:
            print("problem! a file does not exist", path)

print("done")
