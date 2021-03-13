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

# recode
mapper = {"angry": "neg", "happy": "pos", "neutral": "neu", "sad": "neg"}
for filename in data.keys():
    scores = data[filename]
    # tally votes, get average rater valence, get intended valence
    record = {
        "pos": scores["1"] + scores["2"],
        "neu": scores["3"],
        "neg": scores["4"] + scores["5"],
        "avg": sum([int(key) * scores[key] for key in scores.keys()]) / 18,
        "act": mapper[filename.split("_")[2]],
    }
    # label by majority vote
    for _ in ("pos", "neu", "neg"):
        if record[_] > 9:
            record["lab"] = _
            record["labeled_by"] = "majority"
            break
    else:
        # label by average perceived valence where no majority
        if record["avg"] < 3:
            record["lab"] = "pos"
        elif record["avg"] > 3:
            record["lab"] = "neg"
        else:
            record["lab"] = "neu"
        record["labeled_by"] = "average"
    # note whether intended valence matches new valence recode
    record["intent_match"] = record["lab"] == record["act"]
    # assign record
    data[filename] = record

with open("data_retained.csv", "w") as f:
    # write headers
    f.write("filename, avg_val, labeled_by, valence_label\n")
    for key in sorted(data.keys()):
        record = data[key]
        if record["intent_match"]:
            f.write(
                ", ".join(
                    [key, str(record["avg"]), record["labeled_by"], record["lab"]]
                )
                + "\n"
            )
