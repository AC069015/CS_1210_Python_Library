# Author: Anthony Cunningham Section A01
# Homeword 4

# Question 2

def q2List(n):
    recursiveList = []
    if n == 0:
        recursiveList.append(1)
    else:
        recursiveList.append(1)
        recursiveList.append((n + 1)**2)
        recursiveList.extend(q2List(n - 1))
    return recursiveList

# Question 3

def listsAreSimilar(list1, list2):
    if (len(list1) == 0) and (len(list2) == 0):
        print(True)
    elif (len(list1) == 0) and (len(list2) != 0):
        print(False)
    elif (len(list1) != 0) and (len(list2) == 0):
        print(False)
    else:
        if (type(list1[0]) != type(list2[0])):
            print(False)
            return
        elif (type(list1[0]) == type(list)):
            listInList1 = list1[0][:]
            listInList2 = list2[0][:]
            listsAreSimilar(listInList1, listInList2)
        else:
            listsAreSimilar(list1[1:], list2[1:])

    
    
