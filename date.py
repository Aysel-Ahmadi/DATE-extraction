#https://github.com/Aysel-Ahmadi/DATE-extraction.git
 

import re

text = input()

year = r"([0-9]{4})"

month = r"(0[1-9]|1[0-2])"

day = r"(0[1-9]|[12][0-9]|3[01])"

pattern = rf"(?<![0-9])({year}-{month}-{day}|{day}/{month}/{year})(?![0-9])"

matches = re.finditer(pattern, text)

dates = []

for match in matches:
 date = match.group()

if "/" in date:
    d, m, y = date.split("/")
    date = f"{y}-{m}-{d}"
dates.append(date)

if dates:
  for date in dates:
   print(date)
  else:
    print("None")