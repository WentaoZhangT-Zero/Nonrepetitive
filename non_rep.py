#我现在希望按照如下算法检测grid的子图的5染色是否具有nonrepetitive性质。我预先已经有了该子图除了一个点外的5染色，现在我想考虑对最后一个点遍历5种颜色，检查是否仍然满足nonrepetitive性质，算法是，先找到与这个点同色的点，从这些点开始向左右延申出长度为2的路径，与目标点延申出的路径同色且不相交的存在一个列表中。如果这些路径能平城repetitive path，那就结束目标点染这个颜色的情况，如果不行，就继续向左右延申重复步骤，直到路径的长度达到子图顶点个数的一半。如果一直没有repetitive path，那就把这种子图染色存储下来

#第一组代码为检测带一个目标点的染色是否符合nonrepetitive性质
from collections import defaultdict

def extend_path(path, neighbors):
    """
    从路径的两个端点的邻居中延伸路径。
    返回所有可能的延伸路径。
    """
    extended_paths = []
    # 获取路径的两个端点
    start = path[0]
    end = path[-1]
    
    # 从起点延伸
    for neighbor in neighbors[start]:
        if neighbor not in path:  # 避免重复访问节点
            extended_paths.append([neighbor] + path)
    
    # 从终点延伸
    for neighbor in neighbors[end]:
        if neighbor not in path:  # 避免重复访问节点
            extended_paths.append(path + [neighbor])
    
    return extended_paths

def paths_disjoint_samecolor(path1, path2, coloring):
    """
    检查两条路径是否不交且颜色相同，是则返回True。
    """
    set1 = set(path1)
    set2 = set(path2)
    if not set1.isdisjoint(set2):
        return False
    
    a=[ coloring[k] for k in path1]
    b=[ coloring[k] for k in path2]
    if a != b:
        return False
    
    return True



def nonrepetitive(neighbors, coloring, target_node):
    for i in range(len(neighbors)-1):
        if coloring[i]== coloring[target_node]:
            if i in neighbors[target_node]:
                return False
    max_length=len(neighbors)//2
    paths = [[i] for i in range(len(neighbors)-1) if coloring[i]== coloring[target_node]]
    path_targetnode = defaultdict(list)
    x=tuple([target_node])
    path_targetnode[x]=paths


    while path_targetnode:        
        target_paths=list(path_targetnode.keys())
        for path_1 in target_paths:
            path=list(path_1)
            if len(path)==max_length:
                return True
            
            new_target_paths=extend_path(path,neighbors)
            corre_paths_dic=path_targetnode[path_1]
            for i in new_target_paths:
                for j in corre_paths_dic:
                    for p in extend_path(j,neighbors):
                        if paths_disjoint_samecolor(i,p,coloring):
                            if p[0] in neighbors[i[-1]] or i[0] in neighbors[p[-1]]:
                                return False
                            else:
                                path_targetnode[tuple(i)].append(p)
            path_targetnode.pop(path_1)
    return True

#下一组代码：构造grid的子图
import math
def neighborgridvertex(k,n):
    if k==0:
        if n==1:
            return []
        if n==2 or n==3:
            return [1]
        if n>=4:
            return [1,3]
    nei=[]
    a=int(math.sqrt(k))
    b=k+1-a**2
    if b==1:
        nei=[(a-1)**2+b-1,k+1,(a+1)**2+b-1]
    if b < a+1 and b>1:
        nei=[(a-1)**2+b-1,k+1,(a+1)**2+b-1,k-1]
    if b==a+1:
        nei=[k-1,k+1,(a+1)**2+b-1,(a+1)**2+b+1]
    if b< 2*a+1 and b >a+1:
        nei=[k-1,k+1,(a-1)**2+b-3,(a+1)**2+b+1]
    if b==2*a+1:
        nei=[k-1,(a-1)**2+b-3,(a+1)**2+b+1]
    x=[]
    for i in nei:
        if i<n:
            x.append(i)
    return x

def neighborgridsub(n):
    a=[]
    for i in range(n):
        a.append(neighborgridvertex(i,n))
    return a

#下面这块是6\*6的所有5染色，满足左上角的2\*2为(1,2,4,3),(1,2,3,1),(1,2,2,3)
Orig=[[1,2,3,4],[1,2,1,3],[1,2,3,2]]
for i in range(40):
    i=i+5
    neighbor=neighborgridsub(i)
    Orig_1=[]
    for j in range(5):
        j=j+1
        for color in Orig:
            if nonrepetitive(neighbor,color+[j],i-1):
                Orig_1.append(color+[j])
    print(i)
    print(len(Orig_1))
    Orig=Orig_1      
    
    
