from PIL import Image
import pandas as pd
import numpy as np
import os

file = pd.read_csv('2012_2019_PlatteRiverWeir_features_merged_all.csv')
url = file[' Filename']
urlArray = []

for i in url:
    urlArray.append(f'./images/{i}')

ulrArr = np.array(urlArray)

left = 100
right = 380
top = 150
bottom = 380


for i in range(len(ulrArr)):
    if os.path.exists(ulrArr[i]):
        im = Image.open(ulrArr[i])
        iml = im.crop((left, top, right, bottom))
        print(url[i])
        iml.save(f'./new/{url[i]}')

