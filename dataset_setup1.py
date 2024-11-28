import os
import sys
import numpy as np
from sklearn.utils import Bunch
np.set_printoptions (suppress=True,threshold=sys.maxsize)
def load_undergraduate_dataset():
    class_name = []
    class_dict={}
    with open("undergraduate_dataset_classname.csv", 'r', encoding='utf-8-sig') as f:
        # 需使用utf-8-sig编码，否则会出现第一行出现['\ufeff114', '27']
        classname_lines = f.readlines()

        for line in classname_lines:
            line_list = list(filter(None, line.strip('\n').split(',')[:-1]))
            class_name.append(line_list)
        # print(class_name)
        column_name = class_name[1]
    for line in class_name[2:]:
        for i in range(0,len(line)):
            class_dict[line[i]] = i
    # print(class_dict)

    table=[]
    with open("undergraduate_dataset.csv", "r",encoding='utf-8-sig') as f:
        content=f.read().split("\n")
        # print(content)
        for line in content[1:]:
            table.append(line.split(","))
    # print(table)
    table=table[:-1]
    table=np.array(table)
    for i in range(len(table)):
        # print(len(table[i]))
        for j in range(len(table[i])):
            if table[i,j] in class_dict.keys():
                table[i,j]=class_dict[str(table[i,j])]
            else:
                try:
                    table[i,j]=float(table[i,j])
                except SyntaxError:
                    print(table[i,j])

    table=table.astype("float32")
    data_dict={}
    for i in range(len(column_name)):
        data_dict[column_name[i]]=table[:,i]
    dataset = Bunch(data_dict=data_dict)
    return dataset


if __name__ == '__main__':
    data_dict=load_undergraduate_dataset()
    print(data_dict)

