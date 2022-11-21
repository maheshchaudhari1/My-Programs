def find_duplicates(list_of_numbers):
    list1=[]
    for i in list_of_numbers:
        index =list_of_numbers.index(i)
        for x in range(index+1,len(list_of_numbers)):
             if i==list_of_numbers[x]:
                 list1.append(i)
    z= list(set(list1))
    return z
    #start writing your code here

list_of_numbers=[5,4,5,8,7,2,8,5,3,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)