#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.preprocessing import StandardScaler


if __name__=='__main__':
    t_order_data=pd.read_csv('./data/t_order.csv')
    t_comment_data=pd.read_csv('./data/t_comment.csv')
    t_ads_data=pd.read_csv('./data/t_ads.csv')
    t_sales_sum_data=pd.read_csv('./data/t_sales_sum.csv')
    t_product_data=pd.read_csv('./data/t_product.csv')





   # #做平滑处理 订单
   #  t_order_datas=t_order_data.columns[t_order_data.dtypes!='object'] #取出不包含object的列
   #  t_order_data_means=t_order_data.loc[:,t_order_datas].mean() #求所有列的均值
   #  t_order_data_std=t_order_data.loc[:,t_order_datas].std()  #求所有列的方差
   #  t_order_data.loc[:,t_order_datas]=(t_order_data.loc[:,t_order_datas]-t_order_data_means)/t_order_data_std

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



 #获得订单日期在 2016-8 到 2017-3之间的数据
    t_order_data_limt1=t_order_data[t_order_data['ord_dt'].map(lambda x:True if '2016-08-01' <=str(x)<='2016-12-31'else False)]

   #订单总量
    fea01_ord_cnt_sum=t_order_data_limt1.groupby(['shop_id'])['ord_cnt'].agg('sum').reset_index()
    #print(fea01_ord_cnt_sum.head())
    #获得销售金额总量
    fea01_sale_amt_sum=t_order_data_limt1.groupby(['shop_id'])['sale_amt'].agg('sum').reset_index()
    #print(fea01_sale_amt_sum.head())
    #获得下单顾客数
    fea01_user_cnt_sum=t_order_data_limt1.groupby(['shop_id'])['user_cnt'].agg('sum').reset_index()
    #获得退货总金额数
    fea01_rtn_amt_sum=t_order_data_limt1.groupby(['shop_id'])['rtn_amt'].agg('sum').reset_index()
    print(fea01_rtn_amt_sum.head())
    #退货总订单数
    fea01_rtn_cnt_sum=t_order_data_limt1.groupby(['shop_id'])['rtn_cnt'].agg('sum').reset_index()
    #优惠总金额数
    fea01_offer_amt_sum=t_order_data_limt1.groupby(['shop_id'])['offer_amt'].agg('sum').reset_index()
    #优惠总笔数
    fea01_offer_cnt_sum=t_order_data_limt1.groupby(['shop_id'])['offer_cnt'].agg('sum').reset_index()


    feature01=pd.merge(fea01_ord_cnt_sum,fea01_sale_amt_sum,on='shop_id')
    print(feature01.head())
    feature01=pd.merge(feature01,fea01_rtn_amt_sum,on='shop_id',how='left')
    feature01=pd.merge(feature01,fea01_user_cnt_sum,on='shop_id',how='left')
    feature01=pd.merge(feature01,fea01_rtn_cnt_sum,on='shop_id',how='left')
    feature01=pd.merge(feature01,fea01_offer_amt_sum,on='shop_id',how='left')
    feature01=pd.merge(feature01,fea01_offer_cnt_sum,on='shop_id',how='left')
    print(feature01.head())
    ##下单顾客数和订单总量的差值
    feature01['user_ord_rate']=feature01.user_cnt.astype('float')-feature01.ord_cnt.astype('float')
    # 销售总金额和退货总金额的比值
    feature01['rnt_sale_rate']=feature01.rtn_amt.astype('float')/feature01.sale_amt
    #优惠订单总数和订单总数的比值
    feature01['offer_ord_rate']=feature01.offer_cnt.astype('float')/feature01.ord_cnt
    #销售总金额和优惠总金额的比值
    feature01['sale_offer_rate']=feature01.offer_amt.astype('float')/feature01.sale_amt
    #销售总金额和下单顾客数的比值
    feature01['sale_user_rate']=feature01.sale_amt.astype('float')/feature01.user_cnt
    #销售总金额与订单量的比值
    feature01['sale_ord_rate']=feature01.sale_amt.astype('float')/feature01.ord_cnt
    #销售总金额和退货订单数的比值
    feature01['sale_rtn_rate']=feature01.sale_amt.astype('float')/feature01.rtn_cnt
    #优惠总金额和顾客下单数的比值
    feature01['offer_user_rate']=feature01.offer_amt.astype('float')/feature01.user_cnt
    #优惠总金额和订单数的比值
    feature01['offer_ord_rate']=feature01.offer_amt.astype('float')/feature01.ord_cnt
    #退订单数和退订金额的比值
    feature01['rtn_rtn_rate']=feature01.rtn_amt.astype('float')/feature01.rtn_cnt
    print(feature01.head())





