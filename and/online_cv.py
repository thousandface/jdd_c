
import pandas as pd
import numpy as np
import datetime

#获取全部特征
feature_all = pd.read_csv('../newdata/feature_all.csv')
feature_all['dt'] = pd.to_datetime(feature_all['dt'])

#获取静态特征
static_feature = pd.read_csv('../newdata/static_feature.csv')
static_feature['dt'] = pd.to_datetime(static_feature['dt'])



#获取精准label
label_act = pd.read_csv('../newdata/t_sales_sum.csv')
label_act['dt'] = pd.to_datetime(label_act['dt'])
label_act.rename(columns={'sale_amt_3m':'label'},inplace=True)

#获取评论
comment_all = pd.read_csv('../newdata/comment_feature_all.csv')
comment_all['dt'] = pd.to_datetime(comment_all['dt'])

#获取静态评论
comment_static = pd.read_csv('../newdata/static_comment.csv')
comment_static['dt'] = pd.to_datetime(comment_static['dt'])

#确定线上CV时间：
train_begin = datetime.date(2016,11,30)
train_end = datetime.date(2017,1,31)

test = datetime.date(2017,4,30)

#构造训练集：
train = feature_all[(train_begin <= feature_all['dt'])\
                    & (feature_all['dt'] <= train_end)]
train = pd.merge(train, static_feature, how='left', on=['shop_id','dt'])
#1124加入评论
train = pd.merge(train, comment_all, how='left', on=['shop_id', 'dt'])
train = pd.merge(train, comment_static, how='left', on=['shop_id','dt'])
train = pd.merge(train, label_act, how='left', on=['shop_id', 'dt'])


#构造测试集：
test = feature_all[feature_all['dt'] == test]
shoplist = list(test['shop_id'])
test = pd.merge(test, static_feature, how='left', on=['shop_id','dt'])
test = pd.merge(test, comment_all, how='left', on=['shop_id', 'dt'])
test = pd.merge(test, comment_static, how='left', on=['shop_id','dt'])
test = pd.merge(test, label_act, how='left', on=['shop_id', 'dt'])


train.to_csv('../newdata/online_train_1126.csv',index=False)
test.to_csv('../newdata/online_test_1126.csv',index=False)