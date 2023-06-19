list_name = ["akash", "msihra", 1, 23.0]
print(list_name)

list()  # function method
# which is faster [] one

# operations in list[]
# empty list
players = []


for i in range(0, 5):
    name = input("enter player's name ")
    players.append(name)

print(players)


# clear

# print(players.clear())

# counting a particular number

num = [1, 2, 3, 3, 3, 4, 5]
print(num.count(3))


# add multiple lists
# l = num + players
num.extend(players)
print(num)
