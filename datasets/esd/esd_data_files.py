"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Emotional Speech Dataset.
"""

from os import walk

eng1 = "eng"  # ISO 639-3 English
eng2 = "en-us"  # ISO 639-1 English + ISO 3166-1 United States
zho1 = "cmn"  # 639-3 Mandarin Chinese
zho2 = "zh-cn"  # ISO 639-1 Chinese + ISO 3166-1 PRC

speaker_gender = {
    "0001": "f",
    "0002": "f",
    "0003": "f",
    "0004": "m",
    "0005": "m",
    "0006": "m",
    "0007": "f",
    "0008": "m",
    "0009": "f",
    "0010": "m",
    "0011": "m",
    "0012": "m",
    "0013": "m",
    "0014": "m",
    "0015": "f",
    "0016": "f",
    "0017": "f",
    "0018": "f",
    "0019": "f",
    "0020": "m",
}

valence = dict.fromkeys(["ang", "sad", "sur"], "-1")
valence["hap"], valence["neu"] = "1", "0"

with open("esd_data_files.tsv", "w") as f:
    for speaker in speaker_gender.keys():
        lang, lang2 = (zho1, zho2) if 1 <= int(speaker) <= 10 else (eng1, eng2)
        for emotion_folder in {"Angry", "Happy", "Neutral", "Sad", "Surprise"}:
            root = f"{speaker}/{emotion_folder}/"
            emo = emotion_folder[:3].lower()
            for _, _, files in walk(root):
                for file_ in files:
                    f.write(
                        "\t".join(
                            [
                                f"{root}{file_}",
                                emo,
                                valence[emo],
                                lang,
                                lang2,
                                speaker_gender[speaker],
                                "esd\n",
                            ]
                        )
                    )
print("done")
