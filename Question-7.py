#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has
# only the even elements of this list in it

c=[]
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for x in a: 
    if(x % 2 == 0):
        c.append(x)
print("New list containing only even numbers is : ",c)