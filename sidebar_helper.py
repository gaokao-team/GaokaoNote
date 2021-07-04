import os
import re
from collections import defaultdict


def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [int(text) if text.isdigit() else text for text in _nsre.split(s[0])]


filetree = defaultdict(list)
root = os.getcwd()

for subdir, dirs, files in os.walk(root):
    for name in files:
        if name.endswith(".md") == False:
            continue
        if(subdir == root):
            continue
        belong = os.path.relpath(subdir, root)
        f = open(subdir + os.sep + name, "r")
        line = f.readline()
        while line.startswith('#') is False:
            line = f.readline()
        filetree[belong].append((line[1:].strip(), belong + os.sep + name))
        f.close()

f = open("_sidebar.md", "w")

for sub in filetree:
    f.write("  - " + sub + "\n")
    filetree[sub].sort(key=natural_sort_key)
    for item in filetree[sub]:
        f.write("    - [" + item[0] + "](" + item[1].replace(" ","-") + ")\n")

f.close()