#获得店铺评论在2016-8到2017-3之间
    t_comment_data_limt1=t_comment_data[t_comment_data['create_dt'].map(lambda x:True if '2016-08-01' <=str(x)<='2016-12-31'else False)]

    print(t_comment_data_limt1.head())
  #店铺获得的总差评数
    fea01_bad_num_sum=t_comment_data_limt1.groupby(['shop_id'])['bad_num'].agg('sum').reset_index()
    #店铺获得的总中评数
    fea01_mid_num_sum=t_comment_data_limt1.groupby(['shop_id'])['mid_num'].agg('sum').reset_index()
    #店铺获得的好评数
    fea01_good_num_sum=t_comment_data_limt1.groupby(['shop_id'])['good_num'].agg('sum').reset_index()
    #店铺获得的晒单数
    fea01_dis_num_sum=t_comment_data_limt1.groupby(['shop_id'])['dis_num'].agg('sum').reset_index()
    print(fea01_dis_num_sum.tail())
    #店铺获得的评论数
    fea01_cmmt_num_sum=t_comment_data_limt1.groupby(['shop_id'])['cmmt_num'].agg('sum').reset_index()


    #好评数和差评数的比值
    feature01=pd.merge(feature01,fea01_bad_num_sum,on='shop_id',how='left')
    feature01=pd.merge(feature01,fea01_mid_num_sum,on='shop_id',how='left')
    feature01=pd.merge(feature01,fea01_good_num_sum,on='shop_id',how='left')
    feature01=pd.merge(feature01,fea01_dis_num_sum,on='shop_id',how='left')
    feature01=pd.merge(feature01,fea01_cmmt_num_sum,on='shop_id',how='left')
    print(feature01.head())
    #晒单数和评论数的比值
    feature01['dis_cmmt_rate']=feature01.dis_num.astype('float')/feature01.cmmt_num
    #好评数和评论数的比值
    feature01['good_cmmt_rate']=feature01.good_num.astype('float')/feature01.cmmt_num
    #差评数和评论数的比值
    feature01['bad_cmmt_rate']=feature01.bad_num.astype('float')/feature01.cmmt_num
    #中评数和评论数的比值
    feature01['mid_cmmt_rate']=feature01.mid_num.astype('float')/feature01.cmmt_num
    #好评数和差评数的比值
    feature01['bad_good_rate']=feature01.good_num.astype('float')/feature01.bad_num
    #晒单数和好评数的比值
    feature01['dis_good_rate']=feature01.dis_num.astype('float')/feature01.good_num
    #好评数和中评数的比值
    feature01['mid_good']=feature01.good_num.astype('float')/feature01.mid_num
#
#
# #在2016-8 到2017-3中店铺的广告信息
    t_ads_data_limt1=t_ads_data[t_ads_data['create_dt'].map(lambda x:True if '2016-08-01' <=str(x)<='2016-12-31'else False)]

    #广告充值费用
    fea01_charge_sum=t_ads_data_limt1.groupby(['shop_id'])['charge'].agg('sum').reset_index()
    #广告消费费用
    fea01_consume_sum=t_ads_data_limt1.groupby(['shop_id'])['consume'].agg('sum').reset_index()


    feature01=pd.merge(feature01,fea01_charge_sum,on='shop_id',how='left')
    feature01=pd.merge(feature01,fea01_consume_sum,on='shop_id',how='left')
    #广告充值费用和消费费用的比值
    feature01['charge_consume_rate']=feature01.charge.astype('float')/feature01.consume




# #在2016-8 到2017-3商品
    t_product_data_limt1=t_product_data[t_product_data['on_dt'].map(lambda x:True if str(x)<='2016-12-31'else False)]

    #店铺中的商品总数
    t_product_data_limt1['pid_count']=1
    fea01_pid_sum=t_product_data_limt1.groupby(['shop_id'])['pid_count'].agg('sum').reset_index()
    #店铺中的品牌总数
    t_product_data_limt1['brand_count']=1
    fea01_brand_sum=t_product_data_limt1.groupby(['shop_id','brand'])['brand_count'].agg('sum').reset_index()
    #店铺中的商品种类个数
    t_product_data_limt1['cate_count']=1
    fea01_cate_sum=t_product_data_limt1.groupby(['shop_id','cate'])['cate_count'].agg('sum').reset_index()



  #合并
    feature01=pd.merge(feature01,fea01_pid_sum,on='shop_id',how='left')
    feature01=pd.merge(feature01,fea01_brand_sum,on='shop_id',how='left')
    feature01=pd.merge(feature01,fea01_cate_sum,on='shop_id',how='left')
    #品牌总数和商品总数的比值
    feature01['brand_pid_rate']=feature01.brand_count.astype('float')/feature01.pid_count
    #商品总类数和商品总数比值
    feature01['cate_pid_rate']=feature01.cate_count.astype('float')/feature01.pid_count

# #90天销售额
    #t_sales_sum_data_limt1=t_sales_sum_data[t_product_data['on_dt'].map(lambda x:True if str(x)<='2017-03-31'else False)]
    #feature01=pd.merge(fea01_ord_cnt_sum,fea01_sale_amt_sum,on='shop_id')

#最后一个月的销售额
    t_order_data_limt2=t_order_data[t_order_data['ord_dt'].map(lambda x:True if '2017-03-01' <=str(x)<='2017-03-31'else False)]
    label02=t_order_data_limt2.groupby(['shop_id'])['sale_amt'].agg('sum').reset_index()

    names=['shop_id','zuihou']  #重命名列
    label02.columns=names
    feature01=pd.merge(feature01,label02,on='shop_id',how='left')
# #2017-4的销售额


    t_order_data_limt2=t_order_data[t_order_data['ord_dt'].map(lambda x:True if '2017-03-01' <=str(x)<='2017-03-31'else False)]


    label01=t_order_data_limt2.groupby(['shop_id'])['sale_amt'].agg('sum').reset_index()
    names=['shop_id','y']  #重命名列
    label01.columns=names
    feature01=pd.merge(feature01,label01,on='shop_id',how='left')
    feature01.to_csv('./data/pa/feature02.csv')