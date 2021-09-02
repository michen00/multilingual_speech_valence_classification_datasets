"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Crowd-sourced Emotional Multimodal Actors Dataset (CREMA-D).
"""

# Basically copy-pasted from VideoDemographics.csv
ACTORID_GENDER = {
    "1001": "m",
    "1002": "f",
    "1003": "f",
    "1004": "f",
    "1005": "m",
    "1006": "f",
    "1007": "f",
    "1008": "f",
    "1009": "f",
    "1010": "f",
    "1011": "m",
    "1012": "f",
    "1013": "f",
    "1014": "m",
    "1015": "m",
    "1016": "m",
    "1017": "m",
    "1018": "f",
    "1019": "m",
    "1020": "f",
    "1021": "f",
    "1022": "m",
    "1023": "m",
    "1024": "f",
    "1025": "f",
    "1026": "m",
    "1027": "m",
    "1028": "f",
    "1029": "f",
    "1030": "f",
    "1031": "m",
    "1032": "m",
    "1033": "m",
    "1034": "m",
    "1035": "m",
    "1036": "m",
    "1037": "f",
    "1038": "m",
    "1039": "m",
    "1040": "m",
    "1041": "m",
    "1042": "m",
    "1043": "f",
    "1044": "m",
    "1045": "m",
    "1046": "f",
    "1047": "f",
    "1048": "m",
    "1049": "f",
    "1050": "m",
    "1051": "m",
    "1052": "f",
    "1053": "f",
    "1054": "f",
    "1055": "f",
    "1056": "f",
    "1057": "m",
    "1058": "f",
    "1059": "m",
    "1060": "f",
    "1061": "f",
    "1062": "m",
    "1063": "f",
    "1064": "m",
    "1065": "m",
    "1066": "m",
    "1067": "m",
    "1068": "m",
    "1069": "m",
    "1070": "m",
    "1071": "m",
    "1072": "f",
    "1073": "f",
    "1074": "f",
    "1075": "f",
    "1076": "f",
    "1077": "m",
    "1078": "f",
    "1079": "f",
    "1080": "m",
    "1081": "m",
    "1082": "f",
    "1083": "m",
    "1084": "f",
    "1085": "m",
    "1086": "m",
    "1087": "m",
    "1088": "m",
    "1089": "f",
    "1090": "m",
    "1091": "f",
}

LANG = "eng"  # ISO 639-3 English
LANG2 = "en-us"  # ISO 639-1 English (United States)

VALENCE = dict.fromkeys(["ANG", "DIS", "HAP", "NEU", "FEA", "SAD"], "-1")
VALENCE["NEU"], VALENCE["HAP"] = "0", "1"

# filelist is copy-pasted from data_selection.xlsx
with open("filelist", "r") as f1:
    with open("CREMA-D_data_files.tsv", "w") as f2:
        for line in f1:
            actor_id, _, emotion, _ = line.split("_")
            f2.write(
                "\t".join(
                    [
                        f"AudioWAV/{line.rstrip()}.wav",
                        emotion.lower(),
                        VALENCE[emotion],
                        LANG,
                        LANG2,
                        ACTORID_GENDER[actor_id],
                        "CREMA-D\n",
                    ]
                )
            )
print("done")
