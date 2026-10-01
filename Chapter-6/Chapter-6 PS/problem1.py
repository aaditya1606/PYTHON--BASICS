num1=int(input("ENTER THE FIRST NUMBER: "))
num2=int(input("ENTER THE SECOND NUMBER: "))
num3=int(input("ENTER THE THIRD NUMBER: "))
num4=int(input("ENTER THE FOURTH NUMBER: "))
if(num1>num2 and num1>num3 and num1>num4):
    print(f"MAXIMUM NUMBER: {num1}")
elif(num2>num1 and num2>num3 and num2>num4):
    print(f"MAXIMUM NUMBER: {num2}")
elif(num3>num1 and num3>num2 and num3>num4):
    print(f"MAXIMUM NUMBER: {num3}")
else:
    print(f"MAXIMUM NUMBER: {num4}")
print("END OF THE PROGRAM!!")