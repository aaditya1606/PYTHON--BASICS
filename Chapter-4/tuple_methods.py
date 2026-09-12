tuple=(2,"Aaditya",6.7,None,False,5,19,2)
# COUNT
count=tuple.count(2)
print(count)
# INDEX
index=tuple.index(6.7)
print(index)
# CONCATENATION
tuple1=(1,3.5,"Aaditya",False)
tuple2=(5,True,None)
concatenated=tuple1+tuple2
print(concatenated)
# REPETITION
repeated=tuple1*3
print(repeated)
# MEMBERSHIP
print(2 in tuple1)
print(3.5 in tuple1)
# LENGTH
print(len(tuple1))
# MIN AND MAX
sample=(3,7,2,111,29,99)
print(min(sample))
print(max(sample))
# SLICING
sliced=sample[1:4]
print(sliced)
# UNPACKING-EACH ELEMENT OF THE TUPLE CAN BE ASSIGNED TO INDIVIDUAL VARIABLE
a,b,c=sample[1:4]
print(a)
print(b)
print(c)