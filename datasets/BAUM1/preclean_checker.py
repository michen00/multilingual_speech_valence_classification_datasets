# quick script to check preclean.tsv

from os.path import exists
from os import walk


preclean_contains = []
with open("preclean.tsv", "r", encoding="utf-8-sig") as f:
    for line in f:
        line = line.strip()
        if line:
            preclean_contains.append(line.split("\t", 1)[0] + ".mp4")

for file in preclean_contains:
    speaker_folder = file.split("_")[0].lower()
    if exists(f"BAUM1a_MP4_all/{speaker_folder}/{file}") or exists(
        f"BAUM1s_MP4 - All/{speaker_folder}/{file}"
    ):
        pass
    else:
        print(f"{speaker_folder}/{file}.mp4 doesn't exist!")

preclean_contains.append("")
preclean_contains = frozenset(sorted(preclean_contains))

actual_files = frozenset(
    sorted(
        [
            file if file[-3:] == "mp4" else ""
            for folder in {"BAUM1a_MP4_all", "BAUM1s_MP4 - All"}
            for _, _, files in walk(folder)
            for file in files
        ]
    )
)
unaccounted_files = sorted(actual_files - preclean_contains)
print(len(unaccounted_files), "files unaccounted for:")
for file in unaccounted_files:
    speaker = file.split("_")[0].lower()
    dne = True
    if exists(f"BAUM1a_MP4_all/{speaker}/{file}"):
        print(file, "exists in acted")
        dne = False
    if exists(f"BAUM1s_MP4 - All/{speaker}/{file}"):
        print(file, "exists in spon.")
        dne = False
    if dne:
        print(file, "doesn't exist?")
