from os import listdir
import os
from os.path import isfile, join
import pandas as pd
import torch
from tqdm import tqdm
# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)

model.to('cuda');
model.eval();


mypath = ["../video1",
         "../video2"]

for m in range(len(mypath)):
    onlyfiles = [os.path.join(mypath[m], f) 
                    for f in listdir(mypath[m]) 
                    if isfile(join(mypath[m], f))]
    
    f = open("video{}.txt".format(m+1), "a+")
    
    results = model(onlyfiles[0])
    f.write(f'Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS per image at shape {tuple(results.s)}' %
                    results.t)

    df = results.pandas().xyxy[0]
    df["frame"] = 1

    for i in tqdm(range(1, len(onlyfiles))):
        results = model(onlyfiles[i])
        f.write(f'Speed: %.1fms pre-process, %.1fms inference, %.1fms NMS per image at shape {tuple(results.s)}' %
                    results.t)
        df2 = results.pandas().xyxy[0]
        df2["frame"] = i + 1
        df = pd.concat([df, df2], axis=0)
    f.close()
    df.to_csv("video{}.csv".format(m+1), encoding='utf-8')