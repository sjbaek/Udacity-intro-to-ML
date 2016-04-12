# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 15:37:56 2016

@author: seungjinbaek
"""
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 

# remove outlier, which is 'total'
data_dict.pop("TOTAL",0)
max = -1.0
min = 999999999
for dat in data_dict:
    val = data_dict[dat]['exercised_stock_options']
    #val = data_dict[dat]['salary']
    if val!= 'NaN':
        if float(val) > max:
            max = float(val)
        if float(val) < min:
            min = float(val)
#    print '\n'
