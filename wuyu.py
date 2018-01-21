#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import pandas as pd


if __name__=='__main__':
    t_order_data=pd.read_csv('./data/t_order.csv')
    t_comment_data=pd.read_csv('./data/t_comment.csv')
    t_ads_data=pd.read_csv('./data/t_ads.csv')
    t_sales_sum_data=pd.read_csv('./data/t_sales_sum.csv')
    t_product_data=pd.read_csv('./data/t_product.csv')

    #特征一 2016 8 到 2017 3
    ord_feature1=t_order_data[t_order_data['ord_dt'].map(lambda x:True if '2016-08-01' <=str(x)<='2017-04-30'else False)]
    cmt_feature1=t_comment_data[t_comment_data['ord_dt'].map(lambda x:True if '2016-08-01' <=str(x)<='2017-04-30'else False)]
    pro_feature1=t_product_data[t_product_data['ord_dt'].map(lambda x:True if '2016-08-01' <=str(x)<='2017-04-30'else False)]
    ads_feature1=t_ads_data[t_ads_data['ord_dt'].map(lambda x:True if '2016-08-01' <=str(x)<='2017-04-30'else False)]

    #提取商品id

  #   feature01=pd.merge(feature01,fea01_rtn_amt_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_user_cnt_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_rtn_cnt_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_offer_amt_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_offer_cnt_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_user_ord_cnt_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_slae_rnt_rate,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_ord_rnt_rate,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_offer_ord_rate,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_off_sale_rate,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_mid_num_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_good_num_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_dis_num_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_cmmt_num_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_cmmt_dis_rate,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_good_cmmt_rate,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_bad_cmmt_rate,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_mid_cmmt_rate,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_good_bad_rate,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_charge_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_consume_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_pid_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_brand_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_brand_pid_rate,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_cate_sum,on='shop_id',how='left')
#     feature01=pd.merge(feature01,fea01_cate_pid_rate,on='shop_id',how='left')
#     #feature01=pd.merge(feature01,fea01_bad_cmmt_rate,on='shop_id',how='left')






  #做平滑处理 订单
    # t_order_datas=t_order_data.columns[t_order_data.dtypes!='object'] #取出不包含object的列
    # t_order_data_means=t_order_data.loc[:,t_order_datas].mean() #求所有列的均值
    # t_order_data_std=t_order_data.loc[:,t_order_datas].std()  #求所有列的方差
    # t_order_data.loc[:,t_order_datas]=(t_order_data.loc[:,t_order_datas]-t_order_data_means)/t_order_data_std

    #  #做平滑处理   评论
    # t_order_datas=t_comment_data.columns[t_order_data.dtypes!='object'] #取出不包含object的列
    # t_order_data_means=t_comment_data.loc[:,t_order_datas].mean() #求所有列的均值
    # t_order_data_std=t_comment_data.loc[:,t_order_datas].std()  #求所有列的方差
    # t_comment_data.loc[:,t_order_datas]=(t_comment_data.loc[:,t_order_datas]-t_order_data_means)/t_order_data_std
    #
    #  #做平滑处理  销量
    # t_order_datas=t_sales_sum_data.columns[t_order_data.dtypes!='object'] #取出不包含object的列
    # t_order_data_means=t_sales_sum_data.loc[:,t_order_datas].mean() #求所有列的均值
    # t_order_data_std=t_sales_sum_data.loc[:,t_order_datas].std()  #求所有列的方差
    # t_sales_sum_data.loc[:,t_order_datas]=(t_sales_sum_data.loc[:,t_order_datas]-t_order_data_means)/t_order_data_std
    #
    #  #做平滑处理  商品
    # t_order_datas=t_product_data.columns[t_order_data.dtypes!='object'] #取出不包含object的列
    # t_order_data_means=t_product_data.loc[:,t_order_datas].mean() #求所有列的均值
    # t_order_data_std=t_product_data.loc[:,t_order_datas].std()  #求所有列的方差
    # t_product_data.loc[:,t_order_datas]=(t_product_data.loc[:,t_order_datas]-t_order_data_means)/t_order_data_std
    #
    #  #做平滑处理  广告
    # t_order_datas=t_ads_data.columns[t_order_data.dtypes!='object'] #取出不包含object的列
    # t_order_data_means=t_ads_data.loc[:,t_order_datas].mean() #求所有列的均值
    # t_order_data_std=t_ads_data.loc[:,t_order_datas].std()  #求所有列的方差
    # t_ads_data.loc[:,t_order_datas]=(t_ads_data.loc[:,t_order_datas]-t_order_data_means)/t_order_data_std

