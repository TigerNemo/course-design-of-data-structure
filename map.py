import cv2
from PIL import Image,ImageTk

class Dijk:
    def __init__(self):
        self.weight=10000
        self.path=[]
        self.flag=1
class Node:
    def __init__(self,name,x,y,function):
        self.name=name
        self.function=function
        self.x=x
        self.y=y
class Edge:
    def __init__(self,weight,name1,name2):
        self.weight=weight
        self.node_1=name1
        self.node_2=name2
class AdjList:
    def __init__(self,nodes,edges):
        self.nodes=nodes
        self.edges=edges
        self.maps=[]
    def creat(self):
        for node in self.nodes:
            self.maps.append([node])
        for edge in self.edges:
            i,j=0,0
            for n in range(len(self.nodes)):
                if edge.node_1 == self.nodes[n].name:
                    i=n
                if edge.node_2 == self.nodes[n].name:
                    j=n
            self.maps[i].append([j,edge.weight])
            self.maps[j].append([i,edge.weight])

    def short_weight(self,name1="逸夫教学楼", name2="教师公寓"):
        Dists=[]
        a,b=0,0  # 标记起点和终点的位置
        for n in range(len(self.nodes)):
            if name1==self.nodes[n].name:
                a=n
            if name2==self.nodes[n].name:
                b=n
            dist=Dijk()
            Dists.append(dist)
        Dists[a].flag=0  # 表示a走过
        Dists[a].weight=0  # 将走过的点的权重清零
        Dists[a].path.append(a)
        start = a
        while Dists[b].flag:
            for node in self.maps[start][1:]:
                if Dists[node[0]].weight > Dists[start].weight+int(node[1]):
                    Dists[node[0]].weight = Dists[start].weight + int(node[1])  # 修改权值
                    Dists[node[0]].path=Dists[start].path[::]  # 将与c相连的结点分别写成不同的路径
                    Dists[node[0]].path.append(node[0])
            min=10000
            index=0
            for n in range(len(Dists)):
                if Dists[n].flag == 1 and Dists[n].weight < min:
                    min=Dists[n].weight  # 找到最小权值的点
                    index = n
            Dists[index].flag = 0  # 找到权值最短的一个点index，将其清零
            start = index  # 从index开始遍历其邻接的节点

        path=[]
        for i in range(len(Dists[b].path)-1):
            e=Edge(name1=self.nodes[Dists[b].path[i]].name,name2=self.nodes[Dists[b].path[i+1]].name,weight=0)
            path.append(e)
        return path

    def short_mid(self,name1="逸夫教学楼", name2="教师公寓"):
        Dists=[]
        a,b=0,0
        for n in range(len(self.nodes)):
            if name1==self.nodes[n].name:
                a=n
            if name2==self.nodes[n].name:
                b=n
            dist=Dijk()
            Dists.append(dist)
        Dists[a].flag=0
        Dists[a].weight=0
        Dists[a].path.append(a)
        start = a
        while Dists[b].flag:
            for node in self.maps[start][1:]:
                if Dists[node[0]].weight > Dists[start].weight+1:
                    Dists[node[0]].weight = Dists[start].weight + 1
                    Dists[node[0]].path = Dists[start].path[::]  # 将与c相连的结点分别写成不同的路径
                    Dists[node[0]].path.append(node[0])
            min=10000
            index=0
            for n in range(len(Dists)):
                if Dists[n].flag == 1 and Dists[n].weight < min:
                    min=Dists[n].weight  # 找到权值最小的点
                    index = n   # 记录其位置
            Dists[index].flag = 0  # 将终点的flag也改成0
            start = index
        path=[]
        for i in range(len(Dists[b].path)-1):
            e=Edge(name1=self.nodes[Dists[b].path[i]].name,
                   name2=self.nodes[Dists[b].path[i+1]].name,
                   weight=0)
            path.append(e)
        return path

    def all_path(self,name1,name2):

        pass
    def Add_Node(self,name,x,y,function=""):
        for node in self.nodes:
            if node.name == name:
                return 1   # 存在
        a=Node(name=name,x=x,y=y,function="")
        a.function=function
        self.nodes.append(a)
        with open("node.txt","a+") as fp:
            fp.write("%s %s %s %s\n"%(a.name,a.x,a.y,a.function))
            self.creat()
        return 0
    def Add_Edge(self,name1,name2,weight):
        flag1=0
        flag2=0
        for node in self.nodes:
            if node.name == name1:
                flag1=1
            if node.name==name2:
                flag2=1
        if flag1 and flag2:
            for edge in self.edges:
                if edge.node_1 == name1 and edge.node_2 == name2:
                    return 2  # 已存在边
                elif edge.node_1 == name2 and edge.node_2 == name1:
                    return 2
                else:
                    with open("edge.txt", "a+") as fp:
                        fp.write("%s %s %s\n" % (name1,name2,weight))
                        self.creat()
                    return 0  # 成功

        else:
            return 1  # 顶点不存在
    def Del_Node(self,name):
        flag=0
        tops=[]
        edges=[]
        for n in range(len(self.nodes)):
            if self.nodes[n].name != name:
                tops.append(self.nodes[n])
            else:
                for edge in self.edges:
                    flag=0
                    for i in self.maps[n][1:]:
                        if (edge.node_1 == name and edge.node_2 == self.nodes[i[0]].name) or (edge.node_2 == name and self.nodes[i[0]].name):
                            flag=1
                    if flag == 0:
                        edges.append(edge)
        with open("edge.txt","w") as fp:
            for edge in edges:
                fp.write("%s %s %s\n"%(edge.node_1,edge.node_2,edge.weight))
        with open("node.txt","w") as fp:
            for top in tops:
                fp.write("%s %s %s %s\n" % (top.name,top.x,top.y,top.function))
        self.creat()
    def Del_edge(self,name1,name2):
        edges=[]
        for edge in self.edges:
            if (edge.node_1 == name1 and edge.node_2 == name2 )or( edge.node_1 == name2 and edge.node_2 == name1):
                pass
            else:
                edges.append(edge)
        with open("edge.txt","w") as fp:
            for edge in edges:
                fp.write("%s %s %s\n"%(edge.node_1,edge.node_2,edge.weight))
        self.creat()
    def change(self,name,new,function):
        for top in self.nodes:
            if top.name == name:
                top.name = new
                top.function = function
        with open("node.txt","w") as fp:
            for top in self.nodes:
                fp.write("%s %s %s %s\n" % (top.name,top.x,top.y,top.function))
        with open("edge.txt","r") as fp:
            str=fp.read()
            str=str.replace(name,new)
        with open("edge.txt", "w") as fp:
            fp.write(str)


