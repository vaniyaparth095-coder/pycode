# Open the file in read mode ('r')
with open("a.txt", "r") as file:
    data = file.read()  # Read the entire file content
    print("File Content:")
    print(data)
    
    ucount = 0  # Counter for uppercase letters
    lcount = 0  # Counter for lowercase letters
    
    # Loop through each character in the text
    for ch in data:
        if ch.isupper():
            ucount = ucount + 1
        elif ch.islower():
            lcount = lcount + 1
            
    print("Total uppercase letters:", ucount)
    print("Total lowercase letters:", lcount)