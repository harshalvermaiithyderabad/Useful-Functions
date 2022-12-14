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
