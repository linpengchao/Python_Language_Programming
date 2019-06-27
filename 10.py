# # 获得用户输入，去掉其中全部空格，将其他字符按收入顺序打印输出
#
#
# a = input()
# a = a.replace(' ', '')
# print(a)


# # 关键行指一个文件中包含的不重复行。关键行数指一个文件中包含的不重复行的数量。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬
# # 统计附件文件中与关键行的数量。
#
#
# file = open('latex.log', 'r', encoding='utf-8')
# txt = file.readlines()
# a = set(txt)
# for i in txt:
#     txt.remove(i)
# b = set(txt)
# print('共{}关键行'.format(len(a)-len(b)))


# 读入一个字典类型的字符串，反转其中键值对输出。
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



import jieba


def take_second(x):
    return x[1]


def get_text():
    txt = open('沉默的羔羊.txt', 'r', encoding='utf-8').read()
    for item in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~\n':
        txt = txt.replace(item, ' ')
    words = jieba.lcut(txt)
    # print(words)
    dic = dict()
    for item in words:
        if len(item) < 2:
            continue
        else:
            dic[item] = dic.get(item, 0) + 1
    result = list(dic.items())
    # print(result)
    result.sort(key=take_second, reverse=True)
    # print(result)
    print(result[0][0])


get_text()
