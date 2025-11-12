list1=input("Enter integers for list 1 seperated by spaces:").split()
list1=[int(x)for x in list1]

list2=input("Enter integers for list 2 seperated by spaces:").split()
list2=[int(x)for x in list2]

if len(list1)==len(list2):
    print("Both list have same length.")
else:
    print("List have different lengths.")


if sum(list1)==len(list2):
    print("Both list have same sum.")
else:
    print("List have different sums.")

common_values=[]
for item in list1:
    if item in list2 and item not in common_values:
        common_values.append(item)



if common_values:
    print("Common values in both lists:",common_values)
else:
    print("No common values in the lists.")
    

