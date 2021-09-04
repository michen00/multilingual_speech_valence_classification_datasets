"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the eNTERFACE’05 Audio-Visual Emotion Database.
"""

from os import walk

LANG = "eng"  # ISO 639-3 English
LANG2 = "en"  # ISO 639-1 English

speaker_gender = {
    "1": "m",
    "2": "m",
    "3": "m",
    "4": "f",
    "5": "f",
    "6": "m",
    "7": "f",
    "8": "m",
    "9": "m",
    "10": "m",
    "11": "m",
    "12": "m",
    "13": "m",
    "14": "m",
    "15": "m",
    "16": "m",
    "17": "m",
    "18": "m",
    "19": "m",
    "20": "m",
    "21": "m",
    "22": "m",
    "23": "m",
    "24": "m",
    "25": "m",
    "26": "f",
    "27": "m",
    "28": "f",
    "29": "f",
    "30": "m",
    "31": "f",
    "32": "m",
    "33": "f",
    "34": "m",
    "35": "m",
    "36": "m",
    "37": "m",
    "38": "m",
    "39": "m",
    "40": "m",
    "41": "m",
    "42": "m",
    "43": "m",
    "44": "f",
}

valence = dict.fromkeys(["ang", "dis", "fea", "sad", "sur"], "-1")
valence["hap"] = "1"

emo_decoder = {key[:2]: key for key in valence.keys()}

with open("enterface_db_data_files.tsv", "w") as f:
    for root, dirs, files in walk("."):
        for file_ in files:
            filepath = "{}/{}".format(root[2:].replace("\\", "/"), file_)
            try:
                speaker, emo, _ = file_.split("_")
                speaker = speaker.split("s")[-1]
            except ValueError:
                if file_.split(".")[-1] != "avi":
                    continue
                under_split = file_.split("_")
                s_split = under_split[0].split("s")
                if any(s_split):
                    emo = under_split[1].split(".")[0]
                    speaker = s_split[-1]
                else:
                    emo = under_split[2]
                    speaker = under_split[1]
            emo = emo_decoder[emo]
            f.write(
                "\t".join(
                    [
                        filepath,
                        emo,
                        valence[emo],
                        LANG,
                        LANG2,
                        speaker_gender[speaker],
                        "enterface_db\n",
                    ]
                )
            )
print("done")
