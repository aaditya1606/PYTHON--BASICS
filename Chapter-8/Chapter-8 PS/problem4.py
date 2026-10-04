n=int(input("ENTER THE NUMBER: "))
def sum(number):
    if(number==1):
        return 1
    else:
        return number+sum(number-1)
print(f"SUM OF {n} Natural numbers: {sum(n)}")