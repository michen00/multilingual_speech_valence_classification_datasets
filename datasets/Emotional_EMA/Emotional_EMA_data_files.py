"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Electromagnetic Articulography Database.
"""

from typing import OrderedDict, TextIO

LANG = "eng"  # ISO 639-3 English
LANG2 = "en-us"  # ISO 639-1 English + ISO 3166-1 United States
DATASET = "Emotional_EMA"

# Collect valence votes of each file
valence_votes = {}
with open("valence_scores_per_sample", "r") as f:
    for line in f:
        line = line.strip()
        if len(line) > 1:
            lastkey = line
            valence_votes[lastkey] = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
        else:
            valence_votes[lastkey][line] += 1

VALENCE = OrderedDict(
    {"hap": "1", "ang": "-1", "sad": "-1", "neu": "0", "unk": ""}
)  # Gets valence of an emotion
emotion_vote = dict(zip(range(0, 5), VALENCE.keys()))  # Gets an emotion by index


def emotion_voter(*args: int) -> str:
    """Return which emotion received a majority vote."""
    majority_threshold = sum(args) / 2
    counter = 0
    for num_votes in args:
        if num_votes > majority_threshold:
            return emotion_vote[counter]
        counter += 1
    return "unk"


intended_emotion_of_file = lambda file: file.split("_", 2)[-1][:3]
bad_records = []  # Stores discarded


def process_file(filename: str, f_write: TextIO) -> None:
    """Attempts to write a line to f_write if intended valence matches perceived or appends to bad_records otherwise."""
    intended_emotion = intended_emotion_of_file(filename)
    intended_valence = VALENCE[intended_emotion]

    votes = valence_votes[filename]

    for valence, vote in {
        "-1": votes["1"] + votes["2"],
        "0": votes["3"],
        "1": votes["4"] + votes["5"],
    }.items():
        if vote > sum(votes.values()) / 2:
            majority_valence = valence
            break
    else:
        majority_valence = False

    average = sum([int(score) * number for score, number in votes.items()]) / sum(
        votes.values()
    )
    average_valence = "-1" if average > 3 else "1" if average < 3 else "0"

    if intended_valence == majority_valence or intended_valence == average_valence:
        f_write.write(
            "\t".join(
                [
                    f"{filename.split(f'_', 2)[1]}/Wavfiles/{filename}",
                    intended_emotion,
                    intended_valence,
                    LANG,
                    LANG2,
                    f"{DATASET}+{speaker}",
                    SPEAKER_GENDER[speaker],
                    f"{DATASET}\n",
                ]
            )
        )
    else:
        bad_records.append(filename)


SPEAKER_GENDER = {"abe": "m", "joy": "f", "lau": "f"}

best_speaker_files = []
with open("Emotional_EMA_data_files.tsv", "w") as f_write:
    for speaker in SPEAKER_GENDER.keys():
        with open(f"HumanEval/best_{speaker}_files.txt", "r") as f_read:
            if speaker == "lau":
                f_read.readline()  # Skips the header only present in this file
            for line in f_read:
                line = line.strip().split("\t")
                filename = (
                    f"{line.pop(0)}.wav" if speaker == "joy" else line.pop(0)
                )  # best_joy_files.txt doesn't have .wav in the file name
                best_speaker_files.append(filename)
                intended_emotion = intended_emotion_of_file(filename)
                voted_emotion = emotion_voter(*[int(_) for _ in line])
                if intended_emotion == voted_emotion:
                    # write_emotion = intended_emotion
                    pass
                else:
                    # All of them match, incidentally, so this block was never run
                    # That also means there were no "unk" votes, so that condition isn't checked later
                    input("Hey! Intended emotion does not match voted emotion.")
                process_file(filename, f_write)

    # Not all files in valence_scores_per_sample appear in the best_{speaker}_files.txt files.
    for file in set(valence_votes.keys()) - set(best_speaker_files):
        # Process files without categorical emotion votes (valence only)
        process_file(file, f_write)

print("Discarded", len(bad_records))
for record in bad_records:
    print(record)
print("done")
