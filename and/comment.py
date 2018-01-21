import numpy as np
import pandas as pd
import datetime

comment = pd.read_csv('../newdata/t_comment.csv')
t_product=pd.read_csv('../newdata/t_product.csv')
comment['create_dt'] = pd.to_datetime(comment['create_dt'])
t_product['on_dt']=pd.to_datetime(t_product['on_dt'])

#时间滑窗
date_list = ['2016/6/30','2016/7/31','2016/8/31','2016/9/30','2016/10/31','2016/11/30','2016/12/31','2017/1/31','2017/2/28','2017/3/31','2017/4/30']
delta = datetime.timedelta(days=30)
date_list = pd.to_datetime(date_list)

#特征提取
feature = pd.DataFrame()
for d in date_list:
    time_interval = comment[(d - delta < comment['create_dt']) & (comment['create_dt'] <= d)]
    t_product=t_product[t_product['on_dt'] <=d]
    #bad_amt
    bad_num = time_interval.groupby('shop_id', as_index=False).agg({'bad_num':['sum']})
    bad_num.columns = ['shop_id', 'bad_num_sum']
    #cmmt_num
    cmmt_num = time_interval.groupby('shop_id', as_index=False).agg({'cmmt_num': ['sum']})
    cmmt_num.columns = ['shop_id', 'cmmt_num_sum']
    all_feature = pd.merge(bad_num, cmmt_num, on='shop_id')
    #dis_num
    dis_num= time_interval.groupby('shop_id', as_index=False).agg({'dis_num': ['sum']})
    dis_num.columns = ['shop_id', 'dis_num_sum']
    all_feature = pd.merge(all_feature, dis_num, on='shop_id')
    #good_num
    good_num = time_interval.groupby('shop_id', as_index=False).agg({'good_num': ['sum']})
    good_num.columns = ['shop_id', 'good_num_sum']
    all_feature = pd.merge(all_feature, good_num, on='shop_id')
    #mid_num
    mid_num = time_interval.groupby('shop_id', as_index=False).agg({'mid_num': ['sum']})
    mid_num.columns = ['shop_id', 'mid_num_sum']
    all_feature = pd.merge(all_feature, mid_num, on='shop_id')
    all_feature.rename(columns={'create_dt':'dt'}, inplace=True)
    all_feature['dt'] = d
    #晒单数和评论数的比值

    #好评数和评论数的比值
    all_feature['good_cmmt_rate']=all_feature.good_num_sum.astype('float')/all_feature.cmmt_num_sum
    #差评数和评论数的比值
    all_feature['bad_cmmt_rate']=all_feature.bad_num_sum.astype('float')/all_feature.cmmt_num_sum
    #中评数和评论数的比值
    all_feature['mid_cmmt_rate']=all_feature.mid_num_sum.astype('float')/all_feature.cmmt_num_sum
    #好评数和差评数的比值
    all_feature['bad_good_rate']=all_feature.good_num_sum.astype('float')/all_feature.bad_num_sum
    #晒单数和好评数的比值
    #all_feature['dis_good_rate']=all_feature.dis_num_sum.astype('float')/all_feature.good_num_sum
    #好评数和中评数的比值
    all_feature['mid_good_rate']=all_feature.good_num_sum.astype('float')/all_feature.mid_num_sum
    t_product['pid_count']=1
    pid_sum=t_product.groupby('shop_id',as_index=False).agg({'pid_count':['sum']})
    pid_sum.columns=['shop_id','pid_sum']
    all_feature=pd.merge(all_feature,pid_sum,on='shop_id')

    feature = pd.concat([feature, all_feature])
    print(d)

#输出
feature.to_csv('../newdata/comment_feature_all.csv', index=False)