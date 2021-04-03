def printAr(array):
    for el in array:
        print(el)


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
Maze[agent_loc[0]] = copy
for el in Maze:
    for el1 in el:
        print(el1,end='')
    print("")

print("")
copyArray = [Maze[agent_loc[1]-1],Maze[agent_loc[1]],Maze[agent_loc[1]+1]]
action = 0  #UP
#action = 1 #DOWN

if (action == 0):
    index = copyArray[1].find("S")
    
    stringList0 = list(copyArray[0])
    stringList1 = list(copyArray[1])
   
    stringList0[index] = 'S'
    stringList1[index] = ' '
    copyArray[0] = ''.join(stringList0)
    copyArray[1] = ''.join(stringList1)
    Maze[agent_loc[1]-1] = copyArray[0]
    Maze[agent_loc[1]] = copyArray[1]
    
print("")
for el in Maze:
    for el1 in el:
        print(el1,end='')
    print("")

print("")


