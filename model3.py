#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import pandas as pd
from xgboost import XGBRegressor
import numpy as np
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import BaggingRegressor
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Imputer



train=pd.read_csv('./data/feature3.csv')
train=train.drop_duplicates(['shop_id'])  #去重复
x_train,y_train=np.split(train, (-1,), axis=1)
x_train1=x_train.drop('shop_id',1)#删除 shop_id这一列 3.iloc则是直接通过位置来选择数据  2.loc是通过标签来选择数据
print(x_train.head())
x_train1 = Imputer().fit_transform(x_train1) #将数据中的NAN填充
y_train = Imputer().fit_transform(y_train)

print(x_train)

y_train=y_train.ravel()
test=pd.read_csv('./data/test3.csv')
test=x_train.drop_duplicates(['shop_id'])  #去重复
test1=x_train.drop('shop_id',1)
test1 = Imputer().fit_transform(test1)

print(test1)

shop=pd.read_csv('./data/t_order.csv')
test=shop.drop_duplicates(['shop_id'])
t=test[['shop_id']]

#
# x_train = xgb.DMatrix(x_train,label=y_train)
# x_test=xgb.DMatrix(test1)
#
# param = {'max_depth': 3, 'eta': 1, 'silent': 0}
#
# watchlist = [(x_train,'train')]
# print('start...train')
# model = xgb.train(param,x_train,num_boost_round=500,evals=watchlist)
# print('start_test')
# t['y_hat']= model.predict(test1)
# t.to_csv('./data/pre.csv')params = [1,2,3,4,5,6]


# params = [1,2,3,4,5,6]
# test_scores = []
# for param in params:
#     clf = XGBRegressor(max_depth=param)
#     test_score = np.sqrt(-cross_val_score(clf, x_train1, y_train, cv=10, scoring='mean_squared_error'))
#     test_scores.append(np.mean(test_score))
# import matplotlib.pyplot as plt
# print(test_scores)
# plt.plot(params, test_scores)
# plt.title("max_depth vs CV Error")
# plt.show()


clf=XGBRegressor(max_depth=3)
print("start..train")
clf.fit(x_train1,y_train)
print('start..test')
t['y_hat']=clf.predict(test1)
#t.to_csv('./data/pre3.csv')
#save feature score
feature_score = clf.get_fscore()
feature_score = sorted(feature_score.items(), key=lambda x:x[1],reverse=True)
fs = []
for (key,value) in feature_score:
    fs.append("{0},{1}\n".format(key,value))

with open('xgb_feature_score.csv','w') as f:
    f.writelines("feature,score\n")
f.writelines(fs)



# from sklearn.linear_model import Ridge
# ridge = Ridge(15)
# params = [1, 10, 15, 20, 25, 30, 40]
# test_scores = []
# for param in params:
#     clf = BaggingRegressor(n_estimators=param, base_estimator=ridge)
#     test_score = np.sqrt(-cross_val_score(clf, x_train1, y_train, cv=10, scoring='mean_squared_error'))
#     test_scores.append(np.mean(test_score))
#
#
# print(test_scores)
# import matplotlib.pyplot as plt

# plt.plot(params, test_scores)
# plt.title("max_depth vs CV Error")
# plt.show()