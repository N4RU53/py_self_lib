import glob
import os

direc_path = "./content/"
output_name = "list.txt"
mode='name'

def ftnl(path=direc_path, fname=output_name, mode=mode):

    files = glob.glob(path + "*")
    with open(fname, 'a', encoding="utf-8") as f:
        for file in files:
            if mode == 'name':
                f.write(os.path.split(file)[1] + "\n")
            elif mode == 'all':
                f.write(file.replace('\\', '/') + "\n")

ftnl()