# Data structure array
first_array = [8,33,1,6,7656,100000,3 ,762435163,2,-9006]

# 1) find the smallest number in an array
minValue = first_array[0]
for i in first_array:
    if i < minValue:
        minValue = i
print("Minimum value ", minValue)


# 2) find largest number in array
maxValue = first_array[0]
for i in first_array:
    if i > maxValue:
        maxValue = i
print("Maximum value ", maxValue)

# 3) find the sum of all elements in the array and calculate the average
#thoughts:
#total = 0
#for loop i in numbers
#total = total + i
#print total

numbers = [12, 45, 7, 89, 23, 4, 56, 78, 9, 33]
total = 0
for i in numbers:
    total = total + i
average = total/len(numbers)
print("sum of all elements is ", total)
print("average is ", average)

# 4) count elements above average
#thoughts
# need a variable 'counter' to keep track of total elements above average
#for i in numbers
# if i > average
# counter +=1

counter=0
for i in numbers:
    if i > average:
        counter += 1
print("number of elements above average is ", counter)