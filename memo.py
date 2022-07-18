import os
import subprocess, sys

# The file is mainly tested to confirm the expected results.

ret = subprocess.run([
    "ls", 
    "Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed",
    "-a"
    ], capture_output=True)
print(ret.stdout)