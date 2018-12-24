from pathlib import Path
import os
import sys


fn=input("Location: ")

fn = sys.argv[1]
if os.path.exists(fn):
    print=(os.path.basename(fn))
