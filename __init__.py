#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import pandas as pd
if __name__=='__main__':
     # t_product_data=pd.read_csv('./data/order.csv')
     #
     # t_product_data_limt1=t_product_data[t_product_data['on_dt'].map(lambda x:True if str(x)<='2017-03-31'else False)]
     # print(t_product_data_limt1.head())
     # t1=t_product_data_limt1.groupby(['shop_id','cate'])['on_dt'].agg('max').reset_index()
     # # print(t1.head())
     # shop=pd.read_csv('xgb_feature_score.csv')
     #
     # import matplotlib.pylab as plt
     # feat_imp=shop['score']
     # feat_imp.plot(kind='bar', title='Feature Importances')
     #
     # plt.ylabel('Feature Importance Score')
     # plt.show()
     #
     # s=pd.read_csv('./data/pa/t022.csv')
     # s.to_csv('./data/pa/t033',index=None,header=None)
     # shop=pd.read_csv('./data/t_sales_sum.csv')
     # print(len(set(s.shop_id.tolist())))
     s=pd.read_csv('./and/特征重要性.csv')
     s['f']=sorted(s['fscore'])
     print(s)

     #
     # index=shop.drop_duplicates('shop_id')['shop_id']
     # ls=list(index)
     #
     # all_index=pd.DataFrame(ls*8)
     # all_index.columns=['shop_id']
     # shop.set_index('shop_id')
     # all_index.set_index('shop_id')
     # fin=pd.concat([all_index,shop],axis=1)
     #
     #
     #
     # fin.groupby('shop_id').apply(lambda x:x.fillna(x.mean),axis=1)
     # fin.to_csv('./data/t_sales_sum3.csv')
     # print(len(shop[shop.shop_id==1490]))





