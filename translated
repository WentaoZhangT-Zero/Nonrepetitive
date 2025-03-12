# The first set of code checks if the coloring of a target point in a graph satisfies the nonrepetitive property.
from collections import defaultdict

def extend_path(path, neighbors):
    """
    Extend the path from the neighbors of the two endpoints of the path.
    Returns all possible extended paths.
    """
    extended_paths = []
    # Get the two endpoints of the path
    start = path[0]
    end = path[-1]

    # Extend from the start point
    for neighbor in neighbors[start]:
        if neighbor not in path:  # Avoid revisiting nodes
            extended_paths.append([neighbor] + path)

    # Extend from the end point
    for neighbor in neighbors[end]:
        if neighbor not in path:  # Avoid revisiting nodes
            extended_paths.append(path + [neighbor])

    return extended_paths

def paths_disjoint_samecolor(path1, path2, coloring):
    """
    Check if two paths are disjoint and have the same coloring. Returns True if they are.
    """
    set1 = set(path1)
    set2 = set(path2)
    if not set1.isdisjoint(set2):
        return False

    a = [coloring[k] for k in path1]
    b = [coloring[k] for k in path2]
    if a != b:
        return False

    return True

def nonrepetitive(neighbors, coloring, target_node):
    for i in range(len(neighbors) - 1):
        if coloring[i] == coloring[target_node]:
            if i in neighbors[target_node]:
                return False
    max_length = len(neighbors) // 2
    paths = [[i] for i in range(len(neighbors) - 1) if coloring[i] == coloring[target_node]]
    path_targetnode = defaultdict(list)
    x = tuple([target_node])
    path_targetnode[x] = paths

    while path_targetnode:
        target_paths = list(path_targetnode.keys())
        for path_1 in target_paths:
            path = list(path_1)
            if len(path) == max_length:
                return True

            new_target_paths = extend_path(path, neighbors)
            corre_paths_dic = path_targetnode[path_1]
            for i in new_target_paths:
                for j in corre_paths_dic:
                    for p in extend_path(j, neighbors):
                        if paths_disjoint_samecolor(i, p, coloring):
                            if p[0] in neighbors[i[-1]] or i[0] in neighbors[p[-1]]:
                                return False
                            else:
                                path_targetnode[tuple(i)].append(p)
            path_targetnode.pop(path_1)
    return True

# Next set of code: Construct a subgraph of the grid
import math

def neighborgridvertex(k, n):
    if k == 0:
        if n == 1:
            return []
        if n == 2 or n == 3:
            return [1]
        if n >= 4:
            return [1, 3]
    nei = []
    a = int(math.sqrt(k))
    b = k + 1 - a**2
    if b == 1:
        nei = [(a - 1)**2 + b - 1, k + 1, (a + 1)**2 + b - 1]
    if b < a + 1 and b > 1:
        nei = [(a - 1)**2 + b - 1, k + 1, (a + 1)**2 + b - 1, k - 1]
    if b == a + 1:
        nei = [k - 1, k + 1, (a + 1)**2 + b - 1, (a + 1)**2 + b + 1]
    if b < 2 * a + 1 and b > a + 1:
        nei = [k - 1, k + 1, (a - 1)**2 + b - 3, (a + 1)**2 + b + 1]
    if b == 2 * a + 1:
        nei = [k - 1, (a - 1)**2 + b - 3, (a + 1)**2 + b + 1]
    x = []
    for i in nei:
        if i < n:
            x.append(i)
    return x

def neighborgridsub(n):
    a = []
    for i in range(n):
        a.append(neighborgridvertex(i, n))
    return a

# The following block is all 5-colorings of a 6x6 grid where the top-left 2x2 is (1,2,4,3), (1,2,3,1), (1,2,2,3)
Orig = [[1, 2, 3, 4], [1, 2, 1, 3], [1, 2, 3, 2]]
for i in range(40):
    i = i + 5
    neighbor = neighborgridsub(i)
    Orig_1 = []
    for j in range(5):
        j = j + 1
        for color in Orig:
            if nonrepetitive(neighbor, color + [j], i - 1):
                Orig_1.append(color + [j])
    print(i)
    print(len(Orig_1))
    Orig = Orig_1

# Next set of code: Construct P \boxtimes P
import math

