class User:
    def __init__(self, user_id, user_name, ):
        self.id = user_id
        self.username = user_name
        print("Constructor function calling")


user_1 = User(user_id=123, user_name="Arslan")

print(user_1.username)
user_2 = User(user_id=2223, user_name="kamran")

print(user_2.username)
