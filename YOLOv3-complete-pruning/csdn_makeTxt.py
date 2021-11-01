import os
import random
trainval_percent = 0.1
train_percent = 0.9
xmlfilepath = 'D:\HZQ\jtrafficsigns\YOLOv3-complete-pruning\data/Annotations'
txtsavepath = 'D:\HZQ\jtrafficsigns\YOLOv3-complete-pruning\data/ImageSets'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
ftrainval = open('D:\HZQ\jtrafficsigns\YOLOv3-complete-pruning\data/ImageSets/trainval.txt', 'w')
ftest = open('D:\HZQ\jtrafficsigns\YOLOv3-complete-pruning\data/ImageSets/test.txt', 'w')
ftrain = open('D:\HZQ\jtrafficsigns\YOLOv3-complete-pruning\data/ImageSets/train.txt', 'w')
fval = open('D:\HZQ\jtrafficsigns\YOLOv3-complete-pruning\data/ImageSets/val.txt', 'w')
for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
