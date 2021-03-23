import os

with open('./11.txt', 'r') as fp:
    data = fp.readlines()
    print(data)
    users = []
    for line in data:
        user = line[:-1].split(":")
        users.append(user)

print(users)
