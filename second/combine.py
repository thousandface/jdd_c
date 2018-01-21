#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
import xgboost as xgb

def eval_error(preds, df):
    label = df.get_label()
    diff = 0
    for i in range(len(preds)):
        diff += np.abs(preds[i] - label[i])
    print( 'wame', float(diff / sum(label)))
if __name__=='__main__':
    t1=pd.read_csv('../data/pa/feature01111.csv')
    t1=t1.drop_duplicates(['shop_id'])#去重复
    t1=t1.drop('dt', 1)
    t2=pd.read_csv('../data/pa/feature02222.csv')
    t2=t2.drop('dt', 1)
    t2=t2.drop_duplicates(['shop_id'])
    t3=pd.read_csv('../data/pa/feature03333.csv')
    t3=t3.drop_duplicates(['shop_id'])
    t3=t3.drop('dt', 1)
    t4=pd.read_csv('../data/pa/feature04444.csv')
    t4=t4.drop_duplicates(['shop_id'])
    t4=t4.drop('dt', 1)
    t5=pd.read_csv('../data/pa/feature05555.csv')
    t5=t5.drop_duplicates(['shop_id'])
    t5=t5.drop('dt', 1)
    t6=pd.read_csv('../data/pa/feature06666.csv')
    t6=t6.drop_duplicates(['shop_id'])
    t6=t6.drop('dt', 1)
    dateset=pd.concat([t1,t2,t3,t4,t5,t6],ignore_index=True)


    dateset=dateset.drop('shop_id', 1)
    dateset=dateset.drop('brand_pid_rate', 1)
    dateset=dateset.drop('charge_consume_rate', 1)
    dateset=dateset.drop('consume', 1)
    dateset=dateset.drop('charge', 1)
    dateset=dateset.drop('brand', 1)
    dateset=dateset.drop('cate', 1)
    dateset=dateset.drop('user_ord_rate',1)
    mean_count=dateset['pid_count'].dropna().mean()
    dateset.loc[(dateset.pid_count.isnull()), 'pid_count']=mean_count
    mean_count=dateset['brand_count'].dropna().mean()
    dateset.loc[(dateset.brand_count.isnull()), 'brand_count']=mean_count
    mean_count=dateset['cate_count'].dropna().mean()
    dateset.loc[(dateset.cate_count.isnull()), 'cate_count']=mean_count

    mean_count=dateset['cate_pid_rate'].dropna().mean()
    dateset.loc[(dateset.cate_pid_rate.isnull()), 'cate_pid_rate']=mean_count
    mean_count=dateset['rtn_rtn_rate'].dropna().mean()
    dateset.loc[(dateset.rtn_rtn_rate.isnull()), 'rtn_rtn_rate']=mean_count

    #dateset=dateset.replace(np.nan,)
    print(dateset.head())


    test=pd.read_csv('../data/pa/test1111.csv')

    test=test.drop_duplicates(['shop_id'])  #去重复
    test1=test
    test=test.drop('shop_id', 1)#删除 shop_id这一列 3.iloc则是直接通过位置来选择数据  2.loc是通过标签来选择数据

    test=test.drop('charge_consume_rate', 1)
    test=test.drop('brand_pid_rate', 1)
    test=test.drop('consume', 1)
    test=test.drop('charge', 1)
    test=test.drop('brand', 1)
    test=test.drop('cate', 1)
    test=test.drop('user_ord_rate',1)
    mean_count=test['pid_count'].dropna().mean()
    test.loc[(test.pid_count.isnull()), 'pid_count']=mean_count
    mean_count=test['brand_count'].dropna().mean()
    test.loc[(test.brand_count.isnull()), 'brand_count']=mean_count
    mean_count=test['cate_count'].dropna().mean()
    test.loc[(test.cate_count.isnull()), 'cate_count']=mean_count

    mean_count=test['cate_pid_rate'].dropna().mean()
    test.loc[(test.cate_pid_rate.isnull()), 'cate_pid_rate']=mean_count
    mean_count=test['rtn_rtn_rate'].dropna().mean()




   # y,x=np.split(dateset,(-1,),axis=1)
    x,y=np.split(dateset, (-1,), axis=1)
    #x=StandardScaler().fit_transform(x)
    #x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.2)
    # data_train=xgb.DMatrix(x,label=y)
    # data_test=xgb.DMatrix(test)
    # watch_list=[(data_train,'train')]

    shop=pd.read_csv('../data/t_order.csv')
    test1=shop.drop_duplicates(['shop_id'])
    t=test1[['shop_id']]




    depth = 8
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


    dataset = xgb.DMatrix(x,label=y)
    test=xgb.DMatrix(test)
# x_train=xgb.DMatrix(x_train)
# y_train=xgb.DMatrix(y_train)
    watchlist = [(dataset,'train')]
    model = xgb.train(params,dataset,num_boost_round=3500,evals=watchlist)
    preds=model.predict(test)
    preds = pd.DataFrame(preds)
    result = pd.concat([test1['shop_id'], preds], axis=1)
    result.to_csv('../newdata/result1126_5.csv', index=False,header=None)



