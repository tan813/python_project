with open('./test1.txt','r') as file:
    data = file.read()
    #data1 = file.readline()
   # data2 = file.readlines()

users = []
for line in data:
    print(line)
    user = line[:-1].split(":")
    users.append(user)
print(data)
print(users)