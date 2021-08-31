"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Berlin Database of Emotional Speech (EmoDB).
"""

from os import walk


LANG = "deu"  # ISO 639-3 German
EMO_CODE = {
    "W": "ang",
    "L": "bor",
    "E": "dis",
    "A": "fea",
    "F": "hap",
    "T": "sad",
    "N": "neu",
}
VALENCE = dict.fromkeys(EMO_CODE.values(), "-1")
VALENCE["hap"], VALENCE["neu"] = "1", "0"

SPEAKER_GENDER = {
    "03": "m",
    "08": "f",
    "09": "f",
    "10": "m",
    "11": "m",
    "12": "m",
    "13": "f",
    "14": "f",
    "15": "m",
    "16": "f",
}

# folder, [], files in folder
with open("EmoDB_data_files.tsv", "w") as f:
    for _, _, files in walk("."):
        for file in files:
            if len(file) >= 4 and file[-4:] == ".wav":
                # Every utterance is named according to the same scheme:
                # Positions 1-2: number of speaker
                # Positions 3-5: code for text
                # Position 6: emotion (letter stands for german emotion word)
                # Position 7: if there are more than two versions these are numbered a, b, c ....
                # Example: 03a01Fa.wav is the audio file from Speaker 03 speaking text a01 with the emotion "Freude" (Happiness).
                emotion = EMO_CODE[file[5]]
                f.write(
                    "\t".join(
                        [
                            file,
                            emotion,
                            VALENCE[emotion],
                            LANG,
                            SPEAKER_GENDER[file[:2]],
                            "EmoDB\n",
                        ]
                    )
                )
print("done")
