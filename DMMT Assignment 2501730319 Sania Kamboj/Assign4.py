
# BST IMPLEMENTATION

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=" ")
            self._inorder(node.right)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Case 1 & 2
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Case 3 (two children)
            min_larger = self._min_value(node.right)
            node.key = min_larger.key
            node.right = self._delete(node.right, min_larger.key)

        return node

    def _min_value(self, node):
        while node.left:
            node = node.left
        return node

# GRAPH (Adjacency List)

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def print_graph(self):
        for node in self.graph:
            print(node, "->", self.graph[node])

    def bfs(self, start):
        visited = set()
        queue = [start]

        print("BFS:", end=" ")
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbor, _ in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        print()

    def dfs(self, start):
        visited = set()
        print("DFS:", end=" ")
        self._dfs(start, visited)
        print()

    def _dfs(self, node, visited):
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor, _ in self.graph.get(node, []):
                self._dfs(neighbor, visited)


# HASH TABLE (Separate Chaining)

class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return

    def display(self):
        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)



# MAIN TESTING

if __name__ == "__main__":

    print("\n--- BST ---")
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]

    for v in values:
        bst.insert(v)

    print("Inorder:", end=" ")
    bst.inorder()

    print("Search 20:", bst.search(20))
    print("Search 90:", bst.search(90))

    print("Delete 20 (leaf)")
    bst.delete(20)
    bst.inorder()

    bst.insert(65)
    print("Delete 60 (one child)")
    bst.delete(60)
    bst.inorder()

    print("Delete 50 (two children)")
    bst.delete(50)
    bst.inorder()

    print("\n--- GRAPH ---")
    g = Graph()
    edges = [
        ('A','B',2), ('A','C',4), ('B','D',7), ('B','E',3),
        ('C','E',1), ('D','F',5), ('E','D',2), ('E','F',6), ('C','F',8)
    ]

    for u, v, w in edges:
        g.add_edge(u, v, w)

    g.print_graph()
    g.bfs('A')
    g.dfs('A')

    print("\n--- HASH TABLE ---")
    ht = HashTable(5)

    keys = [10, 15, 20, 7, 12]
    for k in keys:
        ht.insert(k, k*10)

    ht.display()

    print("Get 10:", ht.get(10))
    print("Get 7:", ht.get(7))
    print("Get 12:", ht.get(12))

    print("Delete 15")
    ht.delete(15)
    ht.display()