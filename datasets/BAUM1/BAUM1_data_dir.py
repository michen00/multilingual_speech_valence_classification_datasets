"""
This script lists the filepaths and metadata for records retained for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records for feature extraction from the audio signal.
Records are from BAUM-1.
"""

from os.path import exists

# I copied and pasted from Annotations_BAUM1a.xlsx and Annotations_BAUM1s.xlsx to make preclean.tsv with a newline between the subsets
with open("preclean.tsv", "r") as f:
    lines = f.readlines()

codemaker = lambda x: {k: v for k, v in zip([str(_) for _ in range(1, len(x) + 1)], x)}
CODES_ACT, CODES_SPO = codemaker(
    ["ang", "bor", "dis", "fea", "hap", "int", "sad", "sur", "uns"]
), codemaker(
    [
        "ang",
        "bor",
        "bot",
        "con",
        "con",
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

# I set the 266th line in preclean.tsv to a single newline
acted = lines[:265]
spont = lines[266:]

KEEP_EMOS = ["ang", "bor", "con", "dis", "fea", "hap", "int", "neu", "sad", "sur"]
VALENCE = {k: "-1" for k in KEEP_EMOS}
VALENCE["neu"] = "0"
VALENCE["hap"], VALENCE["int"] = "1", "1"

LANG = "tur"  # ISO 639-2/3 Turkish
out = []

for record in acted:
    file, emo, code, gender = record.rstrip().lower().split("\t")
    emo = emo[:3]
    if CODES_ACT[code] != emo:
        print("uh oh, emo code does not match label in annotations", file)
    elif emo in KEEP_EMOS:
        speaker = file.lower().split("_", 1)[0]
        file = "\\".join(("BAUM1a_MP4_all", speaker, ".".join((file, "mp4"))))
        out.append("\t".join((file, emo, VALENCE[emo], LANG, gender, "BAUM1\n")))

for record in spont:
    file, emo, code, gender = record.rstrip().lower().split("\t")
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
        file = "\\".join(("BAUM1s_MP4 - All", speaker, ".".join((file, "mp4"))))
        if not exists(file):
            print("uh oh, %s doesn't exist!" % file)
        out.append("\t".join((file, emo, VALENCE[emo], LANG, gender, "BAUM1\n")))

with open("data_dir.tsv", "w") as f:
    [f.write(record) for record in out]
print("done")
