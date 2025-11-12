a=[1,-2,6,3,-5,7,0]
positive_num=[]
for num in a:
    if num>0:
        positive_num.append(num)
        
print("Positive numbers:",positive_num)

 
print("numbers on the list:",a)
square=int(input("Enter a number from the list to square:"))
if square in a:
           b=square**2
           print("square of",square,"is",b)
else:
    print("The number is not in the list.")            
