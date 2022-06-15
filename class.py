class Vertex:
    def __init__(self,name):
        self.name=name       
class Edge:
    def __init__(self,left,right,weight):
        self.left=left
        self.right=right
        self.weight=weight

a=Vertex('A')
b=Vertex('B')
c=Vertex('C')
# v=[a,b,c]

el=Edge(a,b,4)
e2=Edge(b,c,1)
e3=Edge(a,c,1)
# e2=Edge(a,c)
# e=[el,e2]

class Graph:
    def __init__(self,size):
        self.size=size
        self.vertexes=[]
        self.edges=[]
        self.adjmatrix=[]
        self.dict={'A':0,
               'B':1,
               'C':2
        }
    def connect(self,a,b,weight):
        # el=Edge(a,b,4)
        self.edges.append(el)
        self.edges.append(e2)
        self.edges.append(e3)
        self.vertexes.append(a.name)
        self.vertexes.append(b.name)
        # a.add_edge(el)
        # b.add_edge(e1)
    def print_adjmatrix(self):
        for i in range(self.size):
            self.adjmatrix.append([0 for i in range(self.size)])
            
        
        for edge in self.edges:
            self.adjmatrix[self.dict[edge.left.name]][self.dict[edge.right.name]]=1
        for i in self.adjmatrix:
            print(i)
    def print_edge(self):
        for edge in self.edges:
            print("{left.name}-->{right.name}  {weight}".format(left=edge.left,right=edge.right,weight=edge.weight))
        
        
g=Graph(3)
g.connect(a,b,4)

g.print_edge()
g.print_adjmatrix()


