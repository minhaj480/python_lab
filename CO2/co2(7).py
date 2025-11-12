text=input("Enter a string:")
if len(text)>=3:
    if text.endswith('ing'):
        text=text+'ly'
    else:
         text=text+'ing'
else:
    text=text
print("Modified string:",text)    
