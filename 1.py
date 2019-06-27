# #温度转换
# tempstr=input()
# if tempstr[-1] in ['F','f']:
#     digree=(eval(tempstr[0:-1])-32)/1.8
#     print("{:.2f}C".format(digree))
# elif tempstr[-1] in ['C','c']:
#     digree=eval(tempstr[0:-1])*1.8+32
#     print("{:.2f}F".format(digree))
# else:
#     print("输入格式错误")

# #数字转换
# # source=['零','一','二','三','四','五','六','七','八','九']
# # tempstr=input()
# # out=""
# # for i in tempstr:
# #     out=out+source[eval(i)]
# # print(out)

# #温度转换二
# tempstr=input()
# if tempstr[0] in ['F']:
#     digree=(eval(tempstr[1:])-32)/1.8
#     print("C{:.2f}".format(digree))
# elif tempstr[0] in ['C']:
#     digree=eval(tempstr[1:])*1.8+32
#     print("F{:.2f}".format(digree))

# #货币转换
# tempstr=input()
# if tempstr[0:3] == 'USD':
#     money=eval(tempstr[3:])*6.78
#     print("RMB{:.2f}".format(money))
# elif tempstr[0:3] == 'RMB':
#     money=eval(tempstr[3:])/6.78
#     print("USD{:.2f}".format(money))

# #测试
# tempstr=input()
# if eval(tempstr)==0:
#     print("Hello World")
# elif eval(tempstr)>0:
#     print("He\nll\no \nWo\nrl\nd")
# else:
#     print("H\ne\nl\nl\no\n \nW\no\nr\nl\nd")

# 测试2
tempstr=input()
tempstr=tempstr.replace(' ','')
i=tempstr.find('+')
if i>0:
    num=eval(tempstr[0:i])+eval(tempstr[i+1:])
    print("{:.2f}".format(num))
i=tempstr.find('-')
if i>0:
    num=eval(tempstr[0:i])-eval(tempstr[i+1:])
    print("{:.2f}".format(num))
i=tempstr.find('*')
if i>0:
    num=eval(tempstr[0:i])*eval(tempstr[i+1:])
    print("{:.2f}".format(num))
i=tempstr.find('/')
if i>0:
    num=eval(tempstr[0:i])/eval(tempstr[i+1:])
    print("{:.2f}".format(num))
