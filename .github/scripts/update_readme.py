# .github/scripts/update_readme.py

import os
import re

directories = ['easy', 'medium', 'hard']

counts = [len(os.listdir(dir)) for dir in directories]

with open('README.md', 'r') as file:
    readme = file.read()

for i, dir in enumerate(directories):
    readme = re.sub(fr'{dir}: (\d+)\/\d', fr'\1{counts[i]}', readme)

with open('README.md', 'w') as file:
    file.write(readme)