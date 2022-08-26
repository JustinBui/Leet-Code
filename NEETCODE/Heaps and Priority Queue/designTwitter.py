from collections import deque

class Twitter:

    def __init__(self):
        self.database = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not database.get(userId):
            database[userId] = deque()
        database[userId].appendleft((userId, tweetId)) # Tuple pair for (userId, TweetID)

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds = database[userId]
        res = []
        for i in range(10):
            if i == len(feeds):
                break
            res.append(feeds[i])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        

    def unfollow(self, followerId: int, followeeId: int) -> None: