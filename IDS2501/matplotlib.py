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

#Prim Algorithm
minimumSpainningTree(graph):
    mark all vertices and edges as unvisited
    mark some vertex, say v,  as visited
    for all the vertices:
        find the least weight edge from a visited vertex to an
        unvisited vertex, say w
        mark the edge and was visited
        

#topological sort
topologicalSort(graph g):
    stack = LinkedStack()
    mark all vertices in the graph as unvisited
    for each vertex, v, in the graph:
        if v is unvisited:
           dfs(g, v, stack)
    return stack


dfs(graph, v, stack):
    mark v as visited
    for each vertex, w, adjacent to v:
        if w is unvisited:
            dfs(grap, w, stack)

    stack.push(v)


#Dijkstra Algorithm
Do
  
    Find the vertex F that is not yet included and has the minimal
    distance in the results grid
    Mark F as included
    For each other vertex T not included
        If there is an edge from F to T
        Set new distance + edge's weight
        If new distance < T's distance in the results grid
           Set T's distance to new distance
           Set T's parent in the results grid to F
While at least one vertex is not included

#Back tracking
Create an empty stack
Push the starting state onto the stack
While the stack is not empty
    Pop the stack and examine the state
    If the state represents an ending state
       Return SUCCESSFUL CONCLUSION
    Else if t