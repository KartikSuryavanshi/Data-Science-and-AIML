'''the set data structure n python prorgamming is implemented to support mathematical set operatons.
it is an unoerdered collection of unique items.'''

#Accessing values in sets
'''set is defined by values seprated by commas insde{}.'''
a={1,3,4,5,69.7}
print(a)

'''creating sets using sets'''
s=set('abc')

'''deleting values in set 1
1)a.discard 2)a.remove 3)a.pop 4)a.clear
'''

'''updating set
1)a.add() 2)a.update()'''

'''basic set operation'''
 #1.union
A={1,3,4,5,6}
B={8,9,10,11}
C=A|B
print(C)
 #2.intersection
A={1,3,4,5,6}
B={3,4,8,9,10,11}
C1=A & B
print(C1)

 #3.Difference
A={1,3,4,5,6}
B={3,4,8,9,10,11}
C2=A - B
print(C2)

 #4.symmetric
A={1,3,4,5,6}
B={3,4,8,9,10,11}
C3=A ^ B
print(C3)









