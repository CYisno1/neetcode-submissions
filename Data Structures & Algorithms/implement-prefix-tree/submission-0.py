class PrefixTree:

    def __init__(self):
        self.children = {}
        # children 用 dictionary 存『下一個字母』
        # node.children["a"] = 下一個node
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self

        for ch in word:
            if ch not in node.children:
                node.children[ch] = PrefixTree()            
            node = node.children[ch]
        
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self

        for ch in word:
            if ch not in node.children:
                return False
            
            node = node.children[ch]
        
        return node.is_end
        
    def startsWith(self, prefix: str) -> bool:
        node = self

        for ch in prefix:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return True
        
        
        