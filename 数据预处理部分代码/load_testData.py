from collections import defaultdict
import csv as csv
import codecs
import random
import pandas as pd

get_answers = pd.read_csv('F:/answers.csv', encoding='gb18030')  # 读取answers的CSV的表格数据
# get_questions = pd.read_csv('F:/questions.csv', encoding='gb18030')  # 读取questions的CSV的表格数据
ans_content1 = get_answers['ans_content']

def get_question():
    data = []
    with open('F:/questions.csv', 'r', newline='', encoding='gb18030') as f:
        for line in f.readlines():
            ru = line.strip().replace(' ', '')
            data.append(ru)
    return data

def get_answer():
    data = []
    with open('F:/answers.csv', 'r', newline='', encoding='gb18030') as f:
        for line in f.readlines():
            ru = line.strip().replace(' ', '')  # 去掉空格
            data.append(ru)
    return data

# def question_get_data(filename):
# 	question_list = []
# 	with codecs.open(filename, mode="r", encoding="gb18030") as rf:
# 			reader = csv.reader(rf)
# 			# rows=[]
# 			for row in reader:
# 				question_tmp = {}
# 				# print(row[0])
# 				question_tmp['que_id'] = row[0]
# 				question_tmp['ques_content'] = row[1]
# 				question_list.append(question_tmp)
# 				# rows.append(row)
# 	return question_list

def get_data(filename,id,name):
    with codecs.open(filename, mode="r", encoding="gb18030") as rf:
        reader = csv.reader(rf)
        rows=[]
        question_tmp = {}
        for row in reader:
            question_tmp[row[id]] = row[name]  # 直接变成一个字典对
    return question_tmp

question_list = get_data(u'F:/questions.csv',0,1)
answer_list = get_data(u'F:/answers.csv',1,2)
# print(answer_list[10]['ans_content'])
# print(data)
# question_list = []
# for tmp in data[1:]:
#     print(tmp)
#     question_tmp = {}
#     question_tmp['que_id'] = tmp[1]
#     question_tmp['ques_content'] = tmp[2]
#     # print(question_tmp)
#     question_list.append(question_tmp)
# print(question_list)


#取字典
# data2 = get_answers
# answer_list = []
# for tmp in data2[1:]:
#     answer_tmp = {}
#     answer_tmp['que_id'] = tmp.split(',')[0]
#     answer_tmp['ans_content'] = tmp.split(',')[1]
#     # print(answer_tmp)
#     answer_list.append(answer_tmp)

def randomExtra(text):
	placeNum = [random.randint(0, len(text)) for _ in range(5)]
	return text[placeNum]
# cadAnsw = randomExtra(ans_content)


header=['lable','qid','ques_content','ans_content']
lable = []
qid = []
ques_content=[]
ans_content=[]

# final_result = []
# for tmp in question_list:
# 	count = 0
# 	right_answer = []   # 临时变量
# 	error_answer = []
# 	if (tmp in answer_list.keys()):
# 		lable.append(1)
# 		qid.append(tmp)
# 		ques_content.append(question_list[tmp])
# 		ans_content.append(answer_list[tmp])
# 		# final_result.append(tmp_result)
#
# 		# 随机抽取错误答案样本
# 		# error_list = random.sample(error_answer, count*5)
# 		error_list = randomExtra(ans_content1)
# 		for tmpe in error_list:
# 			# tmp_result = []
# 			lable.append(0)
# 			qid.append(tmp)
# 			ques_content.append(question_list[tmp])
# 			ans_content.append(tmpe)



    # for tmpa in answer_list:
    #     if tmp['que_id'] == tmpa['que_id']:
    #         right_answer.append(tmpa['ans_content'])
    #         count += 1
    #         break
        # else:
        #     error_answer.append(tmpa['ans_content'])
    #没有答案跳过
    # if count != 0:
    #     #正确答案
    #     # for i in range(count):
    #         # tmp_result = []
    #         lable.append(1)
    #         qid.append(tmp['que_id'])
    #         ques_content.append(tmp['ques_content'])
    #         ans_content.append(right_answer[0])
    #         # final_result.append(tmp_result)
	#
    #     #随机抽取错误答案样本
    #     # error_list = random.sample(error_answer, count*5)
    #         error_list = randomExtra(ans_content1)
    #         for tmpe in error_list:
    #            # tmp_result = []
    #            lable.append(0)
    #            qid.append(tmp['que_id'])
    #            ques_content.append(tmp['ques_content'])
    #            ans_content.append(tmpe)
    #         # final_result.append(tmp_result)


# with open("F:/testFile.csv", "w", newline='', encoding="gb18030") as csvfile:
#     writer = csv.writer(csvfile)
#
#     #先写入columns_name
#     writer.writerow(["lable", "que_id", "ques_content", "ans_content"])
#     #写入多行用writerows
#     writer.writerows(zip(lable,qid,ques_content,ans_content))

"""
随机生成Valid验证集
"""
def get_data1(filename,num):
	with codecs.open(filename, mode="r", encoding="gb18030") as rf:
		reader = csv.reader(rf)
		rows=[]
		for row in reader:
			rows.append(row)
		# print(rows)
		placeNum = [random.randint(0, len(rows)) for _ in range(num)]
		data=[]
		for i in placeNum:
			lable.append(rows[i][0])
			qid.append(rows[i][1])
			ques_content.append(rows[i][2])
			ans_content.append(rows[i][3])
	return lable,qid,ques_content,ans_content
# lable,qid,ques_content,ans_content = get_data1(u'F:/testFile.csv',5000)
# print(valid_data)


# with open("F:/valid_File.csv", "w", newline='', encoding="gb18030") as csvfile:
#     writer = csv.writer(csvfile)
#
#     #先写入columns_name
#     writer.writerow(["lable", "que_id", "ques_content", "ans_content"])
#     #写入多行用writerows
#     writer.writerows(zip(lable,qid,ques_content,ans_content))
