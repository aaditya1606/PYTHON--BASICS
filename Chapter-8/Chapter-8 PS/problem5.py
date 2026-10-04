n=int(input("ENTER THE VALUE: "))
def printing(number):
    if(number==0):
        return
    i=0
    for i in range(number):
        print("* ",end=" ")
    print("\n")
    printing(number-1)
printing(n)