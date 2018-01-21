import pandas as pd
import numpy as np
import xgboost as xgb
from xgboost.sklearn import XGBRegressor
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV
from sklearn import preprocessing

import matplotlib.pylab as plt

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 12, 4

train = pd.read_csv('./data/feature11.csv')
test = pd.read_csv('./data/test11.csv')
train=train.drop_duplicates(['shop_id'])  #去重复
test=test.drop_duplicates(['shop_id'])  #去重复
# min_max_scaler = preprocessing.MinMaxScaler()
# train['sale_amt_y']=min_max_scaler.fit_transform(train['sale_amt_y'])

target='sale_amt_y'
IDcol = 'shop_id'

def modelfit(alg, dtrain, dtest, predictors,useTrainCV=True, cv_folds=5, early_stopping_rounds=50):

    # if useTrainCV:
    #     xgb_param = alg.get_xgb_params()
    #     xgtrain = xgb.DMatrix(dtrain[predictors].values, label=dtrain[target].values)
    #
    #     cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
    #          early_stopping_rounds=early_stopping_rounds)
    #
    #     alg.set_params(n_estimators=cvresult.shape[0])

     depth = 13
     eta = 0.01
     ntrees = 8000
     mcw = 3
     params = {"objective": "reg:linear",
              "booster": "gbtree",
              "eta": eta,
              "max_depth": depth,
              "min_child_weight": mcw,
              "subsample": 0.9,
              "colsample_bytree": 0.7,
              "silent": 1
              }
    #建模
    # watchlist=[()]
    # alg.fit(dtrain[predictors], dtrain['sale_amt_y'],eval_metric='auc')
    #
    # #对训练集预测
    # dtrain_predictions = alg.predict(dtrain[predictors])
    # dtrain_predprob = alg.predict_proba(dtrain[predictors])[:,1]
    #
    # #输出模型的一些结果
    # print ("\n关于现在这个模型")
    # print ("准确率 : %.4g" % metrics.accuracy_score(dtrain['sale_amt_y'].values, dtrain_predictions))
    # print ("AUC 得分 (训练集): %f" % metrics.roc_auc_score(dtrain['sale_amt_y'], dtrain_predprob))
    #
    # feat_imp = pd.Series(alg.booster().get_fscore()).sort_values(ascending=False)
    # feat_imp.plot(kind='bar', title='Feature Importances')
    # plt.ylabel('Feature Importance Score')

predictors = [x for x in train.columns if x not in [target, IDcol]] #选取所有列
xgb1 = XGBRegressor(
        learning_rate =0.1,
        n_estimators=1000,
        max_depth=5,
        min_child_weight=1,
        gamma=0,
        subsample=0.8,
        colsample_bytree=0.8,
        objective= 'reg:linear',
        nthread=4,
        scale_pos_weight=1,
        seed=27)
modelfit(xgb1, train, test, predictors)
