from Garrafa import Garrafa
from Filosofo import Filosofo
FilePath = "./graph2.txt"

content = open(FilePath, "r")

graph = []


for line in content:
    l = line.replace('\n', '').split(",")
    graph.append(l)


if __name__ == '__main__':
    
    nFilosofos = len(graph)
    bebidas = set({})
    filosofos: list[Filosofo] = []
    
    count = 0
    for i in range(nFilosofos):
        filosofos.append(Filosofo(i, "Filosofo" + str(i), graph[i], list(bebidas)))
        for j in range(nFilosofos):
            if graph[i][j] == '1':
                count += 1
    
    for i in range(int(count / 2)):
        bebidas.add(Garrafa(i))
    
    for filosofo in filosofos:
        filosofo.garrafas = list(bebidas)
        filosofo.start()
    
        