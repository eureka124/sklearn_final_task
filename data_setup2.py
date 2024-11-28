import pandas as pd
import numpy as np

class_name=[]
with open("undergraduate_dataset_classname.csv",'r',encoding='utf-8-sig') as f:
    #需使用utf-8-sig编码，否则会出现第一行出现['\ufeff114', '27']
    classname_lines=f.readlines()
    
    for line in classname_lines:
        line_list=list(filter(None, line.strip('\n').split(',')[:-1]))
        class_name.append(line_list)
    print(class_name)
    column_name=class_name[1]

data=pd.read_csv('undergraduate_dataset.csv',header=0)

class_name_dict={}
for i in range(2,len(class_name)):
    for j in range(len(class_name[i])):
        class_name_dict[class_name[i][j]] = j
print(class_name_dict)