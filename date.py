#https://github.com/Aysel-Ahmadi/DATE-extraction.git
 


import re

text = input()

pattern = r'(?<!\d)(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})(?!\d)'

dates = re.finditer(pattern, text)

result = []

for match in dates:
    date = match.group()

    if '-' in date:
        year, month, day = date.split('-')
    else:
        day, month, year = date.split('/')

    if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
        result.append(f"{year}-{month}-{day}")

if result:
    print('\n'.join(result))
else:
    print("None")