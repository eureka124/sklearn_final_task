import os 
import numpy as np
import csv
from sklearn.utils import Bunch

def load_undergraduate_dataset():
    
    #声明样本数、特征数
    n_samples = 0
    n_features = 0
    
    #建立各个类别名的空数组
    all_feature_names = []
    Gender_class = []
    Province_class = []        
    Unavailable_class = []  
    Timefallasleep_class = []
    Healthstatus_class = []
    Hairloss_class = []
    Selfstudyplace_class = []
    Anxiousstatus_class = []
    Rank_class = []
    
    # 输出绝对路径
    classname_filepath = os.path.abspath('undergraduate_dataset_classname.csv')
    dataset_filepath = os.path.abspath('undergraduate_dataset.csv')
    
    #打开undergraduate_dataset_classname文件，读取样本数、特征数、类别型特征的具体分类
    with open('undergraduate_dataset_classname.csv',encoding='UTF-8-sig') as class_csv_file:
        
        class_file = csv.reader(class_csv_file)
        
        #读第1行，获得样本数量、特征数量
        temp = next(class_file)
        n_samples = int(temp[0])  #样本数量     
        n_features = int(temp[1]) #特征数量
        
        #读第2行，获得all_feature_names
        temp = next(class_file)
        for i in range(len(temp)):
            if(temp[i] != ''):
                all_feature_names.append(temp[i])
            
        #读第3行，获得Gender表示
        temp = next(class_file)
        for i in range(len(temp)):
            if(temp[i] != ''):
                Gender_class.append("[{0}]".format(i)+temp[i])
        
        #读第4行，获得Province表示
        temp = next(class_file)
        for i in range(len(temp)):
            if(temp[i] != ''):
                Province_class.append("[{0}]".format(i)+temp[i])
        
        #读第5行，获得Unavailable表示
        temp = next(class_file)
        for i in range(len(temp)):
            if(temp[i] != ''):
                Unavailable_class.append("[{0}]".format(i)+temp[i])
        
        #读第6行，获得Timefallasleep表示
        temp = next(class_file)
        for i in range(len(temp)):
            if(temp[i] != ''):
                Timefallasleep_class.append("[{0}]".format(i)+temp[i])
        
        #读第7行，获得Healthstatus表示
        temp = next(class_file)
        for i in range(len(temp)):
            if(temp[i] != ''):
                Healthstatus_class.append("[{0}]".format(i)+temp[i])
        
        #读第8行，获得Hairloss表示
        temp = next(class_file)
        for i in range(len(temp)):
            if(temp[i] != ''):
                Hairloss_class.append("[{0}]".format(i)+temp[i])
        
        #读第9行，获得Selfstudyplace表示
        temp = next(class_file)
        for i in range(len(temp)):
            if(temp[i] != ''):
                Selfstudyplace_class.append("[{0}]".format(i)+temp[i])
        
        #读第10行，获得Anxiousstatus表示
        temp = next(class_file)
        for i in range(len(temp)):
            if(temp[i] != ''):
                Anxiousstatus_class.append("[{0}]".format(i)+temp[i])
        
        #读第11行，获得Rank表示
        temp = next(class_file)
        for i in range(len(temp)):
            if(temp[i] != ''):
                Rank_class.append("[{0}]".format(i)+temp[i])
        
    #打开undergraduate_dataset，读取数据（对类别要转换成数值）
    with open('undergraduate_dataset.csv',encoding='UTF-8-sig') as data_csv_file:
        
        data_file = csv.reader(data_csv_file)

        #读第1行，获得all_features中文描述
        temp = next(data_file)
        all_feature_descr = []
        for i in range(len(temp)):
            if(temp[i] != ''):
                all_feature_descr.append(temp[i]) 

        #建立各列特征的空数组
        Year = np.empty((n_samples,),  dtype=np.float32)
        Gender = np.empty((n_samples,),  dtype=np.float32)
        Province = np.empty((n_samples,),  dtype=np.float32)
        Height = np.empty((n_samples,), dtype=np.float32)
        Weight = np.empty((n_samples,), dtype=np.float32)
        Unavailable = np.empty((n_samples,),  dtype=np.float32)
        Shortsight = np.empty((n_samples,),  dtype=np.float32)
        Dailymealexp = np.empty((n_samples,),  dtype=np.float32)
        Riceexp = np.empty((n_samples,),  dtype=np.float32)
        Monthlyexp = np.empty((n_samples,),  dtype=np.float32)
        Weeklytakeout = np.empty((n_samples,),  dtype=np.float32)
        Monthlyshopping = np.empty((n_samples,),  dtype=np.float32)
        Sleeptime = np.empty((n_samples,),  dtype=np.float32)
        Timefallasleep = np.empty((n_samples,),  dtype=np.float32)
        Dailyslidetime = np.empty((n_samples,),  dtype=np.float32)
        Dailygametime = np.empty((n_samples,),  dtype=np.float32)
        Dailysporttime = np.empty((n_samples,),  dtype=np.float32)
        Weeklyfamilyfreq = np.empty((n_samples,),  dtype=np.float32)
        Weeklyhairwash = np.empty((n_samples,),  dtype=np.float32)
        Healthstatus = np.empty((n_samples,),  dtype=np.float32)
        Hairloss = np.empty((n_samples,),  dtype=np.float32)
        Dailyselfstudy = np.empty((n_samples,),  dtype=np.float32)
        Selfstudyplace = np.empty((n_samples,),  dtype=np.float32)
        Lessoneffect = np.empty((n_samples,),  dtype=np.float32)
        Weelyworktime = np.empty((n_samples,),  dtype=np.float32)
        Anxiousstatus = np.empty((n_samples,),  dtype=np.float32)
        Rank = np.empty((n_samples,),  dtype=np.float32)

        #一行一行地遍历每i行数据，将对应数值填入数组
        for i, sample in enumerate(data_file):
            
            #需要同时打开classname，获得类别的具体分类
            with open('undergraduate_dataset_classname.csv',encoding='UTF-8-sig') as class_csv_file:
                
                class_file = csv.reader(class_csv_file)
                
                #从第0列遍历第i行，sample[col]即为第i行第col列点的数据
                col = 0

                # Year
                Year[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Gender
                temp = next(class_file)#跳过classname.csv中的样本数量行
                temp = next(class_file)#跳过classname.csv中的all_feature_names行
                temp = next(class_file)#来到classname.csv中的Gender_class行
                for j in range(len(temp)):
                    if(temp[j] != ''):
                        if(sample[col] == temp[j]):
                            Gender[i] = np.asarray(j, dtype=np.float32) 
                col+=1
                            
                # Province
                temp = next(class_file)
                for j in range(len(temp)):
                    if(temp[j] != ''):
                        if(sample[col] == temp[j]):
                            Province[i] = np.asarray(j, dtype=np.float32)
                col+=1

                # Height
                Height[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Weight
                Weight[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Unavailable
                temp = next(class_file)
                for j in range(len(temp)):
                    if(temp[j] != ''):
                        if(sample[col] == temp[j]):
                            Unavailable[i] = np.asarray(j, dtype=np.float32) 
                col+=1
                
                # Shortsight
                Shortsight[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Dailymealexp
                Dailymealexp[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Riceexp
                Riceexp[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Monthlyexp
                Monthlyexp[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Weeklytakeout
                Weeklytakeout[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Monthlyshopping
                Monthlyshopping[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Sleeptime
                Sleeptime[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Timefallasleep
                temp = next(class_file)
                for j in range(len(temp)):
                    if(temp[j] != ''):
                        if(sample[col] == temp[j]):
                            Timefallasleep[i] = np.asarray(j, dtype=np.float32) 
                col+=1
                
                # Dailyslidetime
                Dailyslidetime[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Dailygametime
                Dailygametime[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Dailysporttime
                Dailysporttime[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Weeklyfamilyfreq
                Weeklyfamilyfreq[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Weeklyhairwash
                Weeklyhairwash[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Healthstatus
                temp = next(class_file)
                for j in range(len(temp)):
                    if(temp[j] != ''):
                        if(sample[col] == temp[j]):
                            Healthstatus[i] = np.asarray(j, dtype=np.float32) 
                col+=1
                
                # Hairloss
                temp = next(class_file)
                for j in range(len(temp)):
                    if(temp[j] != ''):
                        if(sample[col] == temp[j]):
                            Hairloss[i] = np.asarray(j, dtype=np.float32) 
                col+=1
                
                # Dailyselfstudy
                Dailyselfstudy[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Selfstudyplace
                temp = next(class_file)
                for j in range(len(temp)):
                    if(temp[j] != ''):
                        if(sample[col] == temp[j]):
                            Selfstudyplace[i] = np.asarray(j, dtype=np.float32) 
                col+=1
                
                # Lessoneffect
                Lessoneffect[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Weelyworktime
                Weelyworktime[i] = np.asarray(sample[col], dtype=np.float32)
                col+=1
                
                # Anxiousstatus
                temp = next(class_file)
                for j in range(len(temp)):
                    if(temp[j] != ''):
                        if(sample[col] == temp[j]):
                            Anxiousstatus[i] = np.asarray(j, dtype=np.float32) 
                col+=1
                
                # Rank
                temp = next(class_file)
                for j in range(len(temp)):
                    if(temp[j] != ''):
                        if(sample[col] == temp[j]):
                            Rank[i] = np.asarray(j, dtype=np.float32)         
       
    dataset = Bunch(n_samples=n_samples, n_features=n_features, \
                classname_filepath=classname_filepath, dataset_filepath=dataset_filepath, \
                all_feature_descr=all_feature_descr, all_feature_names=all_feature_names, Gender_class=Gender_class, \
                Province_class=Province_class, Unavailable_class=Unavailable_class, \
                Timefallasleep_class=Timefallasleep_class, Healthstatus_class=Healthstatus_class,\
                Hairloss_class=Hairloss_class, Selfstudyplace_class=Selfstudyplace_class, \
                Anxiousstatus_class=Anxiousstatus_class, Rank_class=Rank_class, \
                Year=Year, Gender=Gender, Province=Province, Height=Height, Weight=Weight, Unavailable=Unavailable, \
                Shortsight=Shortsight, Dailymealexp=Dailymealexp, Riceexp=Riceexp, Monthlyexp=Monthlyexp, \
                Weeklytakeout=Weeklytakeout, Monthlyshopping=Monthlyshopping, Sleeptime=Sleeptime, \
                Timefallasleep=Timefallasleep, Dailyslidetime=Dailyslidetime, Dailygametime=Dailygametime, \
                Dailysporttime=Dailysporttime, Weeklyfamilyfreq=Weeklyfamilyfreq, Weeklyhairwash=Weeklyhairwash, \
                Healthstatus=Healthstatus, Hairloss=Hairloss, Dailyselfstudy=Dailyselfstudy, Selfstudyplace=Selfstudyplace, \
                Lessoneffect=Lessoneffect, Weelyworktime=Weelyworktime, Anxiousstatus=Anxiousstatus, Rank=Rank)
    
    return dataset