numbers=input("Enter integers seperated by spaces:")
numbers_list=numbers.split()
result=[]
for num in numbers_list:
    num=int(num)
    if num>100:
        result.append('over')
    else:
        result.append(num)
print("Modified list:",result)        
