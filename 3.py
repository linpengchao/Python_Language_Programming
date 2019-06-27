# #工作日VS每天
#
# globalWeekOfYear = 365 // 7
# globalDayLast = 365 % 7
# globalResultWorkDay = 1
# globalResultEveryDay = 1
# globalFactorDayUp = 0.01
# constFactorDayUp = 0.01
#
# def voidCalculateDayUp():
#     global globalResultWorkDay
#     global globalResultEveryDay
#     globalResultWorkDay = 1
#     globalResultEveryDay = 1
#     for tempWeek in range(globalWeekOfYear):
#         globalResultWorkDay *= 1 - constFactorDayUp
#         globalResultEveryDay *= 1 + constFactorDayUp
#         for tempDay in range(5):
#             globalResultWorkDay *= 1 + globalFactorDayUp
#             globalResultEveryDay *= 1 + constFactorDayUp
#         globalResultWorkDay *= 1 - constFactorDayUp
#         globalResultEveryDay *= 1 + constFactorDayUp
#     globalResultWorkDay *= 1 - globalFactorDayUp
#     globalResultEveryDay *= 1 + constFactorDayUp
#     # print(globalResultWorkDay)
#     # print(globalResultEveryDay)
#
#
# voidCalculateDayUp()
# while globalResultWorkDay < globalResultEveryDay:
#     globalFactorDayUp += 0.001
#     voidCalculateDayUp()
# print('工作日的努力参数是: {:.3f}'.format(globalFactorDayUp))
#

# # 文本进度条
# # log型
# import time
#
# print('   ----开始执行----')
# for tempPercent in range(21):
#     print('{:<3}'.format(tempPercent*5) + '%'
#           + '[' + tempPercent*'*' + (20-tempPercent)*'.' + ']')
#     time.sleep(0.5)
# print('   ----结束执行----')


# 文本进度条
# 动态型
# import time
#
# print('   ----开始执行----', end='')
# globalStartRunTime = time.perf_counter()
# time.sleep(0.1)
# for tempPercent in range(21):
#     print('\r' + '{:<3}'.format(tempPercent*5) + '%'
#           + '[' + tempPercent*'*' + (20-tempPercent)*'.' + ']'
#           + '{:.1f}S'.format(time.perf_counter()-globalStartRunTime), end='')
#     time.sleep(0.1)
# print('\r' + '   ----结束执行----')

# # 三次方格式化
#
# globalNumInput = input()
# globalResultPow3 = pow(eval(globalNumInput), 3)
# if len(str(globalResultPow3)) > 20:
#     print(globalResultPow3)
# else:
#     print(str(globalResultPow3).center(20, '-'))

# # 星号三角
#
# globalNumInput = eval(input())
# if globalNumInput % 2 == 0:
#     globalNumInput += 1
# for tempCount in range(0, globalNumInput, 2):
#     tempStr = (tempCount+1) * '*'
#     print(tempStr.center(globalNumInput))

# # 凯撒密码
#
# globalStrInput = input()
# globalStrOutput = ''
# globalListRangeAW = list(range(ord('a'), ord('w')+1))\
#                     + list(range(ord('A'), ord('W')+1))
# # 遍历字符串，替换
# for tempCount in range(len(globalStrInput)):
#     if ord(globalStrInput[tempCount]) in globalListRangeAW:
#         globalStrOutput += chr(ord(globalStrInput[tempCount])+3)
#     elif ord(globalStrInput[tempCount]) in range(ord('x'), ord('z')+1):
#         globalStrOutput += chr(ord(globalStrInput[tempCount])
#                                - (ord('x')-ord('a')))
#     elif ord(globalStrInput[tempCount]) in range(ord('X'), ord('Z')+1):
#         globalStrOutput += chr(ord(globalStrInput[tempCount])
#                                - (ord('X')-ord('A')))
#     else:
#         globalStrOutput += globalStrInput[tempCount]
# print(globalStrOutput)

# # 平方根格式化
#
# globalStrInput = input()
# globalNumSqrt = eval(globalStrInput) ** 0.5
# globalStrOutput = '{:+>30.3f}'.format(globalNumSqrt)
# print(globalStrOutput)

# 字符串截取
globalStrInput = input()
globalListSplit = globalStrInput.split('-')
globalStrOutput = ''
globalStrOutput = globalListSplit[0] + '+' + globalListSplit[-1]
print(globalStrOutput)

