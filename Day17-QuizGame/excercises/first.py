# class User:
#     pass

class SimpleUser:
    def __init__(self):
        print("New user has been created...")


simple_user_1 = SimpleUser()
simple_user_1.id = "001"
simple_user_1.username = "Mike"

print(f"id: {simple_user_1.id} - {simple_user_1.username}")

simple_user_2 = SimpleUser()
simple_user_2.id = "002"
simple_user_2.username = "Jack"

print(f"id: {simple_user_2.id} - {simple_user_2.username}")


############################################################



class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("003", "Angela")
user_2 = User("004", "Manuel")

print(f"New user type: {user_1.id} - {user_1.username} - starts with {user_1.followers} followerss")

user_1.follow(user_2)

print(f"user {user_1.username} is followed by {user_1.followers} person")
print(f"user {user_1.username} follows {user_1.following} person")

print(f"user {user_2.username} is followed by {user_2.followers} person")
print(f"user {user_2.username} follows {user_2.following} person")