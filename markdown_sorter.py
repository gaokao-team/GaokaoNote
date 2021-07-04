import re
import os
import glob

"""###### tags: `Politics`"""

reg = re.compile(r"###### tags:.*`(.+?)`")
for file in glob.glob("*.md"):
    if file == "_sidebar.md" or file == "README.md":
        continue
    try:
        f = open(file, "r")
        tag = reg.search(f.read()).group(1)
        if not os.path.isdir(tag):
            os.mkdir(tag)
        os.rename(file, tag + os.sep + file)
    except Exception:
        print("Error: " + file)
