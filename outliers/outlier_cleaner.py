#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    import numpy as np    
#    
    error = abs(predictions - net_worths)  # 90x1 array
    ind_error = error.argsort(axis = 0)   # sort by column
    
    # error[ind_error][0:81]
    
    three_array = np.hstack((ages[ind_error,0][0:81], net_worths[ind_error,0][0:81], error[ind_error,0][0:81]))
    
    # three_array = np.hstack((ages_train[ind_error,0][0:81], net_worths_train[ind_error,0][0:81], error[ind_error,0][0:81]))
#    
#    
#    
    cleaned_data = tuple(map(tuple,three_array))
    
    return cleaned_data

