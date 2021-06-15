import subprocess
from glob import glob

f = open("./merge.txt", "w")
for file in sorted(glob('../source/*.ts')):
    f.write("file '{}'".format(file) + "\n")
f.close()

subprocess.run(['./ffmpeg','-f','concat', '-safe', '0', '-i', 'merge.txt', '-c', 'copy', 'output.mp4'])