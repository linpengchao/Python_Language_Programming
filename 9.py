# import numpy
# import matplotlib
# import matplotlib.pyplot as plt
#
# matplotlib.rcParams['font.family'] = 'SimHei'
# radar_labels = numpy.array(['研究型[I]', '艺术型[A]', '社会型[S]',
#                             '企业型[E]', '常规型[C]', '现实型[R]'])
# data = numpy.array([[0.32, 0.43, 0.89, 0.56, 0.20, 0.18],
#                     [0.97, 0.45, 0.38, 0.28, 0.37, 0.19],
#                     [0.65, 0.38, 0.39, 0.78, 0.45, 0.23],
#                     [0.23, 0.85, 0.27, 0.29, 0.34, 0.20],
#                     [0.34, 0.29, 0.40, 0.19, 0.89, 0.34],
#                     [0.23, 0.56, 0.45, 0.49, 0.26, 0.79]])
# data_labels = ('艺术家', '实验员', '工程师', '推销员', '社会工作者', '记事员')
# angles = numpy.linspace(0, 2*numpy.pi, 6, endpoint=False)
# data = numpy.concatenate((data, [data[0]]))
# angles = numpy.concatenate((angles, [angles[0]]))
# fig = plt.subplot(111, polar=True)
# plt.plot(angles, data, 'o-', linewidth=1, alpha=0.2)
# plt.fill(angles, data, alpha=0.25)
# plt.thetagrids(angles*180/numpy.pi, radar_labels)
# plt.figtext(0.52, 0.95, '霍兰德人格分析', ha='center', size=20)
# legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)
# plt.setp(legend.get_texts(), fontsize='large')
# plt.grid(True)
# plt.savefig('holland_rader.jpg')
# plt.show()


# 获取系统的递归深度、当前执行文件路径、系统最大UNICODE编码值等3个信息，并打印输出
# import sys
#
# a = sys.getrecursionlimit()
# # print(a)
# b = sys.executable
# # print(b[0])
# c = sys.maxunicode
# # print(c)
# print('RECLIMIT:{}, EXEPATH:{}, UNICODE:{}'.format(a, b, c))


import tabulate

data = [ ["北京理工大学", "985", 2000], \
         ["清华大学", "985", 3000], \
         ["大连理工大学", "985", 4000], \
         ["深圳大学", "211", 2000], \
         ["沈阳大学", "省本", 2000], \
    ]
a = tabulate.tabulate(tabular_data=data, tablefmt="grid")

print(a)