def photo_c(tops,edgas):
    img = cv2.imread("map.jpg")
    point_size = 7
    point_color = (0, 255, 0)
    thickness = -1
    for edge in edgas:
        x_1,y_1=0,0
        x_2,y_2=0,0
        for top in tops:
            if edge.node_1 == top.name:
                x_1,y_1=top.x,top.y
            elif edge.node_2 == top.name:
                x_2,y_2=top.x,top.y
        cv2.line(img, (int(x_1), int(y_1)), (int(x_2), int(y_2)), (255, 0, 255), 4)
    for top in tops:
        x,y=top.x,top.y
        cv2.circle(img, (int(x),int(y)), point_size, point_color, thickness)

    img=cv2.resize(img,(int(img.shape[0]*0.7),int(img.shape[1]*0.7)))
    image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    return image


def creat_data():
    top=[]
    with open("node.txt") as fp:
        for i in fp.readlines():
            top.append(i.split())
    edge=[]
    with open("edge.txt") as fp:
        for i in fp.readlines():
            edge.append(i.split())
    return top, edge


def creat_map():
    a, b = creat_data()
    tops = []
    edges = []
    for i in a:
        if i!=[]:
            top = Node(i[0], i[1], i[2],i[3])
            tops.append(top)
    for i in b:
        edge = Edge(i[2], i[0], i[1])
        edges.append(edge)
    map = AdjList(tops, edges)
    map.creat()
    return map

