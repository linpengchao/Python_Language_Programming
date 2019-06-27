# 运算平均值、方差、中位数
# if __name__ == '__main__':
#     lst = []
#     temp = input('input data, quit with ENTER')
#     while temp != '':
#         lst.append(eval(temp))
#         temp = input('input data, quit with ENTER')
#     lst.sort()
#     print(lst)
#
#     ave = sum(lst) / len(lst)
#     print('average:{:.1f}'.format(ave))
#
#     dev = 0
#     for i in range(len(lst)):
#         dev += (lst[i]-ave) ** 2
#     dev /= len(lst)
#     print('dev:{:.1f}'.format(dev))
#
#     if len(lst) % 2 == 0:
#         mid = (lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1]) / 2
#     else:
#         mid = lst[int(len(lst) / 2)]
#     print('mid:{:}'.format(mid))


# # 统计词频 英文
#
#
# def ActInputText():
#     txt = open('Hamlet.txt', 'r').read()
#     txt = txt.lower()
#     for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
#         txt = txt.replace(ch, " ")
#         return txt
#
#
# if __name__ == '__main__':
#     hamletTxt = ActInputText()
#     hamletWords = hamletTxt.split()
#     counts = {}
#     for word in hamletWords:
#         counts[word] = counts.get(word, 0) + 1
#     items = list(counts.items())
#     items.sort(key=lambda x:x[1], reverse=True)
#     for i in range(20):
#         word, count = items[i]
#         print('{0:<20}{1:>5}'.format(word, count))

# # 中文统计词频 jieba库
# import jieba
#
#
# if __name__ == '__main__':
#     txt = open('三国演义.txt', 'r', encoding='utf-8').read()
#     words = jieba.lcut(txt)
#     count = dict()
#     for word in words:
#         if len(word) <= 1:
#             continue
#         else:
#             count[word] = count.get(word, 0) + 1
#     lst = list(count.items())
#     lst.sort(key=lambda x: x[1], reverse=True)
#     # print(lst)
#     dic = dict(lst)
#     print(dic)


# # 练习一
# # 请在...补充一行或多行代码
# # CalStatisticsV1.py
# def getNum():  # 获取用户不定长度的输入
#     list = []
#     temp = input()
#     while temp != "":
#         list.append(eval(temp))
#         temp = input()
#     return list
#
#
# def mean(numbers):  # 计算平均值
#     count = 0
#     for item in numbers:
#         count += item
#     return count / len(numbers)
#
#
# def dev(numbers, mean):  # 计算标准差
#     sdev = 0.0
#     for num in numbers:
#         sdev = sdev + (num - mean) ** 2
#     return pow(sdev / (len(numbers) - 1), 0.5)
#
#
# def median(numbers):  # 计算中位数
#     numbers.sort()
#     if len(numbers) % 2 == 0:
#         temp = (numbers[int(len(numbers)/2)] + numbers[int(len(numbers)/2) - 1])/2
#     else:
#         temp = numbers[int(len(numbers)/2)]
#     return temp
#
#
# n = getNum()  # 主体函数
# m = mean(n)
# print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m, dev(n, m), median(n)))


"""
英文文本：hamlet‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬.txt，参考附件‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

请统计hamlet.txt文件中出现的英文单词情况，统计并输出出现最多的10个单词，注意：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬

(1) 单词不区分大小写，即单词的大小写或组合形式一样；
(2) 请在文本中剔除如下特殊符号：!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~
(3) 输出10个单词，每个单词一行；
(4) 输出单词为小写形式。
"""
#
#
# # 获取文本，转为全部小写，去掉特殊符号
# def get_text():
#     txt = open("hamlet.txt", "r").read()
#     txt = txt.lower()
#     for item in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
#         txt = txt.replace(item, ' ')
#     txt_list = list(txt.split())
#     # print(txt_list)
#     return txt_list
#
#
# def take_second(x):
#     return x[1]
#
#
# def count_words():
#     txt = get_text()
#     count = {}
#     for word in txt:
#         count[word] = count.get(word, 0) + 1
#     lst = list(count.items())
#     lst.sort(key=take_second, reverse=True)
#     # print(lst)
#     return lst
#
#
# def print_words():
#     lst = count_words()
#     for i in range(10):
#         print(lst[i][0])
#
#
# if __name__ == '__main__':
#     print_words()


