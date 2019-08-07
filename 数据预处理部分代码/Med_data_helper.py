from __future__ import print_function
#!/usr/bin/env python3.4
import random
from operator import itemgetter
import codecs
from pandas import Series,DataFrame
import logging
import pandas as pd
import numpy as np
import os,re
import json
import csv as csv
from collections import defaultdict
# define a logger
logging.basicConfig(format="%(message)s", level=logging.INFO)
from gensim.models import word2vec



def readTxt():                      #一个个字列表
	filename = 'F:/1.txt'  # txt文件和当前脚本在同一目录下，所以不用写具体路径
	pos = []
	with open(filename, encoding='utf-8') as file_to_read:
		while True:
			lines = file_to_read.readline()  # 整行读取数据
			if not lines:
				break
				pass
			for i in lines.split():  # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
				pos.append(i)  # 添加新读取的数据
				pass
	pos = list(set(pos))         #set去重
	return pos
# pos = readTxt()
# print(pos)

def creatDict():
	wordCounr = readTxt()
	wordDict = {}
	model = word2vec.Word2Vec.load(u'F:/model.txt')  # 对应的加载方式,加载训练好的字向量模型
	for word in wordCounr:
		wordDict[word] = model[word]

	return wordDict
#wordList= creatDict()
# print(wordList)

"""
#  生成一列字和字向量文件
"""
# with open('F:/dic4.txt', 'w', encoding='utf-8') as file_to_write:
# 	for key in wordList:
# 		aWordList=str(wordList[key])
# 		aWordList= aWordList.strip('[]')
# 		aWordList= aWordList.replace("\n", "")
# 		# print(aWordList)
# 		# aWordList=aWordList.replace('\\r\n')
# 		file_to_write.write("%s %s\n"%(key, aWordList))
# 	file_to_write.close()



# with open('F:/dic4.txt', 'w', encoding='utf-8') as file_to_write:
# 	for key in wordList:
# 		file_to_write.write("%s,%s\n"%(key, wordList[key]))
# 	file_to_write.close()


# s = str(wordList)
# f = open('F:/dic1.txt','w',encoding='utf-8')
# f.writelines(s)
# f.close()

# def writeDict(data):
# 	with open("F:/data.txt", "w") as f:
# 		f.write(json.dumps(data, ensure_ascii=False)) # dic= creatDict()
# writeDict(wordList)

# output = open('F:/dic1.txt','w',encoding='utf-8')
# for i in dic:
# 	print(i,dic[i])
# 	write_str = str(i) + ' ' + float(dic[i]) + '\n'
# 	output.write(write_str)
# output.close()

# dicfile=open('F:/dic.txt','w',encoding='gb18030')
# for key in dic:
#     for innerkey in dic[key]:
#         print('{0:<10}{1:<10}'.format(key,innerkey),file=dicfile)
# dicfile.close()

#测试
# a=wordList['我']
# a=a.reshape(1,100)
# print(a.shape[1])
# print(a)
# data2=[[1,2,3]]
# arr2=np.array(data2)
# print(arr2.shape)
# for key in wordList:
# 	print(str(wordList[key]))
# 	break;
# jsObj = json.dumps(wordList)
# fileObject = open('F:/jsonFile.json', 'w')
# fileObject.write(jsObj)
# fileObject.close()


#去字向量中空格
def dealSpace(oneList):
	tempList=[]
	for one in oneList:
		if(len(one.strip())>0):
			tempList.append(one)
	return tempList


def load_embedding1(wordList, embedding_size):

	embeddings = []
	word2idx = defaultdict(list)
	idx2word = defaultdict(list)
	idx = 0
	for key  in wordList:
		word2idx[key] = len(word2idx)
		idx2word[len(word2idx)] = key
		embeddings.append(wordList[key])


	# p1 = r","#这是我们写的正则表达式规则，你现在可以不理解啥意思
	# pattern1 = re.compile(p1)#我们在编译这段正则表达式
	# matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
