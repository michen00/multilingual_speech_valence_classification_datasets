"""
This script writes the file paths, label, and other metadata of records to retain for model development in a tab-delimited csv.
The resultant tsv is used to help aggregate all records into a unified dataset.
Records are from the Estonian Emotional Speech Corpus (ekorpus).
"""

from os.path import exists


LANG = "est"  # ISO 639-3 Estonian
VALENCE = {"ang": "-1", "hap": "1", "neu": "0", "sad": "-1"}

missing_files = []
bad_files = []
missing_wav = []
intent_percept_mismatch = []

with open("perceived_valences", "r") as f1:
    with open("ekorpus_data_files.tsv", "w") as f2:
        for line in f1:
            sample_ID, perceived_valence = line.strip().split("\t")
            # capture intended emotions through TextGrid files
            # textgrid files for samples 213 and 120574 have special characters
            if sample_ID == "120574":
                intended_emotion = "neu"
            elif sample_ID == "213":
                intended_emotion = "hap"
            else:
                textgrid_file = f"{sample_ID}.TextGrid"
                try:
                    with open(textgrid_file, "r") as f3:
                        intended_emotion = (
                            f3.readlines()[-1].strip().split('"')[-2][:3]
                        )  # Small text files only
                    wavfile = f"{sample_ID}.wav"
                    if exists(wavfile):
                        if intended_emotion == "joy":
                            intended_emotion = "hap"
                        intended_valence = VALENCE[intended_emotion]
                        if intended_valence == perceived_valence:
                            f2.write(
                                "\t".join(
                                    [
                                        wavfile,
                                        intended_emotion,
                                        intended_valence,
                                        LANG,
                                        "f",
                                        "ekorpus\n",
                                    ]
                                )
                            )
                        else:
                            intent_percept_mismatch.append(sample_ID)
                    else:
                        missing_wav.append(wavfile)
                except FileNotFoundError:
                    missing_files.append(textgrid_file)
                except Exception as e:
                    bad_files.append(textgrid_file)


def print_if(filelist: list[str], bad_or_missing: str) -> None:
    """Print each missing or bad file if they exist."""
    if filelist:
        print(f"These files were {bad_or_missing}:")
        for file in filelist:
            print(file)
        print()


print_if(missing_files, "missing")
print_if(bad_files, "bad")
print_if(missing_wav, "missing")
print("intent-perception mismatch:")
print_if(intent_percept_mismatch, "bad")

print("done")
