"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the French Emotional Speech Database - Oréau v2.
"""

from os import walk

LANG = "fra"  # ISO 639-3 French
LANG2 = "fr"  # ISO 639-1 French
DATASET = "oreau2"

emo_chars = ("c", "d", "j", "n", "p", "s", "t")
emotion = dict(zip(emo_chars, ("ang", "dis", "hap", "neu", "fea", "sur", "sad")))
valence = dict.fromkeys(emotion.keys(), "-1")
valence["j"], valence["n"] = "1", "0"

speaker_gender_tracker = {}
bad_files = set()
with open("oreau2_data_files.tsv", "w") as f:
    for speaker_gender in {"f", "m"}:
        for emo_char in emo_chars:
            for root, _, files in walk(f"{speaker_gender}/sess{emo_char}"):
                for file_ in files:
                    speaker_id, emo_char2, extension = file_.split("a", 2)
                    emo_char2 = emo_char2[-1].lower()
                    path = f"{root}/{file_}"
                    if speaker_id in speaker_gender_tracker.keys():
                        if speaker_gender_tracker[speaker_id] != speaker_gender:
                            print(f"speaker gender problem for {path}")
                            bad_files.add(path)
                            continue
                    else:
                        speaker_gender_tracker[speaker_id] = speaker_gender
                    if extension != ".wav":
                        if path == "m/sesss/07z03Sa.wav" or "m/sesss/07z04Sa.wav":
                            speaker_id, emo_char2 = "07", "s"
                        else:
                            print(f"extension problem for {path}")
                            bad_files.add(path)
                            continue
                    if emo_char != emo_char2:
                        print(f"emo_char problem for {path}")
                        bad_files.add(path)
                        continue
                    f.write(
                        "\t".join(
                            [
                                path,
                                emotion[emo_char],
                                valence[emo_char],
                                LANG,
                                LANG2,
                                f"{DATASET}+{speaker_id}",
                                speaker_gender,
                                f"{DATASET}\n",
                            ]
                        )
                    )
if bad_files:
    print(f"{len(bad_files)} bad files:")
    for bad in bad_files:
        print(bad)

print("done")