# 新元素的下标等于当前的元素数量，下标和字向量的转换，字向量直接以数组存起来了，以后你的文字输入，要转换成字向量。

	logging.info("load embedding finish!")
	return embeddings, word2idx, idx2word
# embeddings, word2idx, idx2word = load_embedding(wordList,100)
# #embeddings, word2idx, idx2word = load_embedding(u'F:/dic2.txt',100)
# # print(embeddings)
# # print(word2idx)
# # print(idx2word)
# print(len(word2idx) )




def load_embedding(filename, embedding_size):   # 每个句子做等长切割，然后再做索引
    """
    load embedding
    """
    embeddings = []
    word2idx = defaultdict(list)
    idx2word = defaultdict(list)
    print(type(word2idx))
    idx = 0
    with codecs.open(filename, mode="r", encoding="utf-8") as rf:
        try:
            for line in rf.readlines():
                idx += 1
                arr = line.split(" ")
                # print("----"*20)
                arr= dealSpace(arr)   #去掉空格
                # print(len(a))
                # print(a)
                if len(arr) != (embedding_size + 1):       #一共101行
                    logging.error("embedding error, index is:%s"%(idx))
                    continue
                embedding = [float(val) for val in arr[1 : -1]]
# 新元素的下标等于当前的元素数量，下标和字向量的转换，字向量直接以数组存起来了，以后你的文字输入，要转换成字向量。
                word2idx[arr[0]] = len(word2idx)
                idx2word[len(word2idx)] = arr[0]
                embeddings.append(embedding)
        except Exception as e:
            logging.error("load embedding Exception,", e)
        finally:
            rf.close()

    logging.info("load embedding finish!")
    return embeddings, word2idx, idx2word
# embeddings, word2idx, idx2word = load_embedding(u'F:/dic4.txt',100)
# print(embeddings)
# print(word2idx)
# print(idx2word)

def gene_trainFile():
	da = pd.read_csv('F:/answers.csv', encoding='gb18030')  # 读取answers的CSV的表格数据
	dq = pd.read_csv('F:/questions.csv', encoding='gb18030')  # 读取questions的CSV的表格数据

	train_data = pd.merge(da, dq, on='que_id', how='left')  # pandas处理数据 找出索引关键字
	train_data = train_data[[ 'que_id', 'ques_content', 'ans_content']]
	# pandas写入表格数据
	train_data.to_csv(r'F:/train_file.csv', encoding='gb18030')

def sent_to_idx(sent, word2idx, sequence_len):
	"""
	变换句子为一个索引列表
	"""
	# dataList = []
	# for rowStr in data_train:
	# 	rowStr = list(rowStr)
	# 	tmpList = []
	# 	for ele in rowStr:
	# 		tmpList.append(ele)
	# 		tmpList.append(' ')
	# 	dataList.append(tmpList)
	# sent=str(sent)
	sent = Series(sent).replace('\000', "")  # 去掉空格
	sent = [v for v in sent if not str(v).isdigit()]
	sent=list(sent)
	sent=str(sent)
	unknown_id = word2idx.get("UNKNOWN", 0)#get返回key值，不然返回0

	if len(sent) < sequence_len+1:
		sent2idx = [word2idx.get(word, unknown_id) for word in sent[:sequence_len]]  # 得到句子切割之后,得到字id的列表
		for i in range(sequence_len-len(sent)):
			sent2idx.append(0)
		# print(sent2idx)
	else:
		sent2idx = [word2idx.get(word, unknown_id) for word in sent[:sequence_len]]#得到句子切割之后,得到字id的列表
	return sent2idx

