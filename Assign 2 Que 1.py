given_input = "Python is a case sensitive language"
print(given_input)

#1(a)
# len() function gives the length of string
str_length = len(given_input)

print("Length of the string is:", str_length)

#1(b)
#reverse string
str_reverse = given_input[::-1]
print("The reversed string is:",str_reverse)

#1(c)
#Using slice to store a part of string in a variable
# printing “a case sensitive”
str_slice = given_input[10:27]
print(str_slice)

#1(d)
#repalcing the stored sliced string.
replaced_str = given_input.replace(str_slice, "object oriented")

print(replaced_str)

#1(e)
#Index of "a"
index_a = given_input.find("a")
print('Index of "a" substring in input string is:',index_a)

#1(f)
#Replacing spaces with empty quotes
without_spaces = given_input.replace(" ", "")
print(without_spaces)