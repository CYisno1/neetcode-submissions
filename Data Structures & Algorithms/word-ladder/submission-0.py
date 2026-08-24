from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 先建一個 map: pattern → 所有符合這個 pattern 的 words
        # *ot -> hot, dot, lot
        # h*t, ho*每個位置都試一遍

        pattern_map = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_map[pattern].append(word)

        # 準備 BFS
        queue = deque([beginWord])
        visited = set([beginWord]) 
        level = 1

        while queue:
            # 只處理目前這一層
            for _ in range(len(queue)):
                current = queue.popleft()

                # 如果目前 word 就是 endWord
                if current == endWord:
                    return level

                for i in range(len(current)):
                    c_pattern = current[:i] + "*" + current[i + 1:]

                    for neighbor in pattern_map[c_pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            
            # 目前這一整層走完
            # 下一輪就是下一層
            level += 1
        
        # queue 都空了還找不到 endWord
        return 0

