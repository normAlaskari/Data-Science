
print("---------------------------String--------------------------\n")
# Creating a string “Welcome to Python Programming”
string = "Welcome to Python Programming"

# Output the string using the function Print
print(string)
# Output the substring from indexes 11 to 16.
print(string[11:17])
# Output the substring of the last 5 characters
print(string[-5:])
# Replace the substring “Programming” with “Environment”
print(string.replace("Programming", "Environment"))

print("\n")


print("---------------------------list--------------------------\n")
# Create an empty list 
lists = []
# add 1 to the list
lists.append(1)
# add 2 to the list
lists.append(2)
# add 3 to the list
lists.append(3)
# add 4 to the list
lists.append(4)

#diffrent ways of adding elements to list
#for i in range(1,5):
#    lists.append(i)
#lists = [i+1 for i in range(5)]

#concanting tuple (5,6) to the end
lists.extend((5,6))
#concanting tuple ["perfect", "wonderful"] to the end
lists.extend( ["perfect", "wonderful"])
#print the List
print(lists)
#concanting List of list [[7, 8], [9, 10]] to the end
lists.extend([[7, 8], [9, 10]])
#print the List
print(lists)

#concanting the list [ 8.5, 7,"code","software"] to the end
lists.extend([ 8.5, 7,"code","software"])

#print the last five elements
print(lists[-5:])

#deleting elements from 3 to 6
del lists[3:7]

print("\n")

print("---------------------------tuple--------------------------\n")
#Create a a_tuple Tuple1 using the list with elements 1, 2, 3, 4
a_tuple = tuple([1,2,3,4])

#Create a b_tuple Tuple1 with elements ("python","for","Kids")
b_tuple = ("python","for","Kids")

#adding b_tuple to end of a_tuple
a_tuple = a_tuple + (b_tuple ,)

print("This is full a_tuple: ", a_tuple)

#print the a_tuple starting from the 3rd elements
print("this a_tuple starting from the 3rd elements", a_tuple[3:])

print("\n")
print("---------------------------Dictionary--------------------------\n")

# Create an empty dict
empty_dict = {}

# add "python" to the dict
empty_dict[0] = "python"
# add "Programming to the dict
empty_dict[1] = "Programming"
# add "Funny to the dict
empty_dict[2] = "Funny"
# assigning "is very" to the dict
empty_dict[1] = "is very"

#print all keys
print(empty_dict.keys())
#print all value
print(empty_dict.values())

#deleting elements 2
del empty_dict[2]

#check if 2 exist in the dict
print("Dose element 2 exist in empty_dict ?", 2 in empty_dict)

# Convert the values in the dictionary Dict to a list and output the result
List_dict = list(empty_dict.values())

#print the List
print(List_dict)

print("\n")
print("---------------------------Done--------------------------\n")
