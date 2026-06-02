import re

replacements = {
    'á': 'a', 'à': 'a', 'ā': 'a', 'ǎ': 'a',
    'é': 'e', 'è': 'e', 'ē': 'e', 'ě': 'e',
    'í': 'i', 'ì': 'i', 'ī': 'i', 'ǐ': 'i',
    'ó': 'o', 'ò': 'o', 'ō': 'o', 'ǒ': 'o',
    'ú': 'u', 'ù': 'u', 'ū': 'u', 'ǔ': 'u',
    'ǘ': 'u', 'ǖ': 'u', 'ǚ': 'u', 'ǜ': 'u',  # ü variants
}

with open("lesson2.py", "r", encoding="utf-8") as f:
    content = f.read()

for accented, plain in replacements.items():
    content = content.replace(accented, plain)

with open("lesson2.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Done!")