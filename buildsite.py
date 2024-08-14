import os
import sys

cmds = ["poetry run jupyter-book build portfolio",
        "git add -A",
        "git commit -m ",
        "git push",
        "poetry run ghp-import -n -p -f portfolio/_build/html"]
cmds = [
        "git add -A",
        "git commit -m ",
        "git push"]
defmsg = '"updated portfolio site"'

for cmd in cmds:
    if "commit" in cmd:
        if len(sys.argv) > 1:
            defmsg = sys.argv[1]
        cmd = cmd+defmsg
    print(cmd)
    os.system(cmd)