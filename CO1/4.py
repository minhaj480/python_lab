n=int(input("Enter the number of names:"))
names=[]
for i in range(n):
    name=input("Enter name:")
    names.append(name)
count_a=0
for name in names:
    for ch in name:
        if ch=='a' or ch=='A':
            count_a +=1
print("The letter 'a' appears",count_a,"times in the list of names.")            
