class Node:
    def __init__(self, key: int, val):
        self.key = key
        self.val = val
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, Node] = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next

        assert prev_node is not None
        assert next_node is not None

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node: Node) -> None:
        prev_node = self.right.prev
        assert prev_node is not None
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node
        prev_node.next = node
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        else:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
        
        return node.val        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

            if self.capacity < len(self.cache):
                lru = self.left.next
                assert lru is not None
                assert lru is not self.right
                
                self.remove(lru)
                del self.cache[lru.key]

            
        