#下一组代码，构造稠密网格
import math
def neighbormoregridvertex(k,n):
    if k==0:
        if n==1:
            return [2]
        if n==2 or n==3:
            return [1,2]
        if n>=4:
            return [1,2,3]
    if k==3:
        if n<3:
            return []
        if n>=4 and n<8:
            return [0,1,2]
        if n==8:
            return [0,1,2,7]
        if n>=9:
            return [0,1,2,7,8]
            
    
    nei=[]
    a=int(math.sqrt(k))
    b=k+1-a**2
    if b==1:
        nei=[(a-1)**2+b-1,k+1,(a+1)**2+b-1,(a-1)**2+b,(a+1)**2+b]
    if b < a+1 and b>1:
        nei=[(a-1)**2+b-1,k+1,(a+1)**2+b-1,k-1,(a-1)**2+b,(a-1)**2+b-2,(a+1)**2+b,(a+1)**2+b-2]
    if b==a+1:
        nei=[k-1,k+1,(a+1)**2+b-1,(a+1)**2+b+1,a**2-a,(a+1)**2+b-2,(a+1)**2+b,(a+1)**2+b+2]
    if b< 2*a+1 and b >a+1:
        nei=[k-1,k+1,(a-1)**2+b-3,(a+1)**2+b+1,(a-1)**2+b-4,(a-1)**2+b-2,(a+1)**2+b,(a+1)**2+b+2]
    if b==2*a+1:
        nei=[k-1,(a-1)**2+b-3,(a+1)**2+b+1,(a-1)**2+b-4,(a+1)**2+b]
    x=[]
    for i in nei:
        if i<n:
            x.append(i)
    return x

def neighbormoregridsub(n):
    a=[]
    for i in range(n):
        a.append(neighbormoregridvertex(i,n))
    return a

#下面这块是稠密6\*6的所有8染色，满足左上角的2\*2为(1,2,4,3)

Orig=[[1,2,3,4]]
for i in range(32):
    i=i+5
    neighbor=neighbormoregridsub(i)
    Orig_1=[]
    for j in range(8):
        j=j+1
        for color in Orig:
            if nonrepetitive(neighbor,color+[j],i-1):
                Orig_1.append(color+[j])
    print(i)
    print(len(Orig_1))
    Orig=Orig_1  
    
#构造三角剖分

import math
def neighbormorelessgridvertex(k,n):
    if k==0:
        if n==1:
            return [2]
        if n==2 or n==3:
            return [1,2]
        if n>=4:
            return [1,2]
    if k==3:
        if n<3:
            return []
        if n>=4 and n<8:
            return [0,1,2]
        if n==8:
            return [0,1,2]
        if n>=9:
            return [0,1,2,8]
            
    
    nei=[]
    a=int(math.sqrt(k))
    b=k+1-a**2
    if b==1:
        nei=[(a-1)**2+b-1,k+1,(a+1)**2+b-1,(a-1)**2+b]
    if b < a+1 and b>1:
        nei=[(a-1)**2+b-1,k+1,(a+1)**2+b-1,k-1,(a-1)**2+b,(a+1)**2+b-2]
    if b==a+1:
        nei=[k-1,k+1,(a+1)**2+b-1,(a+1)**2+b+1,(a+1)**2+b-2,(a+1)**2+b+2]
    if b< 2*a+1 and b >a+1:
        nei=[k-1,k+1,(a-1)**2+b-3,(a+1)**2+b+1,(a-1)**2+b-4,(a+1)**2+b+2]
    if b==2*a+1:
        nei=[k-1,(a-1)**2+b-3,(a+1)**2+b+1,(a-1)**2+b-4]
    x=[]
    for i in nei:
        if i<n:
            x.append(i)
    return x

def neighbormorelessgridsub(n):
    a=[]
    for i in range(n):
        a.append(neighbormoregridvertex(i,n))
    return a

#下面这块是三角剖分所有8染色，满足左上角的2\*2为(1,2,4,3)，(1,2,1,3)

Orig=[[1,2,3,4],[1,2,1,3]]
for i in range(32):
    i=i+5
    neighbor=neighbormorelessgridsub(i)
    Orig_1=[]
    for j in range(8):
        j=j+1
        for color in Orig:
            if nonrepetitive(neighbor,color+[j],i-1):
                Orig_1.append(color+[j])
    print(i)
    print(len(Orig_1))
    Orig=Orig_1  
    
