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



def tqdm_func():
    speeds = [int(x) for x in input("Enter all progress finishing time (in seconds and seperated by a ',', for exmp. 12,44,13):\n").split(",")]
    smooth = input("Do you want to the bars to run smootly or more cryomplhy? [y or n]:\n") == "y"
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
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    messages = input("Enter messager for each bar (seperated by a colin for exmp. Loading..., Finished!):\n").split(",")
    spinner = Halo(text=messages[0], spinner='dots')
    for x in messages:
        spinner.start(x)
        time.sleep(1)
        spinner.succeed()



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
