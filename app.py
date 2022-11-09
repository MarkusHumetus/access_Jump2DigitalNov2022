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

pca_6_study = PCA(n_components=6)
pca_6_study.fit(x)
x_pca_6 = pca_6_study.transform(x)

#fit the random forest with the transformed data



#transform the test data set 
test_pca_6 = pca_6_study.transform(polution_test)



print (x_pca_6)