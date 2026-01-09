class Graph:
    def __init__(self , is_directed = False) ->None:

        self.is_directed = is_directed
        self.adj_list = {}

    def add_node(self , node) ->None:

        if node not in self.adj_list:
            self.adj_list[node] = set()

    def del_node(self , node) ->None:

        if node not in self.adj_list:
            raise ValueError("Node doesn't exists")
        
        else:
            for key in self.adj_list:
                self.adj_list[key] = set(
                    (dst , w) for (dst , w) in self.adj_list[key] if dst != node
                )
            del self.adj_list[key]
    
    def add_edge(self , source , destination , weight:int = 0) ->None:

        if source not in self.adj_list:
            self.add_node(source)
        
        if destination not in self.adj_list:
            self.add_node(destination)
        
        self.adj_list[source].add((destination , weight))

        if not self.is_directed:
            self.adj_list[destination].add((source , weight))

    def del_edge(self , source , destination) ->None:

        if source not in self.adj_list:
            raise ValueError('Source node not found')
        
        if destination not in self.adj_list:
            raise ValueError("Destination node not found")
        
        self.adj_list[source] = set(
            (dst , w) for (dst , w) in self.adj_list[source] if dst != destination
        )

        if not self.is_directed:
            self.adj_list[destination] = set(
                (src , w) for (src , w) in self.adj_list[destination] if src != source
            )

    def bfs(self , start):
        if start not in self.adj_list:
            raise ValueError("Starting node not found")
        queue = []
        visited = []
        while queue:
            node = queue.pop(0)
            for src , w in self.adj_list[node]:
                if (src not in queue) and (src not in visited):
                    queue.append(src)
            visited.append(node)
    def view_graph(self):
        return self.adj_list
        
graph = Graph()

for i in range(10):
    graph.add_node(i)

weight = 5
for i in range(1 , 10):
    graph.add_edge(0 , i , weight)
    weight += 5

print(graph.view_graph())
