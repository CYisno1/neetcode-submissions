class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev: Optional["Node"] = None # 可以是一個 Node，也可以是 None
        self.next: Optional["Node"] = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, Node] = {}

        # 建立兩個 dummy node
        # left 代表最久沒用的那一端
        # right 代表最近使用的那一端
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        """
        把某個 node 從 doubly linked list 裡移除。
        原本：
        prev <-> node <-> next

        移除後：
        prev <-> next
        """

        prev_node = node.prev
        next_node = node.next

        # 這裡是為了讓 type checker 知道它們不會是 None
        # 因為我們只會移除真正存在於 list 中的 node，不會移除 dummy node
        assert prev_node is not None
        assert next_node is not None

        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert(self, node: Node) -> None:
        """
        把 node 插到最右邊，也就是 most recently used 的位置。

        原本：
        ... <-> prev <-> right

        插入 node 後：
        ... <-> prev <-> node <-> right
        """

        prev_node = self.right.prev

        # right.prev 一定會存在，至少會是 left
        assert prev_node is not None

        node.prev = prev_node
        node.next = self.right

        prev_node.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # 這個 key 被使用了，所以它變成 most recently used
        self.remove(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        """
        放入或更新 key-value。

        如果 key 已經存在：
        1. 更新 value
        2. 移到最右邊，因為它剛剛被使用

        如果 key 不存在：
        1. 建立新 node
        2. 放進 hashmap
        3. 插到最右邊

        如果超過 capacity：
        1. 刪掉最左邊的真正 node，也就是 least recently used
        """

        if key in self.cache:
            node = self.cache[key]
            node.val = value       

            # 更新過的 key 也算最近使用
            self.remove(node)
            self.insert(node)

        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

            # 如果超過容量，要刪掉 least recently used
            if len(self.cache) > self.capacity:
                lru = self.left.next

                # left.next 應該是真正的 LRU node
                assert lru is not None
                assert lru is not self.right

                self.remove(lru)

                # hashmap 裡也要刪掉這個 key
                del self.cache[lru.key]
        
