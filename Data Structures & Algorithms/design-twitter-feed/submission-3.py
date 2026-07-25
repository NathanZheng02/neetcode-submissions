class Twitter:

    def __init__(self):
        # Use time to determine most recent tweet
        self.time = 0
        self.follow_map = defaultdict(set) # {userId, set(followerId)}
        self.tweet_map = defaultdict(list) # {userId, [time, tweetIds]}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add (time, id) pair to tweet map
        self.tweet_map[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = [] # Heap based on time
        # User follow themselves
        self.follow_map[userId].add(userId)

        # Iterate through people the user follows
        for followee_id in self.follow_map[userId]:
            # Check to see if the followed person has tweets
            if followee_id in self.tweet_map:
                last_idx = len(self.tweet_map[followee_id]) - 1
                time, tweet_id = self.tweet_map[followee_id][last_idx]
                min_heap.append([time, tweet_id, followee_id, last_idx - 1])
        heapq.heapify(min_heap)

        # Returning 10 recent tweets
        while min_heap and len(res) < 10:
            time, tweet_id, followee_id, idx = heapq.heappop(min_heap)
            res.append(tweet_id)
            if idx >= 0:
                time, tweet_id = self.tweet_map[followee_id][idx]
                heapq.heappush(min_heap, [time, tweet_id, followee_id, idx - 1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # Adding to follow map
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove from follow map
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
