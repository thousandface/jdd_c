#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
import pandas as pd
import csv
import numpy as np

if __name__=='__main__':
    xgb1=pd.read_csv('./data/pa/t01.csv')
    xgb2=pd.read_csv('./data/pa/t02.csv')
    xgb3=pd.read_csv('./data/pa/t03.csv')
    sum1=pd.merge(xgb1,xgb2,on='shop_id',how='left')
    sum1=pd.merge(sum1,xgb3,on='shop_id',how='left')
    print(sum1.head())
    first=sum1[['shop_id']]
    first['hat']=sum1.hat_x+sum1.hat_y+sum1.hat




    first.to_csv('./data/pa/T.csv',index=None,header=None)