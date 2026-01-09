
class DisjointSet:
    def __init__(self):
        self.vertices = {}
    
    def make_set(self , vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}
            self.vertices[vertice]["parent"] = vertice
            self.vertices[vertice]["rank"] = 0

    def find(self , vertice):
        if vertice not in self.vertices:
            self.make_set(vertice)
        
        if self.vertices[vertice]["parent"] == vertice:
            return vertice
        
        else:
            self.vertices[vertice]["parent"] = self.find(self.vertices[vertice]["parent"])
        return self.vertices[vertice]["parent"]
    
    def union(self , u , v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return False
        if self.vertices[root_u]["rank"] < self.vertices[root_v]["rank"]:
            self.vertices[root_u]["parent"] = root_v
        
        elif self.vertices[root_u]["rank"] > self.vertices[root_v]["rank"]:
            self.vertices[root_v]["parent"] = root_u
        
        elif self.vertices[root_u]["rank"] == self.vertices[root_v]["rank"]:
            self.vertices[root_u]["parent"] = root_v
            self.vertices[root_v]["rank"] += 1
        return True

if __name__ == "__main__":
    dis_set = DisjointSet()
    set_items = [i for i in range(10)]
    for i in set_items:
        dis_set.make_set(i)

    dis_set.union(1 , 2)
    dis_set.union(2 , 3)
