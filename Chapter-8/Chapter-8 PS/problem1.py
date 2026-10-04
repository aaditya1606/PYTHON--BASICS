def greatest(a,b,c):
    if(a>b and b>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c
num1=int(input("ENTER THE FIRST NUMBER: "))
num2=int(input("ENTER THE SECOND NUMBER: "))
num3=int(input("ENTER THE THIRD NUMBER: "))
greatest_number=greatest(num1,num2,num3)
print(f"MAXIMUM NUMBER OUT OF ALL THE THREE GIVEN NUMBERS: {greatest_number}")
print("END OF THE PROGRAM!!")   