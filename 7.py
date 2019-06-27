# import wordcloud
# import jieba
# from imageio import imread
#
# m = imread('123.png')
# t = open('关于实施乡村振兴战略的意见.txt', 'rt', encoding='gbk')
# c = wordcloud.WordCloud(font_path="C:\\Windows\\Fonts\\FZYouSJJW_507R.TTF",
#                         background_color='white', width=800, height=400,
#                         mask=m)
# c.generate(' '.join(jieba.lcut(t.read())))
# c.to_file("关于实施乡村振兴战略的意见.png")
#


# t = open('latex.log', 'r', encoding='utf-8')
# lines = t.readlines()
# m = lines.count('\n')
# n = len(lines)
# print(n-m)


# t = open('latex.log', 'r', encoding='utf-8')
# txt = t.read()
# txt = txt.lower()
# dic = dict()
# n = 0
# for c in 'abcdefghijklmnopqrstuvwxyz':
#     if txt.count(c) > 0:
#         dic[c] = txt.count(c)
#         n += dic[c]
# print('共{}个字符,{}'.format(n, dic))


# t = open('latex.log', 'r', encoding='utf-8')
# line = t.readlines()
# a = set(line)
# for i in a:
#     line.remove(i)
# b = set(line)
# print("共{}独特行".format(len(a)-len(b)))


# t = open('data.csv', 'r', encoding='utf-8')
# lines = t.readlines()
# nlines = []
# for line in lines:
#     line = line.strip('\n')
#     temp = line.split(',')
#     temp.reverse()
#     # print(temp)
#     nlines.append(','.join(temp)+'\n')
#     print(','.join(temp))


# t = open('data.csv', 'r', encoding='utf-8')
# txt = t.read()
# txt = txt.replace(' ', '')
# print(txt)
"""
打印输出附件文件的平均列数，计算方法如下：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬
（1）有效行指包含至少一个字符的行，不计算空行；‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬
（2）每行的列数为其有效字符数；‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬
（3）平均列数为有效行的列数平均值，采用四舍五入方式取整数进位。
"""


# f = open("latex.log")
# s, c = 0, 0
# for line in f:
#     line = line.strip("\n")
#     if line == "":
#         continue
#     s += len(line)
#     c += 1
# print(round(s / c))

f = open("data.csv")
ls = f.readlines()
ls = ls[::-1]
lt = []
for item in ls:
    item = item.strip("\n")
    item = item.replace(" ", "")
    lt = item.split(",")
    lt = lt[::-1]
    print(";".join(lt))
f.close()


