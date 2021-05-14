"""
This script lists the filepaths and metadata for records retained for model development in a tab-delimited csv.
The resultant csv is used to help aggregate all records for feature extraction from the audio signal.
Records are from the BAUM2 dataset.
"""

with open("temp_csv.csv", "r") as f:
    lines = f.readlines()
files = []
for i in range(len(lines)):
    line = lines[i]
    wav_loc = line[:8]
    which_folder = wav_loc[1:4]