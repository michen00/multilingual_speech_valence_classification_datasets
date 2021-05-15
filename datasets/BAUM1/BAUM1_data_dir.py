"""
This script lists the filepaths and metadata for records retained for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records for feature extraction from the audio signal.
Records are from BAUM-1.
"""

from os.path import exists

# I copied and pasted from Annotations_BAUM1a.xlsx and Annotations_BAUM1s.xlsx to make preclean.tsv with a newline between the subsets
with open("preclean.tsv", "r") as f:
    lines = f.readlines()

codemaker = lambda x: {
    k: v for k, v in zip(["".join((str(_), "\n")) for _ in range(1, len(x) + 1)], x)
}
codes_act, codes_spo = codemaker(
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

keep_emos = ["ang", "con", "dis", "fea", "hap", "neu", "sad"]
valence = {k: "-1" for k in keep_emos}
valence["neu"], valence["hap"] = "0", "1"

lang = "tur"  # ISO 639-2/3 Turkish
out = []

for record in acted:
    file, emo, code = record.split("\t")
    emo = emo[:3].lower()
    if codes_act[code] != emo:
        print("uh oh, emo code does not match label in annotations", file)
    elif emo in keep_emos:
        speaker = file.lower().split("_", 1)[0]
        file = "\\".join(("BAUM1a_MP4_all", speaker, ".".join((file, "mp4"))))
        out.append("\t".join((file, emo, valence[emo], lang, "BAUM1\n")))

for record in spont:
    file, emo, code = record.split("\t")
    if emo == "Concentrating":
        if code != "4\n":
            print("uh oh, emo code does not match label in annotations", file)
        continue
    emo = emo[:3].lower()
    if codes_spo[code] != emo:
        print("uh oh, emo code does not match label in annotations", file)
        # S015_007 was flagged and manually corrected in preclean.tsv
        # it was ambiguous whether it was happy or neutral in the annotation file (spontaneous)
        # it was pretty obvious to me that it was a happy sample (smiling and laughing)
    elif emo in keep_emos:
        speaker = file.lower().split("_", 1)[0]
        file = "\\".join(("BAUM1s_MP4 - All", speaker, ".".join((file, "mp4"))))
        if not exists(file):
            print("uh oh, %s doesn't exist!" % file)
        out.append("\t".join((file, emo, valence[emo], lang, "BAUM1\n")))

with open("data_dir.tsv", "w") as f:
    [f.write(record) for record in out]
