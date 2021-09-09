"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Multimodal EmotionLines Dataset.
"""

from yaml import safe_load, YAMLError
from collections import namedtuple
from os import walk
from os.path import exists

LANG = "eng"  # ISO 639-3 English
LANG2 = "en-us"  # ISO 639-1 English + ISO 3166-1 United States
DATASET = "MELD"

with open("datasets.yaml", "r", encoding="utf-8-sig") as stream:
    try:
        datasets = safe_load(stream)
    except YAMLError as exc:
        print(exc)

Record = namedtuple(
    "Record",
    ["emo", "valence", "speaker_id", "speaker_gender", "expected_file"],
    defaults=None,
)
problemRecord = namedtuple("problemRecord", "record problem_type")

prefix = "MELD.Raw/"
split_path = {
    "dev": f"{prefix}dev_splits_complete/",
    "test": f"{prefix}test/output_repeated_splits_test/",
    "train": f"{prefix}train/train_splits/",
}

valid_emos = {"ang", "dis", "fea", "hap", "neu", "sad", "sur"}
emo_valence = dict.fromkeys(valid_emos, "-1")
emo_valence["hap"], emo_valence["neu"] = "1", "0"
valence_map = {"positive": "1", "negative": "-1", "neutral": "0"}

# file contains info copied and pasted from speaker_gender.xlsx
with open("speaker_genders", "r") as f:
    speaker_genders = {line.split("\t")[0]: line.strip()[-1] for line in f}

datasets_records = {}
problem_records = {}

speaker_merge = {
    "Dr. Leedbetter": "Dr. Ledbetter",
    "A Waiter": "The Waiter",
    "Paleontologist": "Professore Clerk",
    "Ross and Joey": "Joey and Ross",
    "Both": "Joey and Chandler",
    "Phoebe Sr": "Phoebe Sr.",
    "Rachel and Phoebe": "Phoebe and Rachel",
}

full_filepath: str = lambda split, file_name: "{}{}.mp4".format(
    split_path[split], file_name
)

unique_speakers = set()
all_count = 0
for split in datasets:
    split_folder = datasets[split]
    for key in split_folder:
        raw_record = split_folder[key]
        speaker, season = raw_record["Speaker"], raw_record["Season"]
        speaker_gender = ""
        if speaker in {
            "All",
            "Customer",
            "Girl",
            "Guy",
            "Man",
            "The Director",
            "The Interviewer",
        }:
            episode = raw_record["Episode"]
            if speaker == "The Director":
                if season == "7" and episode == "24":
                    episode = "23"
                elif season == "3" and episode == "22":
                    episode = "19"
            speaker = f"{speaker}{season}.{episode}"
            if speaker == "All":
                speaker = f"{speaker}.{all_count}"
                all_count += 1
        elif speaker in {
            "Dr. Oberman",
            "Director",
            "Flight Attendant",
            "Nurse",
            "Receptionist",
            "Student",
            "The Casting Director",
        }:
            speaker += season
        speaker = speaker_merge.get(speaker, speaker)
        unique_speakers.add(speaker)
        file_path = full_filepath(split, key)
        expected_file = (
            f"dia{raw_record['Dialogue_ID']}_utt{raw_record['Utterance_ID']}"
        )
        emo = raw_record["Emotion"][:3]
        emo = "hap" if emo == "joy" else emo
        valence = valence_map[raw_record["Sentiment"]]
        problem = []

        if file_path in datasets_records.keys():
            problem.append(("extant record overwrwitten", datasets_records[file_path]))
        datasets_records[file_path] = Record(
            emo=emo,
            valence=valence,
            speaker_id=speaker,
            speaker_gender=speaker_genders.get(speaker, "u"),
            expected_file=expected_file,
        )

        if key != expected_file:
            problem.append("unexpected file name")
        if not exists(file_path):
            problem.append("file does not exist?")
        if emo not in valid_emos:
            problem.append("invalid emotion")
        if emo != "sur" and emo_valence[emo] != valence:
            problem.append("emo-valence mismatch")
        if problem:
            problem_records[file_path] = problemRecord(
                record=datasets_records[file_path],
                problem_type=problem,
            )

if problem_records:
    print(problem_records)
else:
    print("no problems so far...")

actual_files = set()
for split in split_path:
    for root, _, files in walk(split_path[split]):
        for file_ in files:
            if file_[0] in {".", "f"} or file_.split(".")[-1] != "mp4":
                continue
            actual_files.add(f"{root}{file_}")

# test/dia93_utt9 and test/dia93_utt10 specifically discarded
# train/dia503_utt10 is low quality
# train/dia503_utt10 is mis-annotated
# test/dia108_utt1&2 are identical and mis-annotated
# some are removed for duplication
baddev = {"dia49_utt5", "dia66_utt9", "dia66_utt10"}
badtest = {
    "dia27_utt0",
    "dia27_utt1",
    "dia71_utt1",
    "dia93_utt5",
    "dia93_utt6",
    "dia93_utt7",
    "dia108_utt1",
    "dia108_utt2",
}
badtrain = {"dia4_utt1", "dia503_utt10", "dia715_utt0"}

# Manually address specific problems observed
for split, file_list in zip(sorted(split_path.keys()), (baddev, badtest, badtrain)):
    for file_ in file_list:
        try:
            actual_files.remove(full_filepath(split, file_))
        except KeyError:
            print(f"failed to remove {file_} from {split} of actual_files")

# test/dia93_utt4 manually recoded: emotion ang, sentiment negative, speaker Joey
datasets_records[full_filepath("test", "dia93_utt4")] = Record(
    emo="ang",
    valence="-1",
    speaker_id="Joey",
    speaker_gender="m",
    expected_file="dia93_utt4",
)
datasets_records[full_filepath("dev", "dia49_utt4")] = Record(
    emo="ang",
    valence="-1",
    speaker_id="Ross and Susan",
    speaker_gender="u",
    expected_file="dia49_utt4",
)

files_unaccounted = actual_files - set(datasets_records.keys())
print(f"{len(datasets_records)} in datasets.yaml")
print(f"{len(actual_files)} actual files")
print(f"{len(files_unaccounted)} actual files unaccounted for")
print(f"{len(unique_speakers)} unique speakers")

if files_unaccounted:
    [print(_) for _ in files_unaccounted]
else:
    with open("MELD_data_files.tsv", "w") as f:
        for file_ in actual_files:
            record = datasets_records[file_]
            f.write(
                "\t".join(
                    [
                        file_,
                        record.emo,
                        record.valence,
                        LANG,
                        LANG2,
                        f"{DATASET}+{record.speaker_id}",
                        record.speaker_gender,
                        f"{DATASET}\n",
                    ]
                )
            )
print("done")
