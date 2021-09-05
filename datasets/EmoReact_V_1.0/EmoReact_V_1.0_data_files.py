"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the EmoReact dataset.
"""

from collections import namedtuple

LANG = "eng"  # ISO 639-3 English
LANG2 = "en"  # ISO 639-1 English
DATASET = "EmoReact_V_1.0"

# Speaker is adult interviewer, not child subject
# or there is no vocal utterance
manually_omit = {
    "VCR107_2.mp4",
    "BULLYING27_2.mp4",
    "GAMEBOY19_2.mp4",
    "GAMEBOY29_2.mp4",
    "KIMCHI65_2.mp4",
    "OLDCOMPUTERS128_2.mp4",
    "REBECCA13_2.mp4",
    "TYPEWRITERS19_2.mp4",
    "TYPEWRITERS28_2.mp4",
}

rating_vector = namedtuple(
    "RatingVector",
    [
        "curiosity",
        "uncertainty",
        "excitement",
        "happiness",
        "surprise",
        "disgust",
        "fear",
        "frustration",
    ],
)


def fuzzy_emotion_vote(ratings) -> tuple[str, str]:
    """Return a fuzzy emotion vote from a ratings vector."""

    emotions = {
        "cur": ratings.curiosity,
        "exc": ratings.excitement,
        "hap": ratings.happiness,
        "unc": ratings.uncertainty,
        "sur": ratings.surprise,
        "dis": ratings.disgust,
        "fea": ratings.fear,
        "fru": ratings.frustration,
    }

    any_negative = any(  # negative emotions
        {
            emotions["unc"],
            emotions["sur"],
            emotions["dis"],
            emotions["fea"],
            emotions["fru"],
        }
    )

    if any({emotions["cur"], emotions["exc"], emotions["hap"]}):  # positive emotions
        if any_negative:
            valence = ""
        else:
            valence = "1"
    else:
        if any_negative:
            valence = "-1"
        else:
            # all ratings are 0
            return "neu", "0"

    if sum(ratings) > 1:
        emotion = "unk"
    else:
        for key in emotions.keys():
            if emotions[key]:
                emotion = key
                break

    return emotion, valence


valence_from_float = lambda x: "-1" if x < 4 else "1" if x > 4 else "0"
strip_split = lambda x, c: x.strip().split(c)

with open("EmoReact_V_1.0_data_files.tsv", "w") as f1:
    for split in {"train", "val", "test"}:
        # The *2.txt files include manual speaker gender annotations
        with open(f"{split}_names2.txt", "r") as f2:
            with open(f"Labels/{split}_labels.text", "r") as f3:
                for filename_gender, votes in zip(f2, f3):
                    # manual annotations: filename*gender
                    speaker_number, file, gender = strip_split(filename_gender, "*")
                    ratings = [float(_) for _ in strip_split(votes, ",")]
                    perceived_valence = valence_from_float(ratings.pop(-1))
                    (
                        perceived_emotion,
                        valence_of_perceived_emotion,
                    ) = fuzzy_emotion_vote(rating_vector(*ratings))
                    keep = False
                    if perceived_emotion == "unk":
                        keep = bool(int(perceived_valence))
                    elif valence_of_perceived_emotion == perceived_valence:
                        keep = True
                    if file in manually_omit:
                        keep = False
                    if keep:
                        f1.write(
                            "\t".join(
                                [
                                    f"Data/{split}/{file}",
                                    perceived_emotion,
                                    perceived_valence,
                                    LANG,
                                    LANG2,
                                    f"{DATASET}+{split}{speaker_number}",
                                    gender,
                                    f"{DATASET}\n",
                                ]
                            )
                        )
print("done")
