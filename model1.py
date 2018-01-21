 #! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV

import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
import xgboost as xgb
from sklearn.grid_search import GridSearchCV



#特征选择




train=pd.read_csv('./data/feature1.csv')
train=train.drop_duplicates(['shop_id'])  #去重复
x_train,y_train=np.split(train, (-1,), axis=1)
x_train1=x_train.drop('shop_id',1)  #删除 shop_id这一列 3.iloc则是直接通过位置来选择数据  2.loc是通过标签来选择数据
test=pd.read_csv('./data/test1.csv')
test=x_train.drop_duplicates(['shop_id'])  #去重复
test1=x_train.drop('shop_id',1)
shop=pd.read_csv('./data/t_order.csv')
test=shop.drop_duplicates(['shop_id'])
t=test[['shop_id']]


x_train, x_test, y_train, y_test = train_test_split(x_train1, y_train, random_state=1, test_size=0.5)



# def modelfit(alg, dtrain, dtest, predictors,useTrainCV=True, cv_folds=5, early_stopping_rounds=50):
#
#     if useTrainCV:
#         xgb_param = alg.get_xgb_params()
#         xgtrain = xgb.DMatrix(dtrain[predictors].values, label=dtrain['sale_amt_y'].values)
#         xgtest = xgb.DMatrix(dtest[predictors].values)
#         cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
#              early_stopping_rounds=early_stopping_rounds, show_progress=False)
#         alg.set_params(n_estimators=cvresult.shape[0])
#
#     #建模
#     alg.fit(dtrain[predictors], dtrain['sale_amt_y'],eval_metric='auc')
#
#     #对训练集预测
#     dtrain_predictions = alg.predict(dtrain[predictors])
#     dtrain_predprob = alg.predict_proba(dtrain[predictors])[:,1]
#
#     #输出模型的一些结果
#     print ("\n关于现在这个模型")
#     print ("准确率 : %.4g" % metrics.accuracy_score(dtrain['sale_amt_y'].values, dtrain_predictions))
#     print ("AUC 得分 (训练集): %f" % metrics.roc_auc_score(dtrain['sale_amt_y'], dtrain_predprob))
#
#     feat_imp = pd.Series(alg.booster().get_fscore()).sort_values(ascending=False)
#     feat_imp.plot(kind='bar', title='Feature Importances')
#     plt.ylabel('Feature Importance Score')
#
# predictors = [x for x in train.columns if x not in ['sale_amt_y', 'shop_id']]
# xgb1 = XGBClassifier(
#         learning_rate =0.1,
#         n_estimators=1000,
#         max_depth=5,
#         min_child_weight=1,
#         gamma=0,
#         subsample=0.8,
#         colsample_bytree=0.8,
#         objective= 'reg:logistic',
#         nthread=4,
#         scale_pos_weight=1,
#         seed=27)
# modelfit(xgb1, train, test, predictors)

 #XGBoost
data_train = xgb.DMatrix(x_train, label=y_train)
data_test = xgb.DMatrix(x_test, label=y_test)
watch_list = [(data_test, 'eval'), (data_train, 'train')]
param = {'max_depth': 5, 'eta': 0.1, 'silent': 1, 'objective': 'reg:logistic'}
             # 'subsample': 1, 'alpha': 0, 'lambda': 0, 'min_child_weight': 1}
bst = xgb.train(param, data_train, num_boost_round=100, evals=watch_list)

t['y_hat']= bst.predict(test1)
print(t.head())

t.to_csv('./data/pre1.csv')









