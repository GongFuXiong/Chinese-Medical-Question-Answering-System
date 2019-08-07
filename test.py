import pandas as pd
import csv as csv
import numpy as np
import codecs
import random
import sys
import linecache

da = pd.read_csv('F:/answers.csv', encoding='gb18030')  # 读取answers的CSV的表格数据
dq = pd.read_csv('F:/questions.csv', encoding='gb18030')  # 读取questions的CSV的表格数据
# data = pd.merge(df, dd, on='que_id', how='left')  # pandas处理数据 找出索引关键字
# data = data[[ 'que_id', 'ques_content', 'ans_content']]
# # -------------
# # pandas写入表格数据
# # -------------
# data.to_csv(r'data.csv', encoding='gb18030')

ans_content1 = da['ans_content']
ques_content1 = dq['ques_content']
def randomExtra(text):
	placeNum = [random.randint(0, len(text)) for _ in range(5)]
	return text[placeNum]
cadAnsw = randomExtra(ans_content1)
# print(cadAnsw)


csvfile = open('F:/testFile.csv', 'wt' , newline='',encoding="gb18030")
writer=csv.writer(csvfile, delimiter=",")
header=['lable','qid','ques_content','ans_content']
lable = []
qid = []
ques_content=[]
ques_content=[]

for ele in ques_content:
	lable.append(0)
	qid.append()



# data_train1 = dq['content']
# with codecs.open(filename, mode="r", encoding="gb18030") as rf:
# 	reader = csv.reader(rf)
# 	for row in reader: