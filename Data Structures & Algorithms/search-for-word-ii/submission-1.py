class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # complete word, can add into output

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

         # 1. 建立 Trie root
        root = TrieNode()

        # 2. 把所有 words 放進 Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                
                node = node.children[ch]
        
            # 走完整個 word
            node.word = word
        
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, node):
            ch = board[row][col]

            # 如果這個字母不是目前 Trie node 的 child
            # 代表目前這條 path 不可能形成任何 word
            if ch not in node.children:
                return
            
            # Trie 往下一層
            next_node = node.children[ch]

            # 4. 如果目前已經形成完整 word
            if next_node.word is not None:
                res.append(next_node.word)

                # 避免同一個 word 被重複加入
                next_node.word = None

            
            # backtracking
            # choose board[row][col]
            board[row][col] = "#"
            # 上
            if row - 1 >= 0 and board[row - 1][col] != "#":
                dfs(row - 1, col, next_node)

            # 下
            if row + 1 < rows and board[row + 1][col] != "#":
                dfs(row + 1, col, next_node)

            # 左
            if col - 1 >= 0 and board[row][col - 1] != "#":
                dfs(row, col - 1, next_node)

            # 右
            if col + 1 < cols and board[row][col + 1] != "#":
                dfs(row, col + 1, next_node)

            # unchoose board[row][col]
            board[row][col] = ch

        # 5. 每一格都當起點
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return res            








            




        