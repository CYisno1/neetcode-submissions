class Twitter:

    def __init__(self):
        self.time = 0
        # userId -> [(timestamp, tweetId), ...]
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = [] # tweets ids
        heap = [] # latest tweets from each user

        users = self.following[userId] | {userId}

        for user in users:
            user_tweets = self.tweets[user]

            if user_tweets:
                index = len(user_tweets) - 1
                time, tweet_id = user_tweets[index]

                heapq.heappush(heap, (-time, user, tweet_id, index))
        
        while heap and len(result) < 10:
            neg_time, user, tweet_id, index = heapq.heappop(heap)
            result.append(tweet_id)
        
            pre_index = index - 1

            if pre_index >= 0:
                pre_time, pre_tweet_id = self.tweets[user][pre_index]
            
                heapq.heappush(heap, (-pre_time, user, pre_tweet_id, pre_index))

        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        