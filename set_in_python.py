# 1st topic
# correct way of creating an empty set
C= set()
print("the type of c is",type(C))
# wrong way of creating an empty set
D ={}
print("the type of D is:",type(D)) # it is the empty dictonary
thisset={45,50,39,27,56}
print(type(thisset))
#2nd method
# adding an element in a set
thisset.add(56)
print(set)
# 3rd method
# clearing a set
set2 = {"banana","mango","papaya"}
# clear using clear method
set2.clear()
# 4th method
# difference between two sets {difference()} The returned set contains items that exist only in the first set, and not in both sets.
set3 ={"box","book","mango"}
set4 = {"book","college","class"}
new = set3.difference(set4)
print(new)
# 5th method
# remove ther are the two  method (discard,remove) both used to remove an element from a set in Python, but they behave differently when the element to be removed is not present in the set.When you call the remove() method and the specified element is not present in the set, a KeyError exception is raised. On the other hand, if you call the discard() method and the specified element is not present in the set, no error is raised and the set remains unchanged
colors = {"green","blue","orange","yellow"}
colors.remove("green")
print(colors)
# 6th method intersection() method is used to find the common elements between two or more sets. It returns a new set that contains only the elements that are present in all of the specified sets.
my_friends = {"arjun","nikita","ashok","aditiya","rahul"}
your_friends = {"arjun","aditiya","Karan","Manoj","rahul","pankaj"}
common_friends =my_friends.intersection(your_friends)
print(common_friends)