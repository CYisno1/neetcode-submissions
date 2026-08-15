class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. 建 graph
        # graph[ch] = ch 後面必須出現的字母
        graph = {
            ch: set()
            for word in words
            for ch in word
        }

        # indegree[ch] =
        # 有多少字母必須排在 ch 前面
        indegree = {
            ch : 0
            for ch in graph
        }

        # 2. 比較每一對相鄰的 words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            min_len = min(len(word1), len(word2))

            # 特殊 invalid case
            # ["abc", "ab"] 不可能是正確 dictionary order
            if (
                len(word1) > len(word2)
                and word1[:min_len] == word2[:min_len]
            ):
                return ""
            
            # 找第一個不同的 character
            for j in range(min_len):
                ch1 = word1[j]
                ch2 = word2[j]

                # ch1 必須在 ch2 前面
                if ch1 != ch2:
                    if ch2 not in graph[ch1]:
                        graph[ch1].add(ch2)
                        indegree[ch2] += 1
                    # 只看第一個不同的位置
                    break
            
        # 3. Topological Sort
        queue = deque()

        # indegree = 0
        # → 沒有任何字母必須排在它前面
        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)

        result = []

        while queue:
            ch = queue.popleft()
            result.append(ch)

            for neighbor in graph[ch]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # 4. 如果沒有把所有字母放進 result
        # 代表 graph 裡有 cycle
        if len(result) != len(indegree):
            return ""
        
        return "".join(result)