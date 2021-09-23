"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Morgan Emotional Speech Set.
"""

from os import walk
import csv

LANG = "eng"  # ISO 639-3 English
LANG2 = "en-us"  # ISO 639-1 English + ISO 3166-1 United States
DATASET = "MESS"

emotions = ("ang", "hap", "cal", "sad")
emotion_decoder = dict(zip([emotion[0].upper() for emotion in emotions], emotions))
valence = dict.fromkeys(emotions, "-1")
valence["hap"] = valence["cal"] = "1"

with open("Coded stimuli - final MESS.csv", "r") as csvfile:
    validation_data = csv.DictReader(csvfile, dialect="excel")
    len_validation_data = len(validation_data := [*validation_data])
    validation_data = {
        record["code"]: {
            key: record[key]
            for key in {
                "Emotion",
                "Gender",
                "Talker",
                "Cue",
                "sentencenum",
                "code",
                "Valence",
                "Category_Accuracy",
                "GoF",
                "Percent_A",
                "Percent_C",
                "Percent_H",
                "Percent_S",
            }
        }
        for record in validation_data
    }
if (validation_len := len(validation_data)) != len_validation_data:
    print(
        f"Uh oh! Found {validation_len} rows when there should've been {len_validation_data}"
    )

actual_files = [
    code_extension[0][:-4]
    for _, _, files in walk(".")
    for file_ in files
    if (code_extension := file_.split("."))[-1] == "wav"
]

if validation_len != (actual_len := len(actual_files)):
    print(
        f"Uh oh! There are {validation_len} items in validation_data and {actual_len} actual files."
    )

if (
    sorted(actual_files) != sorted(validation_data.keys())
    or (set_actual := set(actual_files))
) != (set_validation := set(validation_data.keys())):
    print(
        "Uh oh! There are"
        f" {len(unaccounted := (set_actual - set_validation).union(set_validation - set_actual))} "
        "items that aren't in both file lists."
    )
    print(*unaccounted)

bad_files = set()

with open("MESS_data_files.tsv", "w") as f:
    for row in validation_data.keys():
        record = validation_data[row]
        if record["code"] != row or row != "".join(
            (
                emo_code := record["Emotion"],
                gender := record["Gender"],
                speaker_num := record["Talker"],
                record["Cue"],
                f"{int(record['sentencenum']):02}",
            )
        ):
            bad_files.add((row, "bad format"))
            continue
        record_valence = "1" if float(record["Valence"]) > 50.0 else "-1"
        if ("1" if float(record["Valence"]) > 50.0 else "-1") != (
            # I manually checked to make sure none of the valence scores == 50.0
            emo_valence := valence[(emo := emotion_decoder[emo_code])]
        ):
            bad_files.add((row, "valence mismatch"))
            continue
        try:
            f.write(
                "\t".join(
                    [
                        f"{row}_SCR.wav",
                        emo := emotion_decoder[emo_code],
                        valence[emo],
                        LANG,
                        LANG2,
                        f"{DATASET}+{gender}{speaker_num}",
                        gender.lower(),
                        f"{DATASET}\n",
                    ]
                )
            )
        except Exception as e:
            bad_files.add((row, e))

float_bad_record: float = lambda x: float(bad_record[x])
with open("MESS_data_files.tsv", "a") as f:
    while bad_files:
        bad_record = validation_data[bad_files.pop()[0]]
        code, emo_code = bad_record["code"], bad_record["Emotion"]
        if (
            float_bad_record("GoF") < 60.0
            or float_bad_record("Category_Accuracy") < 0.6
            or (float_bad_record("Percent_C") < 0.6 and emo_code == "C")
            or ((50.0 - float_bad_record("Valence") > 6.25) and emo_code in {"C", "H"})
        ):
            print("rejected:", code)
        else:
            try:
                f.write(
                    "\t".join(
                        [
                            f"{code}_SCR.wav",
                            emo := emotion_decoder[emo_code],
                            # Calm audio with mismatched valence perception recoded as neutral calm
                            "0" if emo_code == "C" else valence[emo],
                            LANG,
                            LANG2,
                            f"{DATASET}+{code[1:3]}",
                            code[1].lower(),
                            f"{DATASET}\n",
                        ]
                    )
                )
            except Exception as e:
                bad_files.add((row, e))

if bad_files:
    print("bad files remain!")

print("done")
