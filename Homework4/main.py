
# declare global list variable
myUniqueList = []
myLeftovers = []


# add value to unique list
def addToList(x):
    if x in myUniqueList:
        addtoBin(x)
        return False
    else:
        myUniqueList.append(x)
        return True

# discarded value gets added to leftovers list


def addtoBin(x):
    myLeftovers.append(x)


print(myUniqueList)  # test value
addToList(0)  # first append
addToList(1)
addToList(1)  # check addtoBin function
print('check if duplicate values are moved to leftovers')
print(myUniqueList)  # check if duplicate values discarded
print(myLeftovers)   # check duplicate bin append
# appending values
print('append values')
addToList(2)
addToList(3)
addToList(4)
print('recheck if duplicates are moved')
# recheck if duplicate values are moved to leftovers
addToList(1)
addToList(2)
print(myUniqueList)
print(myLeftovers)
