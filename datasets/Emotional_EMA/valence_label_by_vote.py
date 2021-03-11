from scipy.stats import binom_test

with open("valence_scores_per_sample", "r") as f:
    lines = f.readlines()

# collect scores
data = dict()
for line in lines:
    line = line.strip()
    if len(line) > 1:
        lastkey = line
        data[lastkey] = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
    else:
        data[lastkey][line] += 1

# tally valence votes
maj_counter, match_counter, unmatch_counter = 0, 0, 0
mapper = {"angry": "neg", "happy": "pos", "neutral": "neu", "sad": "neg"}
for filename in data.keys():
    scores = data[filename]
    record = {
        "pos": scores["1"] + scores["2"],
        "neu": scores["3"],
        "neg": scores["4"] + scores["5"],
        "lab": None,
        "avg": sum([int(key) * scores[key] for key in scores.keys()]) / 18,
        "act": mapper[filename.split("_")[2]],
    }
    for _ in ("pos", "neu", "neg"):
        if record[_] > 9:
            record["lab"] = _
            maj_counter += 1
            break
    else:
        if record["avg"] < 3:
            record["lab"] = "pos"
        elif record["avg"] > 3:
            record["lab"] = "neg"
        else:
            record["lab"] = "neu"
    record["intent_match"] = record["lab"] == record["act"]
    if record["intent_match"]:
        match_counter += 1
    else:
        unmatch_counter += 1
    data[filename] = record

print("majority decision", maj_counter)
print("matched", match_counter)
print("unmatched", unmatch_counter)

# no_plurality contains the only score distributions (sorted) where no majority and no plurality is present
no_plurality = [
    [0, 9, 9],
    [2, 8, 8],
    [4, 7, 7],
    [6, 6, 6],
]