# 模板字符串中包含重复人名，输出模板字符串共有多少个独特人名，数量。
#
# s = '''双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖
#        杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙
#        金轮法王 小龙女 杨过 慕容复 梅超风 李莫愁 洪七公 张无忌 梅超风 杨逍
#        鳌拜 岳不群 黄药师 黄蓉 段誉 金轮法王 忽必烈 忽必烈 张三丰 乔峰 乔峰
#        阿紫 乔峰 金轮法王 袁冠南 张无忌 郭襄 黄蓉 李莫愁 赵敏 赵敏 郭芙 张三丰
#        乔峰 赵敏 梅超风 双儿 鳌拜 陈家洛 袁冠南 郭芙 郭芙 杨逍 赵敏 金轮法王
#        忽必烈 慕容复 张三丰 杨逍 令狐冲 黄药师 袁冠南 杨逍 完颜洪烈 殷天正
#        李莫愁 阿紫 逍遥子 乔峰 逍遥子 完颜洪烈 郭芙 杨逍 张无忌 杨过 慕容复
#        逍遥子 虚竹 双儿 乔峰 郭芙 黄蓉 李莫愁 陈家洛 杨过 忽必烈 鳌拜 王语嫣
#        洪七公 韦小宝 阿朱 梅超风 段誉 岳灵珊 完颜洪烈 乔峰 段誉 杨过 杨过 慕容复
#        黄蓉 杨过 阿紫 杨逍 张三丰 张三丰 赵敏 张三丰 杨逍 黄蓉 金轮法王 郭襄
#        张三丰 令狐冲 郭芙 韦小宝 黄药师 阿紫 韦小宝 金轮法王 杨逍 令狐冲 阿紫
#        洪七公 袁冠南 双儿 郭靖 鳌拜 谢逊 阿紫 郭襄 梅超风 张无忌 段誉 忽必烈
#        完颜洪烈 双儿 逍遥子 谢逊 完颜洪烈 殷天正 金轮法王 张三丰 双儿 郭襄 阿朱
#        郭襄 双儿 李莫愁 郭襄 忽必烈 金轮法王 张无忌 鳌拜 忽必烈 郭襄 令狐冲
#        谢逊 梅超风 殷天正 段誉 袁冠南 张三丰 王语嫣 阿紫 谢逊 杨过 郭靖 黄蓉
#        双儿 灭绝师太 段誉 张无忌 陈家洛 黄蓉 鳌拜 黄药师 逍遥子 忽必烈 赵敏
#        逍遥子 完颜洪烈 金轮法王 双儿 鳌拜 洪七公 郭芙 郭襄'''
#
#
# if __name__ == '__main__':
#     s = s.replace('\n', '')
#     s = s.replace('       ', '')
#     lsta = list(s.split(' '))
#     seta = set(lsta)
#     # print(seta)
#     print(len(seta))


# # 字典翻转输出
# def get_dict():
#     dic = eval(input())
#     # print(dict)
#     if type(dic) != dict:
#         print('输入错误')
#         return 'error'
#     return dic
#
#
# def reverse_dict(dic):
#     dict_new = dict()
#     for item in dic:
#         dict_new[dic[item]] = item
#     # print(dic)
#     print(dict_new)
#
#
# dic = get_dict()
# if dic != 'error':
#     reverse_dict(dic)


