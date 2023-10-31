def main()
    G =read_graph()
    start = input ("С какой вершины начать?")
    while start not in G:
        start = input("Такой вершины  графе нет."+
                      "С какой вершины начать?")
        shortest_distances =dijkstra (G, start)
        finish = input ("К какой вершине построить путь?")
        while start not in G:
            star =  input("Такой вершины  графе нет."+
                      "К какой вершине построить путь?")
        shortest_path = reveal_shortest_path (start, finish, shortest_distances)

def read_graph():
    M= int(input()) #M кол-во ребер, далее - строки "А Б вес"
    G= {}
    for i in range (M):
        a, b, weight = input).split()
        weight = float(weight)
        add_edge(G, a, b, weight)
        add_edge (G, b, a, weight)
    return G

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b:weight}
    else:
        G[a][b] = weight




def dijkstra((G, start)):
    Q = deque()
    S = {}
    S[start]=0
    Q.push(start)
    while Q:
        v = Q.pop
        for u in G[v]:
            if u not in s or s[v]+ G[v][u] < s[u]:
                s[u] =s[v]+G[v][u]
                Q.push(u)




if __name__ =="__main__":
    main()

