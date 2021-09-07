"""
This script writes the file_ paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the EmoReact dataset.
"""

from typing import OrderedDict
from copy import deepcopy

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
positives = ("cur", "exc", "hap")
negatives = ("unc", "sur", "dis", "fea", "fru")
valence = OrderedDict(
    {**dict.fromkeys(positives, "1"), **dict.fromkeys(negatives, "-1")}
)
valence_group = {positives: "1", negatives: "-1"}
valence["neu"] = "0"

valence_from_float: str = lambda x: "-1" if x < 4 else "1" if x > 4 else "0"
strip_split: tuple[str, str, str] = lambda x, c: x.strip().split(c)

sub_emo_tally: dict[str, float] = lambda tallies, emolist: OrderedDict(
    {emo: tallies[emo] for emo in emolist}
)


def count_tallies(ratings: list[float]) -> tuple[dict[str, float], dict[str, float]]:
    "Count votes for positive and negative emotions."
    emo_tally = dict(
        zip(
            ("cur", "exc", "hap", "unc", "sur", "dis", "fea", "fru"),
            ratings,
        )
    )
    return sub_emo_tally(emo_tally, positives), sub_emo_tally(emo_tally, negatives)


any_val: bool = lambda tally: any(tally.values())


def fuzzy_vote(
    valence_tally: dict[str, float], perceived_valence: str
) -> tuple[str, str]:
    """Recode perceived emotion and valence."""
    emotions_list = tuple(valence_tally.keys())
    val = valence_group[emotions_list]
    if sum(valence_tally.values()) > 1:
        # multiple votes for emotions of same valence
        perceived_emotion = val
    else:
        # voted emotion is unambiguous
        for valenced_emo in emotions_list:
            if valence_tally[valenced_emo]:
                perceived_emotion = valenced_emo
                break
    # perceived emotions color 0 valence
    perceived_valence = val if perceived_valence == "0" else perceived_valence
    return perceived_emotion, perceived_valence


def copy_and_remove_key(mod_dict: dict[str, str], key: str) -> dict[str, str]:
    """Given a dictionary and a key, 1) copy the dictionary, 2) pop the key off the copy, and 3) return the copy."""
    new = deepcopy(mod_dict)
    new.pop(key)
    return new


not_written = []
with open("EmoReact_V_1.0_data_files.tsv", "w") as f1:
    for split in {"train", "val", "test"}:
        # The *2.txt files include manual speaker gender annotations
        with open(f"{split}_names2.txt", "r") as f2:
            with open(f"Labels/{split}_labels.text", "r") as f3:
                for filename_gender, votes in zip(f2, f3):
                    # manual annotations: set_speaker*file_name*gender
                    speaker_number, file_, gender = strip_split(filename_gender, "*")
                    if file_ in manually_omit:
                        continue
                    ratings = [float(_) for _ in strip_split(votes, ",")]
                    # perceived_valence should always be "1", "0", or "-1"
                    perceived_valence: str = valence_from_float(ratings.pop(-1))
                    pos_tally, neg_tally = count_tallies(ratings)
                    any_positive, any_negative = any_val(pos_tally), any_val(neg_tally)
                    if any_positive:
                        if any_negative:
                            # There are votes for negative and positive emotions
                            perceived_emotion = "unk"
                        else:
                            # votes for positive but not negative emotions
                            perceived_emotion, perceived_valence = fuzzy_vote(
                                pos_tally, perceived_valence
                            )
                    elif any_negative:
                        # votes for negative but not positive emotions
                        perceived_emotion, perceived_valence = fuzzy_vote(
                            neg_tally, perceived_valence
                        )
                    elif int(perceived_valence):
                        # all ratings are 0 and perceived_valence is non-zero
                        perceived_emotion = perceived_valence
                    else:
                        # all ratings are 0 and perceived_valence is zero
                        perceived_emotion = "neu"

                    # write record if valence of perceived emotion is ambiguous or valence matches
                    if perceived_emotion in {
                        "cur",
                        "sur",
                        "unk",
                        "1",
                        "-1",
                    } or perceived_valence == valence.get(
                        perceived_emotion, perceived_emotion
                    ):
                        perceived_emotion = (
                            "unk"
                            if perceived_emotion in {"1", "-1"}
                            else perceived_emotion
                        )
                        # final disambiguation of "unk", "0"
                        if (perceived_emotion, perceived_valence) == ("unk", "0"):
                            # re-color valence after dropping ambiguous emotions
                            any_pos = any_val(copy_and_remove_key(pos_tally, "cur"))
                            any_neg = any_val(copy_and_remove_key(neg_tally, "sur"))
                            if any_pos:
                                if any_neg:
                                    # reject emo votes with incompatible valences + 0 perceived_valence
                                    not_written.append(
                                        (
                                            file_,
                                            perceived_emotion,
                                            perceived_valence,
                                            pos_tally,
                                            neg_tally,
                                        )
                                    )
                                    continue
                                else:
                                    perceived_valence = "1"
                            elif any_neg:
                                perceived_valence = "-1"
                            else:
                                print(
                                    f"correctly captured 'unk', '0' for {split}/{file_}"
                                )
                        f1.write(
                            "\t".join(
                                [
                                    f"Data/{split}/{file_}",
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
                    else:
                        not_written.append(
                            (
                                file_,
                                perceived_emotion,
                                perceived_valence,
                                pos_tally,
                                neg_tally,
                            )
                        )

if not_written:
    print(f"{len(not_written)} files not written:")
for unwritten in not_written:
    print(
        "file: {}/{}, perceived emo: {}, perceived valence: {}\n{} {}".format(
            split, *unwritten
        )
    )

print("done")
