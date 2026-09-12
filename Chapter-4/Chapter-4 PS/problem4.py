numbers=[]
numbers.append(int(input("ENTER THE FIRST NUMBER: ")))
numbers.append(int(input("ENTER THE SECOND NUMBER: ")))
numbers.append(int(input("ENTER THE THIRD NUMBER: ")))
numbers.append(int(input("ENTER THE FOURTH NUMBER: ")))
sum=numbers[0]+numbers[1]+numbers[2]+numbers[3]
# There is also a bulit-in function in python as sum(numbers)
print(f"SUM OF ALL 4 ELEMENTS OF LIST: {sum}")
