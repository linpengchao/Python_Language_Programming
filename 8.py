# 获得用户任何可能的输入，将英文字符打印输出，程序不出错误


# alpha = []
# for i in range(26):
#     alpha.append(chr(ord('a') + i))
#     alpha.append(chr(ord('A') + i))
# s = input()
# for c in s:
#     if c in alpha:
#         print(c, end="")



s = input()
try:
    if complex(s) == complex(eval(s)):
        print(eval(s)**2)
except:
    print("输入有误")
