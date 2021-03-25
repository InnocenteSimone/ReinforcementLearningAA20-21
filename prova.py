Maze = [
    "|----------|",
    "|    E     |",
    "|          |",
    "|          |",
    "|          |",
    "|    S     |",
    "|----------|",
]

agent_loc = (5,5)
exit_loc = (1,5)
for el in Maze:
    for el1 in el:
        print(el1,end='')
    print("")
print("\n")
copy = Maze[agent_loc[0]]
print(copy)
print("\n")

index = copy.find("S") + 1
stringList = list(copy)
stringList[index-1] = ' '
stringList[index] = "S"
copy = ''.join(stringList)




print(copy)
print("\n")

Maze[agent_loc[0]][agent_loc[1]].replace("S"," ")
Maze[agent_loc[0]][agent_loc[1]+1].replace(" ","S")


for el in Maze:
    for el1 in el:
        print(el1,end='')
    print("")
