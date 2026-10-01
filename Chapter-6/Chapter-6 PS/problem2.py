physics=int(input("ENTER YOUR MARKS IN PHYSICS: "))
chemistry=int(input("ENTER YOUR MARKS IN CHEMSITRY: "))
maths=int(input("ENTER YOUR MARKS IN MATHS: "))
sum=physics+chemistry+maths
final=sum/3
if(final>=40 and physics>=33 and chemistry>=33 and maths>=33):
    print("PASS!!")
else:
    print("FAIL!!")
print("END OF THE PROGRAM!!")