#filename格式 1 qid q a+，一行四个
def load_train_data(filename, word2idx, sequence_len):
	"""
	生成train数据
	"""
	ori_quests, cand_quests = [], []
	with codecs.open(filename, mode="r", encoding="gb18030") as rf:
			reader = csv.reader(rf)
			for row in reader:
				# print('********'*20)
				# print(len(row))
				arr = row
				# arr = dealSpace(arr)  # 去掉空格
				# print(arr[0])
				#
				if len(arr) != 4:
					# logging.error("invalid data:%s"%(line))
					continue
				arr[2]=dealSpace(arr[2])
				arr[3] = dealSpace(arr[3])
				ori_quest = sent_to_idx(arr[2], word2idx, sequence_len)#原始答案为第2个
				cand_quest = sent_to_idx(arr[3], word2idx, sequence_len)#匹配答案为第3个

				ori_quests.append(ori_quest)
				cand_quests.append(cand_quest)

	logging.info("load train data finish!")
	return ori_quests, cand_quests
# ori_quests, cand_quests = load_train_data(u'F:/train_file.csv',word2idx,30)
# print(ori_quests)
# print(cand_quests)


def create_valid(data, proportion=0.1): #判断数据是否是有效并且对数据按比例做洗牌
    if data is None:
        logging.error("data is none")
        os._exit(1)
    data_len = len(data)
    shuffle_idx = np.random.permutation(np.arange(data_len))
    data = np.array(data)[shuffle_idx]
    seperate_idx = int(data_len * (1 - proportion))
    return data[:seperate_idx], data[seperate_idx:]

'''
filename类型：是否为正确答案lable(正确为1错误为0)、
result为qid(一个qid可以有多个候选结果，测试的时候取第一个作为答案)
第三列为问题语句
第四列为随机错误和正确语句（有一个正确答案就行）
'''
def load_test_data(filename, word2idx, sequence_len):
	"""
	生成test数据
	"""
	ori_quests, cand_quests, labels, results = [], [], [], []
	with codecs.open(filename, mode="r", encoding="gb18030") as rf:
			reader = csv.reader(rf)
			num = 0
			for row in reader:
				num += 1
				if num != 1:  # 去掉第一行的str
					# print(row)
					arr = row
					if len(arr) != 4:
						# logging.error("invalid data:%s"%(row))
						continue
					ori_quest = sent_to_idx(arr[2], word2idx, sequence_len)
					cand_quest = sent_to_idx(arr[3], word2idx, sequence_len)
					# print(arr[1])
					label = int(arr[0])
					result = int(arr[1])

					ori_quests.append(ori_quest)
					cand_quests.append(cand_quest)
					labels.append(label)
					results.append(result)

	logging.info("load test data finish!")
	return ori_quests, cand_quests, labels, results
# ori_quests, cand_quests, labels, results = load_test_data(u'F:/testFile.csv',word2idx,30)
# print(ori_quests)
# print(cand_quests)
# print(labels)
# print(results)


def batch_iter(ori_quests, cand_quests, batch_size, epoches, is_valid=False):
    """
    一定批量的方法迭代前面的过程，batch_iter里，有随机取的a-代码
    """
    data_len = len(ori_quests)
    batch_num = int(data_len / batch_size)
    ori_quests = np.array(ori_quests)
    cand_quests = np.array(cand_quests)

    for epoch in range(epoches):
        if is_valid is not True:
            shuffle_idx = np.random.permutation(np.arange(batch_num * batch_size))
            ori_quests = np.array(ori_quests)[shuffle_idx]
            cand_quests = np.array(cand_quests)[shuffle_idx]
        for batch in range(batch_num):
            start_idx = batch * batch_size
            end_idx = min((batch + 1) * batch_size, data_len)
            act_batch_size = end_idx - start_idx

            # get negative questions
            if is_valid:
                neg_quests = cand_quests[start_idx : end_idx]
            else:
                randi_list = []
                while len(randi_list) != act_batch_size:
                    [randi_list.append(idx) for idx in np.random.randint(0, data_len, 5 * act_batch_size) if start_idx < idx < end_idx and len(randi_list) < act_batch_size]		# 随机选择5倍的负样本
                neg_quests = [cand_quests[idx] for idx in randi_list]

            yield (ori_quests[start_idx : end_idx], cand_quests[start_idx : end_idx], neg_quests)







