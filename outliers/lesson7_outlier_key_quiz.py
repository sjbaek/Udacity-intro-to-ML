# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:31:01 2015

@author: seungjinbaek
"""


# solution to lesson 7 - outlier

for s in data_dict:
    salary = data_dict[s]["salary"]
    if salary is not "NaN" and float(salary) > 1e7:
        print s
        print "---"

# result of above script was 'TOTAL' and was removed by .pop

# find two people with bonus > 5 mil and salary > 1 mil
        
for s in data_dict:
    salary = data_dict[s]["salary"]
    bonus = data_dict[s]["bonus"]
    if salary is not "NaN" and float(salary) > 1e6:
        if bonus is not "NaN" and float(bonus) > 5e6:
            print s

# solution to Lesson 8 - stock option range
# find max and min from "exercised_stock_options"
newStock = []    
for s in data_dict:
    stock = data_dict[s]["exercised_stock_options"]
    # bonus = data_dict[s]["bonus"]
    
    if stock != "NaN":
    
        # print stock
        newStock.append(stock)
print 'max stock = ',max(newStock)
print 'min stock = ',min(newStock)                   

newStock = []    
for s in data_dict:
    stock = data_dict[s]["salary"]
    # bonus = data_dict[s]["bonus"]
    
    if stock != "NaN":
    
        # print stock
        newStock.append(stock)
print 'max salary = ',max(newStock)
print 'min salary = ',min(newStock)   