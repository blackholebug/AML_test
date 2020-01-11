#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:21:21 2020

@author: s2432234
"""
import time

from autosklearn.classification import AutoSklearnClassifier
from autosklearn.regression import AutoSklearnRegressor
from sklearn.model_selection import train_test_split

import sklearn.datasets as ds

from sklearn.metrics import classification_report
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

cls_dataset = [ds.load_iris, ds.load_digits, ds.load_wine, ds.load_breast_cancer]
rgr_dataset = [ds.load_boston, ds.load_diabetes, ds.load_linnerud]

print('[INFO] Loading dataset.')
X, y = rgr_dataset[1](return_X_y=True)
#feature_types = (['numerical'] * 3) + ['categorical'] + (['numerical'] * 9)
 
print('[INFO] Splitting.')
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, train_size=0.8)
 
print(f'[INFO] Train shape: {X_train.shape}')
print(f'[INFO] Test shape: {X_test.shape}')
 
print('[INFO] Finding best model...')
#for auto vanilla, add this : #ensemble_size=1, initial_configurations_via_metalearning=0
#-----CLASSIFIER-----
#automl = AutoSklearnClassifier(per_run_time_limit=300, ml_memory_limit=1024 * 6, time_left_for_this_task=3600, resampling_strategy='cv',
#        resampling_strategy_arguments={'folds': 5})
#-----REGRESSION-----
automl = AutoSklearnRegressor(per_run_time_limit=300, ml_memory_limit=1024 * 6, time_left_for_this_task=3600, resampling_strategy='cv',
        resampling_strategy_arguments={'folds': 5})
start = time.time()
 
#X_train = X_train.astype('float')
automl.fit(X_train, y_train, dataset_name='linnerud')   #change dataset name accordingly
automl.refit(X_train.copy(), y_train.copy())
print(f'[INFO] Elapsed time finding best model: {time.time() - start} seconds.') 

predictions = automl.predict(X_test)
#print('--- CLASSIFICATION REPORT: ---')        #not for regression
#print(classification_report(y_test, predictions, digits=5))
print('\n\n--- MODELS: ---')
print(automl.show_models())
print('\n\n--- STATISTICS: ---')
print(automl.sprint_statistics()) 

#-----CLASSIFIER-----
#print('\n\n--- SCORE: ---')
#print("Balanced error score", 1 - balanced_accuracy_score(y_test, predictions))
#-----REGRESSION-----
print('\n\n--- SCORE: ---')
print("R2 score", 1 - r2_score(y_test, predictions))