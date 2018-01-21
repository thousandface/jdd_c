#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import pandas as pd
from xgboost import XGBRegressor
import numpy as np
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import BaggingRegressor
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Imputer
from sklearn import preprocessing
import xgboost as xgb



train=pd.read_csv('./data/pa/feature02.csv')
train=train.drop_duplicates(['shop_id'])  #去重复



train=train.drop('shop_id',1)#删除 shop_id这一列 3.iloc则是直接通过位置来选择数据  2.loc是通过标签来选择数据
train=train.drop('charge_consume_rate',1)
train=train.drop('consume',1)
train=train.drop('charge',1)
train=train.drop('brand',1)
train=train.drop('cate',1)
train=train.drop('brand_pid_rate', 1)
mean_count=train['pid_count'].dropna().mean()
train.loc[(train.pid_count.isnull()),'pid_count']=mean_count
mean_count=train['brand_count'].dropna().mean()
train.loc[(train.brand_count.isnull()),'brand_count']=mean_count
mean_count=train['cate_count'].dropna().mean()
train.loc[(train.cate_count.isnull()),'cate_count']=mean_count
# mean_count=train['brand_pid_rate'].dropna().mean()
# train.loc[(train.brand_pid_rate.isnull()),'brand_pid_rate']=mean_count
mean_count=train['cate_pid_rate'].dropna().mean()
train.loc[(train.cate_pid_rate.isnull()),'cate_pid_rate']=mean_count
mean_count=train['rtn_rtn_rate'].dropna().mean()
train.loc[(train.rtn_rtn_rate.isnull()),'rtn_rtn_rate']=mean_count
mean_count=train['zuihou'].dropna().mean()
train.loc[(train.zuihou.isnull()),'zuihou']=mean_count
mean_count=train['y'].dropna().mean()
train.loc[(train.y.isnull()),'y']=mean_count

print(train.head())
#x_train,y_train=np.split(train, (-1,), axis=1)



#测试数据
test=pd.read_csv('./data/pa/test02.csv')
test=test.drop_duplicates(['shop_id'])  #去重复

test=test.drop('shop_id', 1)#删除 shop_id这一列 3.iloc则是直接通过位置来选择数据  2.loc是通过标签来选择数据

test=test.drop('charge_consume_rate', 1)
test=test.drop('consume', 1)
test=test.drop('charge', 1)
test=test.drop('brand', 1)
test=test.drop('cate', 1)
mean_count=test['pid_count'].dropna().mean()
test.loc[(test.pid_count.isnull()), 'pid_count']=mean_count
mean_count=test['brand_count'].dropna().mean()
test.loc[(test.brand_count.isnull()), 'brand_count']=mean_count
mean_count=test['cate_count'].dropna().mean()
test.loc[(test.cate_count.isnull()), 'cate_count']=mean_count
mean_count=test['brand_pid_rate'].dropna().mean()
test.loc[(test.brand_pid_rate.isnull()), 'brand_pid_rate']=mean_count
mean_count=test['cate_pid_rate'].dropna().mean()
test.loc[(test.cate_pid_rate.isnull()), 'cate_pid_rate']=mean_count
mean_count=test['rtn_rtn_rate'].dropna().mean()
test.loc[(test.rtn_rtn_rate.isnull()), 'rtn_rtn_rate']=mean_count
train.loc[(train.zuihou.isnull()),'zuihou']=mean_count
mean_count=train['y'].dropna().mean()
train.loc[(train.y.isnull()),'y']=mean_count
print(test.head())


shop=pd.read_csv('./data/t_order.csv')
test1=shop.drop_duplicates(['shop_id'])
t=test1[['shop_id']]

# x_train = Imputer().fit_transform(x_train) #将数据中的NAN填充
# y_train = Imputer().fit_transform(y_train)


#print(x_train.head())
# x_train1 = Imputer().fit_transform(x_train1) #将数据中的NAN填充
# y_train = Imputer().fit_transform(y_train)


# print(x_train)
#
# y_train=y_train.ravel()
# test=pd.read_csv('./data/test3.csv')
# test=x_train.drop_duplicates(['shop_id'])  #去重复
# test1=x_train.drop('shop_id',1)
# test1 = Imputer().fit_transform(test1)
#
# print(test1)
#
# shop=pd.read_csv('./data/t_order.csv')
# test=shop.drop_duplicates(['shop_id'])
# t=test[['shop_id']]



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


dataset12 = xgb.DMatrix(x_train,label=y_train)
test=xgb.DMatrix(test)
# x_train=xgb.DMatrix(x_train)
# y_train=xgb.DMatrix(y_train)
watchlist = [(dataset12,'train')]
model = xgb.train(params,dataset12,num_boost_round=3500,evals=watchlist)
t['hat']=model.predict(test)
t.to_csv('./data/pa/t02.csv')




#     #对训练集预测
# #predictors = [x for x in x_train.columns if x not in ['shop_id', 'sale_amt_y']]
#dtrain_predictions = model.predict(x_train)
# dtrain_predprob = model.predict_proba(x_train)[:,1]
# from sklearn import cross_validation, metrics
#     #输出模型的一些结果
# print ("\n关于现在这个模型")
# print ("准确率 : %.4g" % metrics.accuracy_score(y_train['sale_amt_y'].values, dtrain_predictions))
# print ("AUC 得分 (训练集): %f" % metrics.roc_auc_score(y_train['sale_amt_y'], dtrain_predprob))
# import matplotlib.pyplot as plt
# feat_imp = pd.Series(model.booster().get_fscore()).sort_values(ascending=False)
# feat_imp.plot(kind='bar', title='Feature Importances')
# plt.ylabel('Feature Importance Score')

#获得特征得分
# feature_score = model.get_fscore()
# feature_score = sorted(feature_score.items(), key=lambda x:x[1],reverse=True)
# fs = []
# for (key,value) in feature_score:
#     fs.append("{0},{1}\n".format(key,value))
#
# with open('xgb_feature_score.csv','w') as f:
#     f.writelines("feature,score\n")
#     f.writelines(fs)

# from sklearn.preprocessing import StandardScaler
# from sklearn.cross_validation import train_test_split
# def eval_error(preds, df):
#     preds=np.array(preds).tolist()
#     df=np.array(preds).tolist()
#
#     label = df
#     diff = 0
#     for i in range(len(preds)):
#         diff += np.abs(preds[i] - df[i])
#     print( 'wame', float(diff / sum(df)))
#
# x,y=np.split(train,(-1,),axis=1)
# #x=StandardScaler().fit_transform(x)
# x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.2)
# data_train=xgb.DMatrix(x_train,label=y_train)
# data_test=xgb.DMatrix(x_test,label=y_test)
# watch_list=[(data_test,'eval'),(data_train,'train')]
#
# depth = 13
# eta = 0.01
# ntrees = 8000
# mcw = 3
# params = {"objective": "reg:linear",
#               "booster": "gbtree",
#               "eta": eta,
#               "max_depth": depth,
#               "min_child_weight": mcw,
#               "subsample": 0.9,
#               "colsample_bytree": 0.7,
#               "silent": 1
#               }
# bst=xgb.train(params,data_train,num_boost_round=1000,evals=watch_list)
# y_hat=bst.predict(data_test)
# # eval_error(y_hat,y_test)
# y_hat=np.array(y_hat).tolist()
# y_test=np.array(y_test).tolist()

