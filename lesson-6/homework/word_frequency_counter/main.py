from pathlib import Path
import os

current_dir = Path(__file__).resolve().parent

sample = current_dir / "sample.txt"

if not os.path.isfile(sample):
    with open(sample, 'w') as f:
        txt = input("Input a paragraph for the text: \n")
        f.write(txt)
    print("File has been created with the your paragraph!")

from collections import defaultdict

txt = ""
with open(sample, 'r') as f:
    txt = f.read()

counter = defaultdict(int)

word = ""
total_words = 0
for i in txt:
    if not i.isalpha():
        if len(word):
            counter[word.lower()] += 1
            total_words += 1
        word = ""
    else:
        word += i


lst = [(cnt, w) for w, cnt in counter.items()]

lst.sort(reverse=True)

res = f"Word Count Report\nTotal number of words: {total_words}\n"
res += "Top words:\n"

for i in range(min(len(lst), 5)):
    res += f"{lst[i][1]} ({lst[i][0]} times)\n"

report = current_dir / "word_count_report.txt"
print(res)
with open(report, 'w') as f:
    f.write(res)