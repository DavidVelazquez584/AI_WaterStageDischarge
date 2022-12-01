from os import listdir
import os
from os.path import isfile, join

url = './images/Validation'

onlyfiles = [f for f in listdir(url) if isfile(join(url, f))]


for file in onlyfiles:
    a = file.split(' ')
    if len(a) > 1:
        os.remove(url + '/' + file)
