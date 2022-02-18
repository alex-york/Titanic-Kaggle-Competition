# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 10:48:47 2022

@author: asmod
"""

import pandas as pd
import matplotlib as plt


df_1 = pd.read_csv('C:/Users/asmod/Dropbox/Titanic ML project/train.csv')

df_1.insert(6,'Age_Bin_Q', pd.qcut(df_1['Age'],4,labels=False))
df_1.insert(6,'Age_Bin_E', pd.cut(df_1['Age'],4,labels=False))
df_1.insert(12,'Fare_Bin_Q', pd.cut(df_1['Fare'],4,labels=False))
df_1.insert(12,'Fare_Bin_E', pd.cut(df_1['Fare'],4,labels=False))
#Here we will insert new rows for binning our data next to our age row that is binned into 4 bins (0,1,2,3)
#Bin_Q is by quantiles (each bin has equal # of cases, Bin E has equal size bins)

df_1['Cabin_Letter']=df_1['Cabin'].str[:1] # I want to use the letters of cabins (assuming they represent decks or something)
df_1['Cabin_Letter']=df_1['Cabin_Letter'].fillna(value='Z')
df_1['C_L']= [ord(x) - 64 for x in df_1.Cabin_Letter]
df_1['C_L'].plot(kind='hist')
#df_1['Age'].plot(kind='hist')
#df_1['Age_Bin_Q'].plot(kind='hist')

#df_1['Fare'].plot(kind='hist')
#df_1['Fare_Bin_Q'].plot(kind='hist')

#%%
"""
Another option would be to creata  brand new data frame with the data we are interestd in and binned.
"""

#df_2 = pd.DataFrame()
#df_2['Survived'] = df_1['Survived']
#df_2['pclass'] = df_1['pclass']
#df_2['sex'] = df_1['sex']
#df_2['Age'] = pd.qcut(df_1['Age'],4, labels=False)


