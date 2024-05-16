# .github/scripts/update_readme.py

import os
import re

directories = ["easy", "medium", "hard"]

counts = [len(os.listdir(dir)) for dir in directories]

with open("README.md", "r") as file:
    readme = file.read()

for i, dir in enumerate(directories):
    readme = re.sub(rf"({dir}: )\d+(\/\d+)", rf"\g<1>{counts[i]}\g<2>", readme)

with open("README.md", "w") as file:
    file.write(readme)
