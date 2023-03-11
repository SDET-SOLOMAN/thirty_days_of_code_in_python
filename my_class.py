class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.following = 0
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User('1', "Angel")
user2 = User('2', "Mark")
user1.follow(user2)

