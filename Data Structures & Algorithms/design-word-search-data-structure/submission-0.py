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
            # i = 現在正在檢查 word[i]
            # node = 目前 Trie 走到哪個 node

            if i == len(word):
                return node.is_end

            ch = word[i]

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