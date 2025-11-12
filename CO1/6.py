filename=input("Enter the file name:")
i=len(filename)-1
while i>=0 and filename[i]!='.':
    i-=1
if i==-1:
    print("The file has no extension.")
else:
    print("The extension of the file is:",filename[i+1:])
    
