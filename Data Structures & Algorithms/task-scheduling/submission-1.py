class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        heap = [-freq for freq in count.values()] # 放『現在立刻可以執行的 tasks』
        heapq.heapify(heap)

        queue = deque() # （剩下的freq, 還要等多久）放的是『還在 cooldown，暫時不能執行的 tasks』
        time = 0

        while heap or queue:
            time += 1

            if queue and queue[0][1] <= time:
                freq, ava_time = queue.popleft()
                heapq.heappush(heap, freq)
            
            if heap:
                freq = heapq.heappop(heap)
                freq += 1

                if freq < 0:
                    queue.append((freq, time + n + 1))
        
        return time
                

        
