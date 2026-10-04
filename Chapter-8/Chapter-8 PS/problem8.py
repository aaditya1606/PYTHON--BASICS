n=int(input("ENTER THE NUMBER WHOSE TABLE IS TO BE PRINTED: "))
def table(number,i):
    if(i==11):
        return 0
    else:
        print(f"{number} x {i} = {number*i}")
        table(number,i+1)
i=1
table(n,i)