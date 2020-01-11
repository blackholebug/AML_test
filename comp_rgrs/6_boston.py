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

rgr_dataset = [ds.load_boston, ds.load_diabetes, ds.load_linnerud, ds.fetch_california_housing]

print('[INFO] Loading dataset.')

X, y = rgr_dataset[0](return_X_y=True)
#feature_types = (['numerical'] * 3) + ['categorical'] + (['numerical'] * 9)
 
print('[INFO] Splitting.')
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, train_size=0.8)
 
print('[INFO] Train shape: {}'.format(X_train.shape))
print('[INFO] Test shape: {}'.format(X_test.shape))
print('[INFO] Finding best model...')

#for auto vanilla, add this : #ensemble_size=1, initial_configurations_via_metalearning=0
#for specific clf or rgr or prep :     include_estimators=["random_forest", ], exclude_estimators=None,
#                                      include_preprocessors=["no_preprocessing", ], exclude_preprocessors=None)

#-----CLASSIFIER-----
#automl = AutoSklearnClassifier(per_run_time_limit=300, ml_memory_limit=1024 * 6, 
#                               time_left_for_this_task=300, resampling_strategy='cv',
#                               ensemble_size=1, initial_configurations_via_metalearning=0, 
#                               resampling_strategy_arguments={'folds': 5})

#-----REGRESSION-----
automl = AutoSklearnRegressor(per_run_time_limit=300, ml_memory_limit=1024 * 4, 
                              time_left_for_this_task=1800, resampling_strategy='cv',
                              include_estimators=["gradient_boosting", ], exclude_estimators=None,
                              resampling_strategy_arguments={'folds': 5})
start = time.time()
 
#X_train = X_train.astype('float') # when?
automl.fit(X_train, y_train, dataset_name='boston_housing')   #change dataset name accordingly
automl.refit(X_train.copy(), y_train.copy())
print('[INFO] Elapsed time finding best model: {} seconds.'.format(time.time() - start)) 

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
print("R2 score", r2_score(y_test, predictions))