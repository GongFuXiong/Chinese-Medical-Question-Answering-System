#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import pandas as pd #导入数据
import numpy as np #矩阵计算
import matplotlib.pyplot as plt
from math import sin as sin
from math import cos as cos
from math import exp as exp
from pandas import Series,DataFrame
import csv
import sklearn.preprocessing as preprocessing			#归一化
import operator
from os import listdir
from numpy import *
import warnings		# gensim导入问题
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import word2vec
import gensim
import logging
import jieba
import re
import multiprocessing


# header表示文件第0行为列索引,index_col为行索引
data_train = pd.read_csv(u"F:/answers.csv", header=0,index_col=None, encoding='gb18030')
data_train1 = pd.read_csv(u"F:/questions.csv", header=0,index_col=None, encoding='gb18030')
print(data_train1)

# **************
data_train = data_train['content']
data_train1 = data_train1['content']
data_train = list(data_train)+list(data_train1)  #合并两个列表
# print(data_train)


def clean_email_text(text):
    # text = text.replace('\n'," ") #新行，我们是不需要的
    # text = re.sub(r"-", " ", text) #把 "-" 的两个单词，分开。（比如：july-edu ==> july edu）
    # text = re.sub(r"\d+/\d+/\d+", "", text) #日期，对主体模型没什么意义
    # text = re.sub(r"[0-2]?[0-9]:[0-6][0-9]", "", text) #时间，没意义
    # text = re.sub(r"[\w]+@[\.\w]+", "", text) #邮件地址，没意义
    # text = re.sub(r"/[a-zA-Z]*[:\//\]*[A-Za-z0-9\-_]+\.+[A-Za-z0-9\.\/%&=\?\-_]+/i", "", text) #网址，没意义
    # pure_text = ''
    text = Series(text).replace('\t', "")  # 去掉空格
    text = [v for v in text if not str(v).isdigit()]
    return text

# data_train = clean_email_text(data_train)
# print(data_train)

# dataList = []
# for rowStr in data_train:
# 	rowStr = list(rowStr)
# 	tmpList = []
# 	for ele in rowStr:
# 		tmpList.append(ele)
# 		tmpList.append(' ')
# 	dataList.append(tmpList)

# print(dataList)
# f=open('F:/1.txt','w',encoding='utf-8')
# for i in dataList:
#     k=' '.join([str(j) for j in i])
#     f.write(k+"\n")
# f.close()

# ******************
# word2vec模型
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# sentences = word2vec.Text8Corpus(u"F:/1.txt")  # 加载语料,分词后的文件，词之间以空格隔开
#
# model = word2vec.Word2Vec(sentences, sg=1, size=100,  window=5,  min_count=1,  negative=3, sample=0.001, hs=1, workers=4)  # 默认window=5,min_count=1，size为词向量的维度

# model.save(u'F:/model.txt')   # 模型保存路径,以便重用
model = word2vec.Word2Vec.load(u'F:/model.txt')  # 对应的加载方式

# print(model)
# print(model.similarity('你', '嘛'))
# print(model['我'])


word = u"什么是白癜风"
# print(model[word])