def neighbormoregridvertex(k, n):
    if k == 0:
        if n == 1:
            return [2]
        if n == 2 or n == 3:
            return [1, 2]
        if n >= 4:
            return [1, 2, 3]
    if k == 3:
        if n < 3:
            return []
        if n >= 4 and n < 8:
            return [0, 1, 2]
        if n == 8:
            return [0, 1, 2, 7]
        if n >= 9:
            return [0, 1, 2, 7, 8]

    nei = []
    a = int(math.sqrt(k))
    b = k + 1 - a**2
    if b == 1:
        nei = [(a - 1)**2 + b - 1, k + 1, (a + 1)**2 + b - 1, (a - 1)**2 + b, (a + 1)**2 + b]
    if b < a + 1 and b > 1:
        nei = [(a - 1)**2 + b - 1, k + 1, (a + 1)**2 + b - 1, k - 1, (a - 1)**2 + b, (a - 1)**2 + b - 2, (a + 1)**2 + b, (a + 1)**2 + b - 2]
    if b == a + 1:
        nei = [k - 1, k + 1, (a + 1)**2 + b - 1, (a + 1)**2 + b + 1, a**2 - a, (a + 1)**2 + b - 2, (a + 1)**2 + b, (a + 1)**2 + b + 2]
    if b < 2 * a + 1 and b > a + 1:
        nei = [k - 1, k + 1, (a - 1)**2 + b - 3, (a + 1)**2 + b + 1, (a - 1)**2 + b - 4, (a - 1)**2 + b - 2, (a + 1)**2 + b, (a + 1)**2 + b + 2]
    if b == 2 * a + 1:
        nei = [k - 1, (a - 1)**2 + b - 3, (a + 1)**2 + b + 1, (a - 1)**2 + b - 4, (a + 1)**2 + b]
    x = []
    for i in nei:
        if i < n:
            x.append(i)
    return x

def neighbormoregridsub(n):
    a = []
    for i in range(n):
        a.append(neighbormoregridvertex(i, n))
    return a

# The following block is all 8-colorings of P \boxtimes P 6x6 where the top-left 2x2 is (1,2,4,3)
Orig = [[1, 2, 3, 4]]
for i in range(32):
    i = i + 5
    neighbor = neighbormoregridsub(i)
    Orig_1 = []
    for j in range(8):
        j = j + 1
        for color in Orig:
            if nonrepetitive(neighbor, color + [j], i - 1):
                Orig_1.append(color + [j])
    print(i)
    print(len(Orig_1))
    Orig = Orig_1

# Construct T_3
import math

def neighbormorelessgridvertex(k, n):
    if k == 0:
        if n == 1:
            return [2]
        if n == 2 or n == 3:
            return [1, 2]
        if n >= 4:
            return [1, 2]
    if k == 3:
        if n < 3:
            return []
        if n >= 4 and n < 8:
            return [0, 1, 2]
        if n == 8:
            return [0, 1, 2]
        if n >= 9:
            return [0, 1, 2, 8]

    nei = []
    a = int(math.sqrt(k))
    b = k + 1 - a**2
    if b == 1:
        nei = [(a - 1)**2 + b - 1, k + 1, (a + 1)**2 + b - 1, (a - 1)**2 + b]
    if b < a + 1 and b > 1:
        nei = [(a - 1)**2 + b - 1, k + 1, (a + 1)**2 + b - 1, k - 1, (a - 1)**2 + b, (a + 1)**2 + b - 2]
    if b == a + 1:
        nei = [k - 1, k + 1, (a + 1)**2 + b - 1, (a + 1)**2 + b + 1, (a + 1)**2 + b - 2, (a + 1)**2 + b + 2]
    if b < 2 * a + 1 and b > a + 1:
        nei = [k - 1, k + 1, (a - 1)**2 + b - 3, (a + 1)**2 + b + 1, (a - 1)**2 + b - 4, (a + 1)**2 + b + 2]
    if b == 2 * a + 1:
        nei = [k - 1, (a - 1)**2 + b - 3, (a + 1)**2 + b + 1, (a - 1)**2 + b - 4]
    x = []
    for i in nei:
        if i < n:
            x.append(i)
    return x

def neighbormorelessgridsub(n):
    a = []
    for i in range(n):
        a.append(neighbormoregridvertex(i, n))
    return a

# The following block is all 8-colorings of T_3 where the top-left 2x2 is (1,2,4,3), (1,2,1,3)
Orig = [[1, 2, 3, 4], [1, 2, 1, 3]]
for i in range(32):
    i = i + 5
    neighbor = neighbormorelessgridsub(i)
    Orig_1 = []
    for j in range(8):
        j = j + 1
        for color in Orig:
            if nonrepetitive(neighbor, color + [j], i - 1):
                Orig_1.append(color + [j])
    print(i)
    print(len(Orig_1))
    Orig = Orig_1
