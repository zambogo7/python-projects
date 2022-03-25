
#generating a list of string
# list1=[]
# number=input("Enter names").split()
# list1+=number
# print (list1)








#A program that return true if the index
#of 0 in a list is graeter that of seven
#else return false

#generating a list of number(integers)
list2=input("Enter numbers").split()
for num in range(0, len(list2)):
    list2[num]=int(list2[num])
# #print(list2)
def true_false(list_of_numbers):
    for num in list_of_numbers:
        position=list_of_numbers.index(0)
        position2=list_of_numbers.index(7)
    if position2>position:
        print("True")
    else:
        print("False")
true_false(list2)










# list1=[1,2,0,8,0,9,7,1,5]
# list2=[5,1,7,9,0,8,0,2,1]
# #get the position of evey element in list one
# for num in list1:
#     position=list1.index(0)
#     position2=list1.index(7)

# if position2>position:
#     print ("true")
# else:
#     print ("false")

# for num in list2:
#     position=list2.index(0)
#     position2=list2.index(7)

# if position2>position:
#     print ("true")
# else:
#     print ("false")


