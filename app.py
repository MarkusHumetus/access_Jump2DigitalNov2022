#Data exploration & manipulation
import pandas as pd
import numpy as np
from collections import Counter
import datetime as dt
import os
import matplotlib.pyplot as plt


#ML Models search and optimisation
from pycaret.classification import * 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, confusion_matrix
#import optuna
# print('optuna: %s' % optuna.__version__) # print version
from sklearn.model_selection import cross_val_score, RandomizedSearchCV, RepeatedKFold, GridSearchCV


# Data manipulation
import pandas as pd # for data manipulation
print('pandas: %s' % pd.__version__) # print version
import numpy as np # for data manipulation
print('numpy: %s' % np.__version__) # print version


# Sklearn
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import sklearn # for model evaluation
print('sklearn: %s' % sklearn.__version__) # print version
from sklearn.model_selection import train_test_split # for splitting the data into train and test samples
from sklearn.preprocessing import OrdinalEncoder # for encoding labels
from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import StratifiedShuffleSplit # to split stratified 
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, balanced_accuracy_score, precision_score, recall_score, f1_score, cohen_kappa_score, matthews_corrcoef, roc_auc_score, confusion_matrix
from sklearn.decomposition import PCA

# Visualization
import matplotlib.image as mpimg
import plotly.io as pio #To fix an issue with the renderer of graphs in VSC
pio.renderers
import matplotlib 
import matplotlib.pyplot as plt # for showing images
print('matplotlib: %s' % matplotlib.__version__) # print version
import random
import seaborn as sns
sns.set_style('white') 


# Other utilities
import sys
import os
from platform import python_version
import datetime
from time import localtime, strftime, gmtime
import pathlib


# Import initial files from the website

polution_train = pd.read_csv("https://challenges-asset-files.s3.us-east-2.amazonaws.com/Events/Jump2digital+2022/train.csv", sep=";")

polution_test = pd.read_csv("https://challenges-asset-files.s3.us-east-2.amazonaws.com/Events/Jump2digital+2022/test.csv", sep=";")


x=polution_train.copy()
x.drop('target',axis=1, inplace =True)

y=polution_train.target



#Random forest with the best tunned hyperparameters (see Jupyter Notebook) 

rf_best_model = RandomForestClassifier(bootstrap=True,
                                          ccp_alpha=0.0,
                                          class_weight=None,
                                          criterion ='gini',
                                          max_depth = 25,
                                          max_features = 0.45,
                                          max_leaf_nodes = None,
                                          max_samples = None,
                                          min_impurity_decrease = 0.0,
                                          min_samples_leaf = 1,
                                          min_samples_split = 2,
                                          min_weight_fraction_leaf = 0.0,
                                          n_estimators = 572
                                          )  


rf_best_model.fit(x,y)

x_test_pred = rf_best_model.predict(polution_test)

predictions_df = pd.DataFrame(x_test_pred, columns=['final_status'])

predictions_df.to_csv('predictions.csv',index=False) #saving predictions to a csv eda_37file

predictions_df.to_json('predictions.json') #saving predictions to a json file
