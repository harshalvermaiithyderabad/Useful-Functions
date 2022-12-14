# solution 1 
def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    '''for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))''' # uncomment to get the inside of each directory
    return subfolders
  
  
# Solution 2 

for f in os.scandir('../dirname'):
    if f.is_dir() and  f.path != '../dirname/.ipynb_checkpoints':
        print(f.path)

# Solution 3
def list_of_sub_dir(dir_name):
    subfolder = []
    for f in os.scandir('../'+dir_name):
        if f.is_dir() and  f.path != '../'+ dir_name +'/.ipynb_checkpoints':
            subfolder.append(f.path)
            #print(subfolder)  
    return subfolder


'''
 comaprison of various methods for tracing the files in a system
'''        
        

import time
import os
from glob import glob
from pathlib import Path


directory = r"<insert_folder>"
RUNS = 1


def run_os_walk():
    a = time.time_ns()
    for i in range(RUNS):
        fu = [x[0] for x in os.walk(directory)]
    print(f"os.walk\t\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. Found dirs: {len(fu)}")


def run_glob():
    a = time.time_ns()
    for i in range(RUNS):
        fu = glob(directory + "/*/")
    print(f"glob.glob\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. Found dirs: {len(fu)}")


def run_pathlib_iterdir():
    a = time.time_ns()
    for i in range(RUNS):
        dirname = Path(directory)
        fu = [f for f in dirname.iterdir() if f.is_dir()]
    print(f"pathlib.iterdir\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. Found dirs: {len(fu)}")


def run_os_listdir():
    a = time.time_ns()
    for i in range(RUNS):
        dirname = Path(directory)
        fu = [os.path.join(directory, o) for o in os.listdir(directory) if os.path.isdir(os.path.join(directory, o))]
    print(f"os.listdir\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms. Found dirs: {len(fu)}")


def run_os_scandir():
    a = time.time_ns()
    for i in range(RUNS):
        fu = [f.path for f in os.scandir(directory) if f.is_dir()]
    print(f"os.scandir\t\ttook {(time.time_ns() - a) / 1000 / 1000 / RUNS:.0f} ms.\tFound dirs: {len(fu)}")


if __name__ == '__main__':
    run_os_scandir()
    run_os_walk()
    run_glob()
    run_pathlib_iterdir()
    run_os_listdir()
    
    
'''

RESULTS
     
os.scandir      took   1 ms. Found dirs: 439
os.walk         took 463 ms. Found dirs: 441 -> it found the nested one + base folder.
glob.glob       took  20 ms. Found dirs: 439
pathlib.iterdir took  18 ms. Found dirs: 439
os.listdir      took  18 ms. Found dirs: 439 '''
    
 
