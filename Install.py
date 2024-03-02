import subprocess
import os
import sys
print(os.popen("python3 Load.py").read())
try:
    subprocess.popen.__class__(f"python3 recursiveresearch.py {sys.argv[1]} {sys.argv[2]} {sys.argv[3]} {sys.argv[3]}")
except:
    print("installed")