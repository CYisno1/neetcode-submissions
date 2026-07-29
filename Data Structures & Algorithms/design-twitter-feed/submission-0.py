class Twitter:

    def __init__(self):
        # 用 time 判斷 tweet 的發布順序。
        self.time = 0
        # userId -> [(timestamp, tweetId), ...]
        self.tweets = defaultdict(list)
        # followerId -> {followeeId, followeeId, ...}
        self.following = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        heap = []

        # self.following[userId] 是使用者 follow 的人。
        # {userId} 是使用者自己。
        # | 是 set union，會把兩個 set 合併。
        users = self.following[userId] | {userId}

        # 把每個 user 最新的一篇 tweet 放進 heap
        for user in users:
            tweets = self.tweets[user]

            if tweets:
                index = len(tweets) - 1 # 最後一個是最新的tweet
                time, tweet_id = tweets[index]

                # heap 裡面的 tuple 儲存四個資訊：
                # 1. -time：
                #    讓最新的 tweet 最先被 pop。
                #
                # 2. tweet_id：
                #    最後要加入 result。
                #
                # 3. user：
                #    知道這篇 tweet 是哪個 user 發的。
                #
                # 4. index：
                #    知道這篇 tweet 在該 user 的 list 中的位置。
                #
                # user 和 index 很重要，
                # 因為 pop 出這篇之後，
                # 我們要去找同一個 user 的下一篇較舊 tweet。
                heapq.heappush(
                    heap,
                    (-time, tweet_id, user, index) # max heap
                )

        # 只要 heap 還有 tweet，
        # 而且 result 還沒有收集到 10 篇，
        # 就繼續從 heap 取出最新 tweet。
        while heap and len(result) < 10:
            neg_time, tweet_id, user, index = heapq.heappop(heap)
            result.append(tweet_id)
        
            # 目前這篇 tweet 在 index 位置。
            # 同一個 user 的下一篇較舊tweet就在 index - 1 的位置。
            previous_index = index - 1

            # 如果 previous_index >= 0，
            # 代表這個 user 還有更舊的 tweet。
            if previous_index >= 0:
                # 取出同一個 user 的下一篇較舊 tweet。
                previous_time, previous_tweet_id = (
                    self.tweets[user][previous_index]
                )

                # 把這篇較舊 tweet 放入 heap，
                # 讓它和其他使用者的 tweets 比較時間。
                heapq.heappush(
                    heap,
                    (
                        -previous_time,
                        previous_tweet_id,
                        user,
                        previous_index
                    )
                )

        # 最後回傳最多 10 個 tweetId。
        return result



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            # 把 followeeId 加進 followerId 的 following set。
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        # 用discard因為：如果 followeeId 不存在，不會報錯。
        
