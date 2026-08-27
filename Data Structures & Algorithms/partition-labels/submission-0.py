class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 我一路往右走，記錄目前遇到的所有字母中，「最晚的最後出現位置」。當我真的走到那個位置時，就可以切一刀。

        # Step 1: 記錄每個字母最後一次出現的位置
        last = {}

        for i, char in enumerate(s):
            last[char] = i
        
        # Step 2: 從左到右決定每一段的範圍
        result = []
        start = 0
        end = 0
        # end: 目前這一整段裡，我看過的所有字母，最遠必須走到哪裡。

        # 真的從左往右走，決定 partition
        for i, char in enumerate(s):
            end = max(end, last[char])

            # 我現在終於走到目前這一段所有字母需要涵蓋的最遠位置了。
            if i == end:
                result.append(end - start + 1)
                # 切完之後 下一段從下一個位置開始
                start = i + 1
        
        return result