# # 《沉默的羔羊》之最多的单词
# # 分词后输出长度大于2且最多的单词，如果多个单词出现频率一致，按照unicode排序后最大
# # 的单词
# import jieba
#
#
# def take_second(x):
#     return x[1]
#
#
# def get_text():
#     txt = open('沉默的羔羊.txt', 'r', encoding='utf-8').read()
#     for item in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~\n':
#         txt = txt.replace(item, ' ')
#     words = jieba.lcut(txt)
#     # print(words)
#     dic = dict()
#     for item in words:
#         if len(item) < 2:
#             continue
#         else:
#             dic[item] = dic.get(item, 0) + 1
#     result = list(dic.items())
#     # print(result)
#     result.sort(key=take_second, reverse=True)
#     # print(result)
#     print(result[0][0])
#
#
# get_text()

#
# # 获得用户输入的整数N，输出N汇总出现不同数字的和。
# # 如输入123123123，输出6
# num = input()
# set_num = set(num)
# result = 0
# for item in set_num:
#     result += eval(item)
# print(result)

# 模板给出了一个字符串，包含了重复的人名。输出出现最多的人名
s = '''双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖 
       杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙 
       金轮法王 小龙女 杨过 慕容复 梅超风 李莫愁 洪七公 张无忌 梅超风 杨逍 
       鳌拜 岳不群 黄药师 黄蓉 段誉 金轮法王 忽必烈 忽必烈 张三丰 乔峰 乔峰 
       阿紫 乔峰 金轮法王 袁冠南 张无忌 郭襄 黄蓉 李莫愁 赵敏 赵敏 郭芙 张三丰 
       乔峰 赵敏 梅超风 双儿 鳌拜 陈家洛 袁冠南 郭芙 郭芙 杨逍 赵敏 金轮法王 
       忽必烈 慕容复 张三丰 赵敏 杨逍 令狐冲 黄药师 袁冠南 杨逍 完颜洪烈 殷天正 
       李莫愁 阿紫 逍遥子 乔峰 逍遥子 完颜洪烈 郭芙 杨逍 张无忌 杨过 慕容复 
       逍遥子 虚竹 双儿 乔峰 郭芙 黄蓉 李莫愁 陈家洛 杨过 忽必烈 鳌拜 王语嫣 
       洪七公 韦小宝 阿朱 梅超风 段誉 岳灵珊 完颜洪烈 乔峰 段誉 杨过 杨过 慕容复 
       黄蓉 杨过 阿紫 杨逍 张三丰 张三丰 赵敏 张三丰 杨逍 黄蓉 金轮法王 郭襄 
       张三丰 令狐冲 赵敏 郭芙 韦小宝 黄药师 阿紫 韦小宝 金轮法王 杨逍 令狐冲 阿紫 
       洪七公 袁冠南 双儿 郭靖 鳌拜 谢逊 阿紫 郭襄 梅超风 张无忌 段誉 忽必烈 
       完颜洪烈 双儿 逍遥子 谢逊 完颜洪烈 殷天正 金轮法王 张三丰 双儿 郭襄 阿朱 
       郭襄 双儿 李莫愁 郭襄 忽必烈 金轮法王 张无忌 鳌拜 忽必烈 郭襄 令狐冲 
       谢逊 梅超风 殷天正 段誉 袁冠南 张三丰 王语嫣 阿紫 谢逊 杨过 郭靖 黄蓉 
       双儿 灭绝师太 段誉 张无忌 陈家洛 黄蓉 鳌拜 黄药师 逍遥子 忽必烈 赵敏 
       逍遥子 完颜洪烈 金轮法王 双儿 鳌拜 洪七公 郭芙 郭襄 赵敏'''

s = s.replace('       ', '')
s = s.replace('\n', '')
s = s.split(' ')
dic = {}
for item in s:
    dic[item] = dic.get(item, 0) + 1
res = list(dic.items())
res.sort(key=lambda x: x[1], reverse=True)
print(res[0][0])



