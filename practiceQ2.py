#pallindrome or not

list1=[1,2,1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("pallindrome")
else:
    print("NOT pallindrome")

copy_list2=list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("pallindrome")
else:
    print("NOT pallindrome")
