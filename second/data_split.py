#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.preprocessing import StandardScaler


if __name__=='__main__':
    t_order_data=pd.read_csv('../data/t_order.csv')
    t_comment_data=pd.read_csv('../data/t_comment.csv')
    t_ads_data=pd.read_csv('../data/t_ads.csv')
    t_sales_sum_data=pd.read_csv('../data/t_sales_sum.csv')
    t_product_data=pd.read_csv('../data/t_product.csv')


    t_order_data_limt1=t_order_data[t_order_data['ord_dt'].map(lambda x:True if '2016-08-01' <=str(x)<='2016-08-31'else False)]
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


    #9月订单
    t_order_data_limt1=t_order_data[t_order_data['ord_dt'].map(lambda x:True if '2016-09-01' <=str(x)<='2016-09-30'else False)]
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


    feature02=pd.merge(fea01_ord_cnt_sum,fea01_sale_amt_sum,on='shop_id')
    print(feature02.head())
    feature02=pd.merge(feature02,fea01_rtn_amt_sum,on='shop_id',how='left')
    feature02=pd.merge(feature02,fea01_user_cnt_sum,on='shop_id',how='left')
    feature02=pd.merge(feature02,fea01_rtn_cnt_sum,on='shop_id',how='left')
    feature02=pd.merge(feature02,fea01_offer_amt_sum,on='shop_id',how='left')
    feature02=pd.merge(feature02,fea01_offer_cnt_sum,on='shop_id',how='left')

    ##下单顾客数和订单总量的差值
    feature02['user_ord_rate']=feature02.user_cnt.astype('float')-feature02.ord_cnt.astype('float')
    # 销售总金额和退货总金额的比值
    feature02['rnt_sale_rate']=feature02.rtn_amt.astype('float')/feature02.sale_amt
    #优惠订单总数和订单总数的比值
    feature02['offer_ord_rate']=feature02.offer_cnt.astype('float')/feature02.ord_cnt
    #销售总金额和优惠总金额的比值
    feature02['sale_offer_rate']=feature02.offer_amt.astype('float')/feature02.sale_amt
    #销售总金额和下单顾客数的比值
    feature02['sale_user_rate']=feature02.sale_amt.astype('float')/feature02.user_cnt
    #销售总金额与订单量的比值
    feature02['sale_ord_rate']=feature02.sale_amt.astype('float')/feature02.ord_cnt
    #销售总金额和退货订单数的比值
    feature02['sale_rtn_rate']=feature02.sale_amt.astype('float')/feature02.rtn_cnt
    #优惠总金额和顾客下单数的比值
    feature02['offer_user_rate']=feature02.offer_amt.astype('float')/feature02.user_cnt
    #优惠总金额和订单数的比值
    feature02['offer_ord_rate']=feature02.offer_amt.astype('float')/feature02.ord_cnt
    #退订单数和退订金额的比值
    feature02['rtn_rtn_rate']=feature02.rtn_amt.astype('float')/feature02.rtn_cnt
    print(feature02.head())

    #十月分的订单

    t_order_data_limt1=t_order_data[t_order_data['ord_dt'].map(lambda x:True if '2016-10-01' <=str(x)<='2016-10-31'else False)]
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


    feature03=pd.merge(fea01_ord_cnt_sum,fea01_sale_amt_sum,on='shop_id')
    print(feature01.head())
    feature03=pd.merge(feature03,fea01_rtn_amt_sum,on='shop_id',how='left')
    feature03=pd.merge(feature03,fea01_user_cnt_sum,on='shop_id',how='left')
    feature03=pd.merge(feature03,fea01_rtn_cnt_sum,on='shop_id',how='left')
    feature03=pd.merge(feature03,fea01_offer_amt_sum,on='shop_id',how='left')
    feature03=pd.merge(feature03,fea01_offer_cnt_sum,on='shop_id',how='left')
    print(feature01.head())
    ##下单顾客数和订单总量的差值
    feature03['user_ord_rate']=feature03.user_cnt.astype('float')-feature03.ord_cnt.astype('float')
    # 销售总金额和退货总金额的比值
    feature03['rnt_sale_rate']=feature03.rtn_amt.astype('float')/feature03.sale_amt
    #优惠订单总数和订单总数的比值
    feature03['offer_ord_rate']=feature03.offer_cnt.astype('float')/feature03.ord_cnt
    #销售总金额和优惠总金额的比值
    feature03['sale_offer_rate']=feature03.offer_amt.astype('float')/feature03.sale_amt
    #销售总金额和下单顾客数的比值
    feature03['sale_user_rate']=feature03.sale_amt.astype('float')/feature03.user_cnt
    #销售总金额与订单量的比值
    feature03['sale_ord_rate']=feature03.sale_amt.astype('float')/feature03.ord_cnt
    #销售总金额和退货订单数的比值
    feature03['sale_rtn_rate']=feature03.sale_amt.astype('float')/feature03.rtn_cnt
    #优惠总金额和顾客下单数的比值
    feature03['offer_user_rate']=feature03.offer_amt.astype('float')/feature03.user_cnt
    #优惠总金额和订单数的比值
    feature03['offer_ord_rate']=feature03.offer_amt.astype('float')/feature03.ord_cnt
    #退订单数和退订金额的比值
    feature03['rtn_rtn_rate']=feature03.rtn_amt.astype('float')/feature03.rtn_cnt


    #11月的

    t_order_data_limt1=t_order_data[t_order_data['ord_dt'].map(lambda x:True if '2016-11-01' <=str(x)<='2016-11-30'else False)]
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


    feature04=pd.merge(fea01_ord_cnt_sum,fea01_sale_amt_sum,on='shop_id')
    print(feature01.head())
    feature04=pd.merge(feature04,fea01_rtn_amt_sum,on='shop_id',how='left')
    feature04=pd.merge(feature04,fea01_user_cnt_sum,on='shop_id',how='left')
    feature04=pd.merge(feature04,fea01_rtn_cnt_sum,on='shop_id',how='left')
    feature04=pd.merge(feature04,fea01_offer_amt_sum,on='shop_id',how='left')
    feature04=pd.merge(feature04,fea01_offer_cnt_sum,on='shop_id',how='left')
    print(feature01.head())
    ##下单顾客数和订单总量的差值
    feature04['user_ord_rate']=feature04.user_cnt.astype('float')-feature04.ord_cnt.astype('float')
    # 销售总金额和退货总金额的比值
    feature04['rnt_sale_rate']=feature04.rtn_amt.astype('float')/feature04.sale_amt
    #优惠订单总数和订单总数的比值
    feature04['offer_ord_rate']=feature04.offer_cnt.astype('float')/feature04.ord_cnt
    #销售总金额和优惠总金额的比值
    feature04['sale_offer_rate']=feature04.offer_amt.astype('float')/feature04.sale_amt
    #销售总金额和下单顾客数的比值
    feature04['sale_user_rate']=feature04.sale_amt.astype('float')/feature04.user_cnt
    #销售总金额与订单量的比值
    feature04['sale_ord_rate']=feature04.sale_amt.astype('float')/feature04.ord_cnt
    #销售总金额和退货订单数的比值
    feature04['sale_rtn_rate']=feature04.sale_amt.astype('float')/feature04.rtn_cnt
    #优惠总金额和顾客下单数的比值
    feature04['offer_user_rate']=feature04.offer_amt.astype('float')/feature04.user_cnt
    #优惠总金额和订单数的比值
    feature04['offer_ord_rate']=feature04.offer_amt.astype('float')/feature04.ord_cnt
    #退订单数和退订金额的比值
    feature04['rtn_rtn_rate']=feature04.rtn_amt.astype('float')/feature04.rtn_cnt
    #print(feature01.head())

    #12月的

    t_order_data_limt1=t_order_data[t_order_data['ord_dt'].map(lambda x:True if '2016-12-01' <=str(x)<='2016-12-31'else False)]
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


    feature05=pd.merge(fea01_ord_cnt_sum,fea01_sale_amt_sum,on='shop_id')
    print(feature01.head())
    feature05=pd.merge(feature05,fea01_rtn_amt_sum,on='shop_id',how='left')
    feature05=pd.merge(feature05,fea01_user_cnt_sum,on='shop_id',how='left')
    feature05=pd.merge(feature05,fea01_rtn_cnt_sum,on='shop_id',how='left')
    feature05=pd.merge(feature05,fea01_offer_amt_sum,on='shop_id',how='left')
    feature05=pd.merge(feature05,fea01_offer_cnt_sum,on='shop_id',how='left')
    #print(feature01.head())
    ##下单顾客数和订单总量的差值
    feature05['user_ord_rate']=feature05.user_cnt.astype('float')-feature05.ord_cnt.astype('float')
    # 销售总金额和退货总金额的比值
    feature05['rnt_sale_rate']=feature05.rtn_amt.astype('float')/feature05.sale_amt
    #优惠订单总数和订单总数的比值
    feature05['offer_ord_rate']=feature05.offer_cnt.astype('float')/feature05.ord_cnt
    #销售总金额和优惠总金额的比值
    feature05['sale_offer_rate']=feature05.offer_amt.astype('float')/feature05.sale_amt
    #销售总金额和下单顾客数的比值
    feature05['sale_user_rate']=feature05.sale_amt.astype('float')/feature05.user_cnt
    #销售总金额与订单量的比值
    feature05['sale_ord_rate']=feature05.sale_amt.astype('float')/feature05.ord_cnt
    #销售总金额和退货订单数的比值
    feature05['sale_rtn_rate']=feature05.sale_amt.astype('float')/feature05.rtn_cnt
    #优惠总金额和顾客下单数的比值
    feature05['offer_user_rate']=feature05.offer_amt.astype('float')/feature05.user_cnt
    #优惠总金额和订单数的比值
    feature05['offer_ord_rate']=feature05.offer_amt.astype('float')/feature05.ord_cnt
    #退订单数和退订金额的比值
    feature05['rtn_rtn_rate']=feature05.rtn_amt.astype('float')/feature05.rtn_cnt
    #print(feature01.head())



    #一月的订单
    t_order_data_limt1=t_order_data[t_order_data['ord_dt'].map(lambda x:True if '2017-01-01' <=str(x)<='2017-01-31'else False)]
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


    feature06=pd.merge(fea01_ord_cnt_sum,fea01_sale_amt_sum,on='shop_id')
    print(feature01.head())
    feature06=pd.merge(feature06,fea01_rtn_amt_sum,on='shop_id',how='left')
    feature06=pd.merge(feature06,fea01_user_cnt_sum,on='shop_id',how='left')
    feature06=pd.merge(feature06,fea01_rtn_cnt_sum,on='shop_id',how='left')
    feature06=pd.merge(feature06,fea01_offer_amt_sum,on='shop_id',how='left')
    feature06=pd.merge(feature06,fea01_offer_cnt_sum,on='shop_id',how='left')
   # print(feature01.head())
    ##下单顾客数和订单总量的差值
    feature06['user_ord_rate']=feature06.user_cnt.astype('float')-feature06.ord_cnt.astype('float')
    # 销售总金额和退货总金额的比值
    feature06['rnt_sale_rate']=feature06.rtn_amt.astype('float')/feature06.sale_amt
    #优惠订单总数和订单总数的比值
    feature06['offer_ord_rate']=feature06.offer_cnt.astype('float')/feature06.ord_cnt
    #销售总金额和优惠总金额的比值
    feature06['sale_offer_rate']=feature06.offer_amt.astype('float')/feature06.sale_amt
    #销售总金额和下单顾客数的比值
    feature06['sale_user_rate']=feature06.sale_amt.astype('float')/feature06.user_cnt
    #销售总金额与订单量的比值
    feature06['sale_ord_rate']=feature06.sale_amt.astype('float')/feature06.ord_cnt
    #销售总金额和退货订单数的比值
    feature06['sale_rtn_rate']=feature06.sale_amt.astype('float')/feature06.rtn_cnt
    #优惠总金额和顾客下单数的比值
    feature06['offer_user_rate']=feature06.offer_amt.astype('float')/feature06.user_cnt
    #优惠总金额和订单数的比值
    feature06['offer_ord_rate']=feature06.offer_amt.astype('float')/feature06.ord_cnt
    #退订单数和退订金额的比值
    feature06['rtn_rtn_rate']=feature06.rtn_amt.astype('float')/feature06.rtn_cnt
    #print(feature01.head())
    feature01=feature01.drop_duplicates(['shop_id'])  #去重复
    feature02=feature02.drop_duplicates(['shop_id'])  #去重复
    feature03=feature03.drop_duplicates(['shop_id'])  #去重复
    feature04=feature04.drop_duplicates(['shop_id'])  #去重复
    feature05=feature05.drop_duplicates(['shop_id'])  #去重复
    feature06=feature06.drop_duplicates(['shop_id'])  #去重复
    feature07=pd.concat([feature01,feature02,feature03,feature04,feature05,feature06],ignore_index=True)

    feature07.to_csv('../data/pa/ff.csv')


    #8月店铺评论
    #获得店铺评论在2016-8到2017-3之间
    t_comment_data_limt1=t_comment_data[t_comment_data['create_dt'].map(lambda x:True if '2016-08-01' <=str(x)<='2017-03-31'else False)]

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