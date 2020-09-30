import numpy as ny
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
data = np.load('.../data/测试数据.npz')
name = data['columns']
values = data['values']
label = ['第一产业','第二产业',' 第三产业']
plt.figure(fisize=(6,5))
plt.bar(range(3),values[-1,3:6],width = 0.5)
plt.xlabel('产业')
plt.ylabel('生产总值（亿元）')
plt.xticks(range(3),label)
plt.title('一季度国民生产总值')
plt.savefig('.../tmp/一季度国民生产总值.png')
plt.show()

matplotlib.pyplot.pie(x, explode, labels=None,colors, autopct=None,
pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None,
radius=None, counterclock=True, wegeprops=None, textprops=None, center=(0,0),
frame=False, hold=None, data=None)

plt.figure(figsize=(6,6))
lable=['第一产业','第二产业','第三产业']
explode = [0.01,0.01,0.01]
plt.pie(values[-1,3:6],explode=explode,labels=label,autopct='%1.1f%%')
plt.title('一季度国民生产总值')
plt.savefig('.../tmp/一季度国民生产总值.png')
plt.show()

minimumSpainningTree(graph):
    mark all vertices and edges as unvisited
    mark so
