import os
import shutil

dir = "d:\\tempdir"

#os.makedirs()2bw
if os.path.exists(dir):
    shutil.rmtree(dir)
os.mkdir(dir)
print(os.name)
