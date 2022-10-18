from __future__ import unicode_literals
from multiprocessing import Process
from tqdm import *
from alive_progress import *
from halo import Halo
from yaspin import yaspin
from yaspin.spinners import Spinners
import random
import os
import sys
import time


# Things to do : Nested loops, stop at 99% (at own made bar), variyng (speed differs)!!!!!!!!!!!!!!!!

def tqdm_func():
    barCunt = int(input("Enter amount of progress bars:\n"))
    if barCunt > 1:
        speeds = input("Enter all progress finishing time (in seconds and seperated by a ',', for exmp. 12,44,13):\n")
    else:
        speeds = input("Enter finishing time (in seconds):\n")
    speeds = [int(x) for x in speeds.split(",")]
    smooth = input("Do you want to the bars to run smootly or more cryomplhy? [y or n]:\n")
    smooth = "y" == smooth
    blocks = int(input("In how many chonks do you want the progress bars be?:\n"))
    if smooth:
        for x in range(len(speeds)):
            for y in tqdm(range(blocks)):
                time.sleep(speeds[x] / blocks)
    else:
        differing = int(input("Enter differing scale [1-10]:\n"))
        for x in range(len(speeds)):
            total_time = speeds[x]
            for y in tqdm(range(blocks)):
                if y != 99:
                    t = speeds[x] / blocks * (1 + 0.1 * random.randint(-differing, differing))
                    if total_time - t > 0:
                        total_time -= t
                        time.sleep(t)

                else:
                    time.sleep(total_time)



def halo_func():
    print("gay")

def yaspin_func():
    print("2gays")

def alive_func():
    print("3gays")

def bash_func():
    print("4gays")

def progress_func():
    print("5gays")

def showtime_func():
    print("6gays")

print("Progress bars:\n0:tqdm\n1:halo\n2:yaspin\n3:alive_progress\n4:bash\n5:progress\n6:showtime(alive_progress)")
bars = ["tqdm", "halo", "yaspin", "alive", "bash", "progress", "showtime"]
bar = input("Enter progress bar (by number):\n")
numToFuncDic = {"0":"tqdm_func()", "1":"halo_func()", "2":"yaspin_func()", "3":"alive_func()", "4":"bash_func()", "5":"progress_func()", "6":"showtime_func()"}
eval(numToFuncDic[bar])
