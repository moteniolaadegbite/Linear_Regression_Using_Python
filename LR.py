from importlib.metadata import metadata
from multiprocessing.resource_sharer import stop
from pyexpat import model
import sqlite3
from tracemalloc import start
from matplotlib.pyplot import step
import numpy as np
from sqlalchemy import create_engine, Table,column,Float, Integer, String, MetaData
from sklearn import linear_model
import pandas as pd
import os

# use connection to connect to a db likewise create a db if it does not exist
from sqlalchemy import create_engine
engine = create_engine('sqlite:///LR.db', echo = True)
meta = MetaData()
# creating tables in the database
# Loading train dataset
train_df = pd.read_csv('train.csv')
table_name = 'train_data'
train_df.to_sql(table_name, engine, if_exists='replace', index=False, chunksize=500)
# Loading ideal dataset
ideal_df = pd.read_csv('ideal.csv')
table_name = 'ideal_data'
ideal_df.to_sql(table_name, engine, if_exists='replace', index=False, chunksize=500)
# Loading test dataset
test_df = pd.read_csv('test.csv')
table_name = 'test_data'
test_df.to_sql(table_name, engine, if_exists='replace',index=False,chunksize =500)
meta.create_all(engine)

# calculating the square of the sum of the deviation using the train_dataset on the 50 ideal_function.
TrainSet_Y1 = [];TrainSet_Y2 = []; TrainSet_Y3 = []; TrainSet_Y4 = []
DevY = 0
#DevY =((ideal_df['y1']).sum() - (train_df['y1']).sum())**2
#print(DevY)

for i in range(1, 5):
    train_index = 'y' + str(i)
    #print(train_df['{}'.format(train_index)]) - to be deleted
    for j in range(1,51):
        ideal_index = 'y'+ str(j)
        DevY =((ideal_df['{}'.format(ideal_index)]).sum() - (train_df['{}'.format(train_index)]).sum())**2
        #print(ideal_index)  to be deleted     
        if train_index=='y1':
            TrainSet_Y1.append(DevY)
        elif train_index =='y2':
            TrainSet_Y2.append(DevY)
        elif train_index == 'y3':
            TrainSet_Y3.append(DevY)
        else:
            TrainSet_Y4.append(DevY)
print(len(TrainSet_Y1))
print(TrainSet_Y1)
#print(ideal_df.columns.values)
#factors sqrt


#creating a dictionary key value pair for the ideal function
'''SumDevSqrY1_Y =0
Dict_TrainSet_Y1 = {}
for i in range(1,50):
    #print(TrainSet_Y1[i])
   Dict_TrainSet_Y1 = {'SumDevSqrY1_Y'+str(i): TrainSet_Y1[i]}
print(Dict_TrainSet_Y1)
'''
#mylist = ["one", "two", "three"]

# Using for loop enumerate()

#{k: v+1 for k,v in Dev}
