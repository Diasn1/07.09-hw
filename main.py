list1 = [1,2,3,4,5,6,7]

def function(array):
    result = {}
    for digit in array:
        if digit % 2 != 0:
            result[digit] = digit**3
    return result

print(function(list1))

##############################################

list2 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

def function(array):

    result = []

    for digit in array:

        if digit % 2 == 0 and digit not in result:
            result.append(digit)

    return result

print(function(list2))

######################################################

function = lambda: [i*10 for i in range(0,10)]

print(function())