from __future__ import unicode_literals
from random import randint
import os
import sys
import time
import cursor
from tqdm import *
from alive_progress import *
from halo import Halo
from yaspin import yaspin
from yaspin.spinners import Spinners

cursor.hide()

def tqdm():
    print("nogay")

def halo():
    print("gay")

def yaspin():
    print("2gays")

def alive():
    print("3gays")

def bash():
    print("4gays")

def progress():
    print("5gays")    

def showtime():
    print("6gays")    

print("Progress bars:\n0:tqdm\n1:halo\n2:yaspin\n3:alive_progress\n4:bash\n5:progress\n6:showtime(alive_progress)")
bars = ["tqdm", "halo", "yaspin", "alive", "bash", "progress", "showtime"]
bar = input("Enter progress bar (by number):\n")

eval(f"{bars[int(bar)]}()")










