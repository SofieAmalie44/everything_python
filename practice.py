newList = ["hej", "med", "dig", "homie"]

print(newList[0:3]);
print(newList[-3:-1]);

print(newList[:] is newList)

a = newList[0:3]
b = newList[-3:0]

print("test" , newList[3::-2])
print(newList[1:0:-1])

inAndNotInOperators = 'hej' in newList

print(inAndNotInOperators)

concatenationOperators = newList + ["går", "det", "godt"]

print(concatenationOperators)

replicationOperators = newList * 2

print(replicationOperators)

# len(), min(), max() functions

print(len(newList))

print(min(newList))

print(max(newList))

# operating a newList literal (but always assign a newList to a variable tho!)

print(newList[::-1])

print(len(newList[::-1]))

# you can do likewise with a string literal

print("hejsa sin lækre skid"[::-1])  # reverses the string literal



# sets

newSet = set(["oi", "tudo", "bem", "lindo"])



name = "johan"

makeList = list(name)

print(makeList)

makeSet = set(name)

print(makeSet)



test = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(test[-5:-3])
print(test[:] is test)
print(test[4::-2])
print(test[-6])
print(max(test[2:4] + ['grault']))

inTo = len(test) //  2
print(test[inTo:])

print(len(test))

x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']

print(x[1][2][1::1])

r = [1, 2, 3, 4, 5]

del r[2]

print(r)

add = ['a', 'b', 'c']
add[-1:] = ['d', 'e']
print(add)

n = [1, 2, 7, 8]
n[2:2] = [3, 4, 5, 6]
print(n)


y = 5
i = -5



print((i, y)[::-1])

wordList = ['mix', 'tix', 'xis', 'xim', 'xit', 'six']

def front_x(words):
    # +++your code here+++
    xStrings = []
    otherStrings = []

    for word in words:
        if word[0] == 'x':
            xStrings.append(word)
        else:
            otherStrings.append(word)

    return sorted(xStrings) + sorted(otherStrings)

result = front_x(wordList)
print(result)


listOfTuples = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]

def sort_last(tuples):
   
    return sorted(tuples, key=lambda x: x[-1])

result = sort_last(listOfTuples)
print(result)  


def remove_adjacent(nums):
    if not nums:
        return ()
    
    result = [nums[0]] 
    

    for num in nums[1:]:
        if num != result[-1]:
            result.append(num)
    
    return tuple(result)



print(remove_adjacent([1, 2, 2, 3]))  
print(remove_adjacent([2, 2, 3, 3, 3])) 
print(remove_adjacent([]))  


l1 = [3, 1, 4, 5, 6]
l2 = [2, 7, 8, 9]

def linear_merge(list1, list2):
    # Sort both lists
    sortedList1 = sorted(list1)
    sortedList2 = sorted(list2)
    
    merged_list = []
    i = 0
    j = 0
    

    while i < len(sortedList1) and j < len(sortedList2):
        if sortedList1[i] < sortedList2[j]:
            merged_list.append(sortedList1[i])
            i += 1
        else:
            merged_list.append(sortedList2[j])
            j += 1
    
    while i < len(sortedList1):
        merged_list.append(sortedList1[i])
        i += 1
    
   
    while j < len(sortedList2):
        merged_list.append(sortedList2[j])
        j += 1
    
    return merged_list

result = linear_merge(l1, l2)
print(result)
