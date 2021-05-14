"""
Records are from the Arabic Natural Audio Dataset.
Unfortunately, the emotion labels for this dataset are not at the utterance level.
"""

from os import name
import pandas as pd

name_emo = {"name": "path", "Emotion ": "emo"}  # sic

data = pd.read_csv("ANAD.csv", header=0)[name_emo].rename(columns=name_emo)
data.path = data.path.str.split(pat=" ", n=1).apply(lambda x: x[0])
temp_index = data.value_counts().index
get_series = (
    lambda x, y: temp_index.get_level_values(x).to_series(name=y).reset_index(drop=True)
)
data = pd.concat([get_series(0, "path"), get_series(1, "emo")], axis=1)
print(data)
data2 = data
data2.path = data2.path.str.slice(0,2)
print(data2.value_counts())
