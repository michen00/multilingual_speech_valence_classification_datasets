"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the corpus provided by Lima, Castro, and Scott (2013).
"""

from os import walk
from csv import DictReader

LANG = "por"  # ISO 639-3 Portuguese
LANG2 = "pt-pt"  # ISO 639-1 Portuguese + ISO 3166-1 Portugal
DATASET = "LimaCastroScott"

emotions = (
    *(
        "anger",
        "disgust",
        "fear",
        "sadness",
    ),
    *(
        "achievement",
        "amusement",
        "pleasure",
        "relief",
    ),
)
valence = dict(zip([emo[:3] for emo in emotions], (*(["-1"] * 4), *(["1"] * 4))))
speaker_genders = {"M": "f", "T": "f", "C": "m", "MS": "m"}

actual_files = [
    stimulus_extension[0]
    for _, _, files in walk("VocalizationsCorpus")
    for file_ in files
    if (stimulus_extension := file_.split("."))[-1] == "wav"
]

# I copy pasted the csv contents from 13428_2013_324_MOESM1_ESM.xlsx
with open("supplementary_subset.csv", "r", encoding="utf-8-sig") as csvfile:
    validation_data = [*DictReader(csvfile, dialect="excel")]

bad_files = set()

if (
    sorted(actual_files)
    != sorted((stimuli := [row["Stimulus"] for row in validation_data]))
) or (set_actual := set(actual_files)) != (set_validation := set(stimuli)):
    print(
        "Uh oh! There are"
        f" {len(unaccounted := (set_actual - set_validation).union(set_validation - set_actual))} "
        "items that aren't in both file lists."
    )
    print(*unaccounted)
elif sorted(stimuli) != sorted(actual_files):
    print("files don't match!")
else:
    with open(f"{DATASET}_data_files.tsv", "w") as f:
        for row in validation_data:
            emotion, speaker, _ = (stimulus := row["Stimulus"]).split("_", maxsplit=2)
            if emotion not in emotions or emotion not in row["Emotion"].lower():
                bad_files.add((stimulus, "emotion mismatch"))
                continue
            if speaker not in speaker_genders.keys():
                bad_files.add((stimulus, "unexpected speaker"))
                continue
            if (emo_valence := valence[(emo := emotion[:3])]) != (
                # I manually verified that no row had a valence score == 50.0
                "1"
                if float(row["Valence (0-100)"]) > 50.0
                else "-1"
            ):
                bad_files.add((stimulus, "valence mismatch"))
                continue
            try:
                f.write(
                    "\t".join(
                        [
                            f"VocalizationsCorpus/{stimulus}.wav",
                            emo,
                            emo_valence,
                            LANG,
                            LANG2,
                            f"{DATASET}+{speaker}",
                            speaker_genders[speaker],
                            f"{DATASET}\n",
                        ]
                    )
                )
            except Exception as e:
                bad_files.add((stimulus, e))

if bad_files:
    print(f"{len(bad_files)} bad files:")
    for bad in bad_files:
        print(bad)

print("done")
