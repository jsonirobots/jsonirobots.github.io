# use by running: python buildsite.py
# for custom commit message, run: python buildsite.py "some message"
import os
import sys

cmds = ["poetry run jupyter-book build portfolio",
        "git add -A",
        "git commit -m",
        "git push",
        "poetry run ghp-import -n -p -f portfolio/_build/html"]
commsg = 'updated portfolio site'

for cmd in cmds:
    if "commit" in cmd:
        if len(sys.argv) > 1:
            commsg = sys.argv[1]
        cmd = f'{cmd} "{commsg}"'
    os.system(cmd)