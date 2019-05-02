import os
import glob
import pandas as pd
import csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import matplotlib.gridspec as gridspec
from sklearn.model_selection import KFold, train_test_split, GridSearchCV


def randforest_param_selection(X, y, nfolds):
    param_grid = {
    'bootstrap': [True],
    'max_depth': [80, 90, 100, 110],
    'max_features': [2, 3],
    'min_samples_leaf': [3, 4, 5],
    'min_samples_split': [8, 10, 12],
    'n_estimators': [100, 200, 300, 1000]
    }
    rf=RandomForestClassifier()
    grid_search = GridSearchCV(estimator = rf, param_grid = param_grid, 
                          cv = 3, n_jobs = -1, verbose = 2)
    grid_search.fit(X, y)
    grid_search.best_params_
    return grid_search.best_params_

df1=pd.read_csv("for_model.csv")


target = df1.iloc[:,1]
catenc = pd.factorize(target)
target = catenc[0]
data = df1.iloc[:,2:18]
data_training, data_test, target_training, target_test = train_test_split(data, target, test_size = 0.25, random_state = 25)
print(data.shape)
print(target.shape)
print(data_training.shape)
print(data_test.shape)
print(target_training.shape)
print(target_test.shape)

randfor_best=randforest_param_selection(data_training,target_training,1)
print(randfor_best)

