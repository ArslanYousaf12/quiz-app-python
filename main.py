class User:
    def __init__(self, user_id, user_name, ):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0
        print("Constructor function calling")
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(user_id=123, user_name="Arslan")


print(user_1.username)
user_2 = User(user_id=2223, user_name="kamran")

print(user_2.username)
user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)
