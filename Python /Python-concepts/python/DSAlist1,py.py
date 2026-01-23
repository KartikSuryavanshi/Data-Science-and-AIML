#creating null list
mylist=[]

#adding elements
mylist.append(10)
mylist.append(20)
mylist.append(30)
mylist.append(40)
mylist.append(50)
mylist.append(60)
mylist.append(70)

print("After adding elements:",mylist)
print("**********************************************")
print("BUILT IN FUNCTIONS")
#finding  max in list
print(max(mylist))
print(min(mylist))
print(len(mylist))
print(sum(mylist))
print("**********************************************")
#deleting elements
print("pop element is :",mylist.pop(2))
print("**********************************************")
del(mylist[1])
print("After del elements:",mylist)
print("**********************************************")
#updating list
list1=[10,'one',20,30,40,'two']
print(list1[-2])
print(list1[1])
list1[1]=[5,11]
print(list1)
list1[4:4]=[7,9]
print(list1)
print("**********************************************")
list1.extend([40, 50])
print("After extending:", list1)
list1.insert(4,90)
print("After inserting:", list1)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)
# Creating a list with repetition
repeated_list = [0] * 5
print("Repeated list:", repeated_list)

