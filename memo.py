import os
import subprocess, sys

# The file is mainly tested to confirm the expected results.

os.chdir("Functional_SpecConfirmance_Arguments_Single_WhichFilesAreListed")
ret = subprocess.run([
    "ls", "--hide=*.a"
    ], capture_output=True)
print(ret.stdout)