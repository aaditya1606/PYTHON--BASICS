Name="Harry"
print(Name)
# Name is the string with length 5 and the indexing starts from 0 and ends at length-1
lengthofstring=len(Name)
print(f"Length of the string: {lengthofstring}")
# Slicing of the Strings
# Since the Strings are immutable so we can not change the individual character of the string rather we have to change the complete string
string='''Aaditya'''
character1=string[3]
print(string)
print(character1)
print(string[0:4])
# 0:4 - Here the first number i.e. 0 is the starting index which is included whereas the second number is the last index which is excluded
print(Name[-3])
# Negative indexing is also possible and it starts from -1 from the right side and ends at length
string='''AadityaShakya'''
print(string[2:7])
print(string[:7])
print(string[0:])
print(string[4:])
print(string[-6:-2])
print(string[-6:])
# Slicing with skipping values
name='Aaaditya'
print(name[1:7:2])
