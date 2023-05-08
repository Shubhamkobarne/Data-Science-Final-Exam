# -*- coding: utf-8 -*-
"""Student Attendance Dashboard for Decision Making data science project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T34iVUVX3JPdR0nDtMCty-si9vqgftbi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('Batchwise Attendance Data - Class 1.csv')

data.head()

data.shape

data.isna().sum()

data2 = pd.read_csv('Batchwise Attendance Data - Class 2.csv')

data2.head()

data2.shape

data2.isna().sum()

data2['Type'].replace(['NaN'],'student')

data2['Type'] = data2['Type'].fillna('STUDENT')

data['Type'] = data['Type'].fillna('STUDENT')

data.isna().sum()

data2.isna().sum()

data2.drop(['01-01-21','R-01-01-21'],axis=1,inplace=True)

data2.isna().sum()

data2.head()

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='most_frequent')
new_data = imputer.fit_transform(data)

new_data

data = pd.DataFrame(new_data,columns = data.columns)

data.head()

imputer = SimpleImputer(strategy='most_frequent')
new_data2 = imputer.fit_transform(data2)

data2 = pd.DataFrame(new_data2,columns=data2.columns)

data2.head()

data.shape

data2.shape

data['Type'].unique(),data['10-01-21'].unique()

data.info()

data2.info()

data2['R-10-01-21'].unique()

# DATAFRAME FOR CLASS A

date_10 = data[['Student Roll Num','Type','10-01-21','R-10-01-21']]

date_9 = data[['Student Roll Num','Type','09-01-21','R-9-01-21']]

date_8 = data[['Student Roll Num','Type','08-01-21','R-8-01-21']]

date_7 = data[['Student Roll Num','Type','07-01-21','R-7-01-21']]

date_6 = data[['Student Roll Num','Type','06-01-21','R-6-01-21']]

date_5 = data[['Student Roll Num','Type','05-01-21','R-5-01-21']]

date_4 = data[['Student Roll Num','Type','04-01-21','R-4-01-21']]

date_3 = data[['Student Roll Num','Type','03-01-21','R-3-01-21']]

date_2 = data[['Student Roll Num','Type','02-01-21','R-02-01-21']]

date_1 = data[['Student Roll Num','Type','01-01-21','R-01-01-21']]

# DATAFRAME FOR CLASS B

clb_10 = data2[['Student Roll Num','Type','10-01-21','R-10-01-21']]

clb_9 = data2[['Student Roll Num','Type','09-01-21','R-9-01-21']]

clb_8 = data2[['Student Roll Num','Type','08-01-21','R-8-01-21']]

clb_7 = data2[['Student Roll Num','Type','07-01-21','R-7-01-21']]

clb_6 = data2[['Student Roll Num','Type','06-01-21','R-6-01-21']]

clb_5 = data2[['Student Roll Num','Type','05-01-21','R-5-01-21']]

clb_4 = data2[['Student Roll Num','Type','04-01-21','R-4-01-21']]

clb_3 = data2[['Student Roll Num','Type','03-01-21','R-3-01-21']]

import scipy.stats

rat = [5,6,7,8,9,10]
total_rat_cnt =[]
for r in rat:
    cnt =0
    rat_cnt = []
    for i in data.columns:
        if i[0] == 'R':
            for j in data[i]:
                if j == r:
                    cnt+=1
            rat_cnt.append(cnt)
    total_rat_cnt.append(sum(rat_cnt))
print(total_rat_cnt)

plt.bar(rat,total_rat_cnt)
plt.title('Total Rating From Different Days')
plt.show()

Total_Score = []
for i in data.columns:
    if i[0] == 'R':
        Total_Score.append(scipy.stats.mode(data[i]))
print(scipy.stats.mode(Total_Score))

# Rating and Visualisations for Specific Dates for class A
# These are all the students who gave 10 out of 10 rating for class A
plt.pie(date_10[date_10['R-10-01-21']>9]['Type'].value_counts(),labels=date_10[date_10['R-10-01-21']>9]['Type'].unique())
plt.show()
date_10[date_10['R-10-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type', kind='count', data=data, col='10-01-21')
plt.show()

sns.countplot(x='Type',
             hue='R-10-01-21',
             data=data)

plt.pie(date_9[date_9['R-9-01-21']>9]['Type'].value_counts(),labels=date_9[date_9['R-9-01-21']>9]['Type'].unique())
plt.show()
date_9[date_9['R-9-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type', col='09-01-21', kind='count', data=data)
plt.show()

sns.countplot(x='Type',
             hue='R-9-01-21',
             data=data)

plt.pie(date_8[date_8['R-8-01-21']>9]['Type'].value_counts(),labels=date_8[date_8['R-8-01-21']>9]['Type'].unique())
plt.show()
date_8[date_8['R-8-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='08-01-21',kind='count',data=data)
plt.show()

sns.countplot(x='Type',
             hue='R-8-01-21',
             data=data)

plt.pie(date_7[date_7['R-7-01-21']>9]['Type'].value_counts(),labels=date_7[date_7['R-7-01-21']>9]['Type'].unique())
plt.show()
date_7[date_7['R-7-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='07-01-21',kind='count',data=data)
plt.show()

sns.countplot(x='Type',
             hue='R-7-01-21',
             data=data)

plt.pie(date_6[date_6['R-6-01-21']>9]['Type'].value_counts(),labels=date_6[date_6['R-6-01-21']>9]['Type'].unique())
plt.show()
date_6[date_6['R-6-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='06-01-21',kind='count',data=data)
plt.show()

sns.countplot(x='Type',
             hue='R-6-01-21',
             data=data)

plt.pie(date_5[date_5['R-5-01-21']>9]['Type'].value_counts(),labels=date_5[date_5['R-5-01-21']>9]['Type'].unique())
plt.show()
date_5[date_5['R-5-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='05-01-21',kind='count',data=data)
plt.show()

sns.countplot(x='Type',
             hue='R-5-01-21',
             data=data)

plt.pie(date_4[date_4['R-4-01-21']>9]['Type'].value_counts(),labels=date_4[date_4['R-4-01-21']>9]['Type'].unique())
plt.show()
date_4[date_4['R-4-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='04-01-21',kind='count',data=data)
plt.show()

sns.countplot(x='Type',
             hue='R-4-01-21',
             data=data)

plt.pie(date_3[date_3['R-3-01-21']>9]['Type'].value_counts(),labels=date_3[date_3['R-3-01-21']>9]['Type'].unique())
plt.show()
date_3[date_3['R-3-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='03-01-21',kind='count',data=data)
plt.show()

sns.countplot(x='Type',
             hue='R-3-01-21',
             data=data)

plt.pie(date_2[date_2['R-02-01-21']>9]['Type'].value_counts(),labels=date_2[date_2['R-02-01-21']>9]['Type'].unique())
plt.show()
date_2[date_2['R-02-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='02-01-21',kind='count',data=data)
plt.show()

sns.countplot(x='Type',
             hue='R-02-01-21',
             data=data)

plt.pie(date_1[date_1['R-01-01-21']>9]['Type'].value_counts(),labels=date_1[date_1['R-01-01-21']>9]['Type'].unique())
plt.show()
date_1[date_1['R-01-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='01-01-21',kind='count',data=data)
plt.show()

sns.countplot(x='Type',
             hue='R-01-01-21',
             data=data)

Total_Score1 = []
for i in data2.columns:
    if i[0] == 'R':
        Total_Score1.append(scipy.stats.mode(data2[i]))
print(scipy.stats.mode(Total_Score1))

rat2 = [5,6,7,8,9,10]
total_rat2_cnt =[]
for r in rat2:
    cnt =0
    rat_cnt = []
    for i in data2.columns:
        if i[0] == 'R':
            for j in data2[i]:
                if j == r:
                    cnt+=1
            rat_cnt.append(cnt)
    total_rat2_cnt.append(sum(rat_cnt))
print(total_rat2_cnt)

plt.bar(rat2,total_rat2_cnt)
plt.title('Total Rating From Different Days')
plt.show()

plt.pie(clb_10[clb_10['R-10-01-21']>9]['Type'].value_counts(),labels=clb_10[clb_10['R-10-01-21']>9]['Type'].unique())
plt.show()
clb_10[clb_10['R-10-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='10-01-21',kind='count',data=data2)
plt.show()

sns.countplot(x='Type',
             hue='R-10-01-21',
             data=data2)

plt.pie(clb_9[clb_9['R-9-01-21']>9]['Type'].value_counts(),labels=clb_9[clb_9['R-9-01-21']>9]['Type'].unique())
plt.show()
clb_9[clb_9['R-9-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='09-01-21',kind='count',data=data2)
plt.show()

sns.countplot(x='Type',
             hue='R-9-01-21',
             data=data2)

plt.pie(clb_8[clb_8['R-8-01-21']>9]['Type'].value_counts(),labels=clb_8[clb_8['R-8-01-21']>9]['Type'].unique())
plt.show()
clb_8[clb_8['R-8-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='08-01-21',kind='count',data=data2)
plt.show()

sns.countplot(x='Type',
             hue='R-8-01-21',
             data=data2)

plt.pie(clb_7[clb_7['R-7-01-21']>9]['Type'].value_counts(),labels=clb_7[clb_7['R-7-01-21']>9]['Type'].unique())
plt.show()
clb_7[clb_7['R-7-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='07-01-21',kind='count',data=data2)
plt.show()

sns.countplot(x='Type',
             hue='R-7-01-21',
             data=data2)

plt.pie(clb_6[clb_6['R-6-01-21']>9]['Type'].value_counts(),labels=clb_6[clb_6['R-6-01-21']>9]['Type'].unique())
plt.show()
clb_6[clb_6['R-6-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='06-01-21',kind='count',data=data2)
plt.show()

sns.countplot(x='Type',
             hue='R-6-01-21',
             data=data2)

plt.pie(clb_5[clb_5['R-5-01-21']>9]['Type'].value_counts(),labels=clb_5[clb_5['R-5-01-21']>9]['Type'].unique())
plt.show()
clb_5[clb_5['R-5-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='05-01-21',kind='count',data=data2)
plt.show()

sns.countplot(x='Type',
             hue='R-5-01-21',
             data=data2)

plt.pie(clb_4[clb_4['R-4-01-21']>9]['Type'].value_counts(),labels=clb_4[clb_4['R-4-01-21']>9]['Type'].unique())
plt.show()
clb_4[clb_4['R-4-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='04-01-21',kind='count',data=data2)
plt.show()

sns.countplot(x='Type',
             hue='R-4-01-21',
             data=data2)

plt.pie(clb_3[clb_3['R-3-01-21']>9]['Type'].value_counts(),labels=clb_3[clb_3['R-3-01-21']>9]['Type'].unique())
plt.show()
clb_3[clb_3['R-3-01-21']>9]['Type'].value_counts()

sns.catplot(x='Type',col='03-01-21',kind='count',data=data2)
plt.show()

sns.countplot(x='Type',
             hue='R-3-01-21',
             data=data2)








