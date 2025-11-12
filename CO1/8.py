colors=input("Enter comma-seperated volor names:")
color_list=[]
color=""
for ch in colors:
    if ch==',':
        color_list.append(color)
        color=""
    else:
        color +=ch
color_list.append(color)
print("First color:",color_list[0])
print("Last color:",color_list[-1])
