class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1





user1 = User("001", "Sunny")
user2 = User("002", "Sticky")
user2.follow(user1)
user1.follow(user2)
print(user1.user_id, user1.username, user1.following, user1.followers)
print(user2.user_id, user2.username, user2.following, user2.followers)