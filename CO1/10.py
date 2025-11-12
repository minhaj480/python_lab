list_1=["Red","Green","Blue","Yellow","White"]
list_2=["Green","Yellow","Black"]
unique_colors=[]
for color in list_1:
    if color not in list_2:
        unique_colors.append(color)
        print("Colors from list 1 not in list2:",unique_colors)
        
