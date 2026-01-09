class Graph:
    def __init__(self , is_directed = False):
        self.is_directed = is_directed
        self.adj_list = {}

    def add_node(self , node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
    
    def del_node(self , node):
        if node not in self.adj_list:
            raise ValueError("Node doesn't exists")
        else:
            for key in self.adj_list:
                self.adj_list[key].discard(node)
            del self.adj_list[node]

    def add_edge(self , source , destination):
        if source not in self.adj_list:
            self.add_node(source)
        
        if destination not in self.adj_list:
            self.add_node(destination)

        self.adj_list[source].add(destination)
        if not self.is_directed:
            self.adj_list[destination].add(source)

    def del_edge(self , source , destination):
        if source not in self.adj_list:
            raise ValueError("Source node not found")
        
        if destination not in self.adj_list:
            raise ValueError("Destination node not found")
        
        self.adj_list[source].discard(destination)

        if not self.is_directed:
            self.adj_list[destination].discard(source)

    def bfs(self , start):
        if start not in self.adj_list:
            raise ValueError('Starting node not found')
        queue = [start]
        visited = []

        while len(queue) > 0:
            node = queue.pop(0)
            for neighbor in self.adj_list[node]:
                if neighbor not in queue and neighbor not in visited:
                    queue.append(neighbor)
            visited.append(node)
        return visited

    def dfs(self , start):
        if start not in self.adj_list:
            raise ValueError('Starting node not found')
        stack = [start]
        visited = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)

            for neighbor in self.adj_list[node]:
                if (neighbor not in stack) and (neighbor not in visited):
                    stack.append(neighbor)
        return visited 

   
graph = Graph()
for i in range(10):
    graph.add_node(i)

for i in range(1 , 10):
    graph.add_edge(0 , i)

print(graph.bfs((0)))
print(graph.dfs((0)))