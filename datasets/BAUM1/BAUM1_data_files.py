"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from BAUM-1.
"""

from os.path import exists

# I copied and pasted from Annotations_BAUM1a.xlsx and Annotations_BAUM1s.xlsx to make preclean.tsv with a newline between the subsets
with open("preclean.tsv", "r", encoding="utf-8-sig") as f:
    lines = f.readlines()

# retroactive fix: change "uns" to "unc" and "int" to "cur"
fixed_emo = lambda emo: "unc" if emo == "uns" else "cur" if emo == "int" else emo

codemaker = lambda x: {k: v for k, v in zip([str(_) for _ in range(1, len(x) + 1)], x)}
# codes in the acted and spontaneous sets
CODES_ACT, CODES_SPO = codemaker(
    ["ang", "bor", "dis", "fea", "hap", "int", "sad", "sur", "uns"]
), codemaker(
    [
        "ang",
        "bor",
        "bot",
        "con",  # concentrating
        "con",  # contempt
        "dis",
        "fea",
        "hap",
        "neu",
        "sad",
        "sur",
        "thi",
        "uns",
    ]
)

# I set the 275th line in preclean.tsv to a single newline
acted = lines[:274]
spont = lines[275:]

KEEP_EMOS = [
    "ang",
    "bor",
    "bot",
    "con",
    "dis",
    "fea",
    "hap",
    "int",
    "neu",
    "sad",
    "sur",
    "uns",
]
VALENCE = {k: "-1" for k in KEEP_EMOS}
VALENCE["neu"] = "0"
VALENCE["hap"], VALENCE["int"] = "1", "1"

LANG = "tur"  # ISO 639-3 Turkish
LANG2 = "tr-tr"  # ISO 639-1 Turkish + ISO 3166-1 Turkey
DATASET = "BAUM1"

out = []

# The next two for loops are not DRY, but keeping them separate helped me validate the data

for record in acted:
    file, emo, code, gender = record.rstrip().lower().split("\t")
    emo = emo[:3]
    if CODES_ACT[code] != emo:
        print("uh oh, emo code does not match label in annotations", file)
    elif emo in KEEP_EMOS:
        speaker = file.lower().split("_", 1)[0]
        out.append(
            "\t".join(
                (
                    f"BAUM1a_MP4_all/{speaker}/{file.upper()}.mp4",
                    fixed_emo(emo),
                    VALENCE[emo],
                    LANG,
                    LANG2,
                    f"{DATASET}+{speaker}",
                    gender,
                    f"{DATASET}\n",
                )
            )
        )

for record in spont:
    file, emo, code, gender = record.rstrip().lower().split("\t")
    # disambiguate contempt and concentrating
    if emo == "Concentrating" and code != "4":
        print("uh oh, emo code does not match label in annotations", file)
    emo = emo[:3].lower()
    if CODES_SPO[code] != emo:
        print("uh oh, emo code does not match label in annotations", file)
        # S015_007 was flagged and manually corrected in preclean.tsv
        # it was ambiguous whether it was happy or neutral in the annotation file (spontaneous)
        # it was pretty obvious to me that it was a happy sample (smiling and laughing)
    elif emo in KEEP_EMOS:
        speaker = file.lower().split("_", 1)[0]
        if not exists(file := f"BAUM1s_MP4 - All/{speaker}/{file.upper()}.mp4"):
            # This never happens since all s files exist
            print("uh oh, %s doesn't exist!" % file)
        out.append(
            "\t".join(
                (
                    file,
                    fixed_emo(emo),
                    VALENCE[emo],
                    LANG,
                    LANG2,
                    f"{DATASET}+{speaker}",
                    gender,
                    f"{DATASET}\n",
                )
            )
        )

with open("BAUM1_data_files.tsv", "w") as f:
    [f.write(record) for record in out]
print("done")
