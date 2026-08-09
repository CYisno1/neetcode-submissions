class WordDictionary:

    def __init__(self):
        self.children = {} # key: ch; value: next node
        self.is_end = False
        
    def addWord(self, word: str) -> None:
        node = self

        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
                
            node = node.children[ch]
        
        node.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.is_end
        
            ch = word[i] 
        # 如果現在遇到 "."，它可以代表任何字母，所以我要嘗試目前 node 的每一個 child。
        # 只要其中任何一條路最後成功找到完整 word，就回傳 True。
        # 如果所有 child 都失敗，才回傳 False。

            if ch == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                
                return False
            
            else:
                if ch not in node.children:
                    return False
                
                return dfs(i + 1, node.children[ch])
                        
        return dfs(0, self)
        
