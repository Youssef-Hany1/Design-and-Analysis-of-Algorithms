import random,copy
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


graph = {
    1: {"neighbors": [8,6], "color": "black"},
    2: {"neighbors": [7,9], "color": "black"},
    3: {"neighbors": [8,4], "color": "black"},
    4: {"neighbors": [3,9,11], "color": ""},
    5: {"neighbors": [10,12], "color": ""},
    6: {"neighbors": [1,7,11], "color": ""},
    7: {"neighbors": [2,6,12], "color": ""},
    8: {"neighbors": [1,3], "color": ""},
    9: {"neighbors": [2,4,10], "color": ""},
    10: {"neighbors": [5,9], "color": "white"},
    11: {"neighbors": [4,6], "color": "white"},
    12: {"neighbors": [5,7], "color": "white"}
}

goal_graph = {
    1: {"neighbors": [8,6], "color": "white"},
    2: {"neighbors": [7,9], "color": "white"},
    3: {"neighbors": [8,4], "color": "white"},
    4: {"neighbors": [3,9,11], "color": ""},
    5: {"neighbors": [10,12], "color": ""},
    6: {"neighbors": [1,7,11], "color": ""},
    7: {"neighbors": [2,6,12], "color": ""},
    8: {"neighbors": [1,3], "color": ""},
    9: {"neighbors": [2,4,10], "color": ""},
    10: {"neighbors": [5,9], "color": "black"},
    11: {"neighbors": [4,6], "color": "black"},
    12: {"neighbors": [5,7], "color": "black"}
}

sol_seq = []
left_nodes = []

def draw_graph(graph):
    G = nx.Graph()
    for node, data in graph.items():
        color = data["color"] if data["color"] else "grey"  # default color is grey
        G.add_node(node, color=color)
        for neighbor in data["neighbors"]:
            G.add_edge(node, neighbor)

    colors = [data["color"] for node, data in G.nodes(data=True)]
    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, pos, node_color=colors)

    # edges
    nx.draw_networkx_edges(G, pos)

    # labels
    nx.draw_networkx_labels(G, pos, font_size=16, font_color='r')

    plt.axis('off')
    plt.show()


def bfs(graph, start , w):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if graph[start]["color"] == "black":
            if graph[node]["color"] == "white" and not w.__contains__(node) :
                return node
        else:
            if graph[node]["color"] == "black" and not w.__contains__(node) :
                return node
            
        if node not in visited:
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node]["neighbors"] if neighbor not in visited)

    return None


def remaining_least_moves(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return len(path) - 1 , path
    
        for neighbor in graph[node]["neighbors"]:
            if neighbor not in visited :
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None

""" def find_pair(node):
    for pair in pairs:
        if node in pair:
            return pair[1] if pair[0] == node else pair[0]
    #print(pairs,node)
    return node """


def update_left_nodes(graph2):
    global left_nodes  
    
    left_n = []
    for node,g in zip(graph2,goal_graph):
        if graph2[node]["color"] != goal_graph[g]["color"]:         
            print("not in goal", node)
            init_list = [1, 2, 3] if graph[node]["color"] == "white" else [10, 11, 12]
            for _ in init_list:
                if go_to(graph2, node, _):
                    if node in left_n:
                        left_n.remove(node)
                    continue
                else:
                    left_n.append(node)
    left_nodes = list(dict.fromkeys(left_n))





def evaluator(graph2):    
    for n in left_nodes:
        l = []
        while not go_to(graph2,n,bfs(graph2,n,l)):
            if bfs(graph2,n,l) is None:
                move(graph2,n)
                update_left_nodes(graph2)
                break
            l.append(bfs(graph2,n,l))
    print(left_nodes,"finished")
    return
                       
                


def move( graph2 , node ):
    seq = {}
    choices = graph2[node]["neighbors"]
    random.shuffle(choices)
    l = None
    for l in choices:
        if graph2[l]["color"] == "":
            graph2[l]["color"] = graph2[node]["color"]
            graph2[node]["color"] = ""
            seq[graph2[l]["color"]] = [node,l]
            #if graph2[l]["color"] == "white":
                #tracker_w = []+
            break
    #draw_graph(graph2)
    if len(seq) > 0:
        sol_seq.append(seq)
    update_left_nodes(graph2)
    #evaluator(graph2)

        

def valid_path(graph2, path):
    for node in path[1:]:
        if graph2[node]["color"] != "":
            return node
    return 0


def go_to(graph2 , start , goal):
    if start == goal or goal is None:
        return False
    if graph2[goal]['color'] == "" and graph2[start]["color"] != goal_graph[start]["color"]:
        l,path = remaining_least_moves(graph2,start,goal)
        node = valid_path(graph2, path)
        if node != 0:
            print(sol_seq,node)
            #evaluator(graph2)
            return False
        else:
            sol_seq.append({graph2[start]["color"] : path})
            graph2[goal]["color"] = graph2[start]["color"]
            graph2[start]["color"] = ""
            return True
    else:
        return False

  

def solver():
    l = [1,2,3]
    w = []
    graph2 = graph.copy()    
    #draw_graph(graph)
    c = random.choice(l)
    move(graph2,c)
    update_left_nodes(graph2)
    evaluator(graph2)
    #draw_graph(graph2)
    #print(go_to())
    
    
    
    
    draw_graph(graph2)
    print(sol_seq)
    



solver()
