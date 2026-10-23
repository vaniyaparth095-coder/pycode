# Open the file in read mode ('r')
with open("a.txt", "r") as file:
    data = file.read()  # Read the entire file content
    print("File Contents:")
    print(data)
    
    count = 0
    # Loop through each character in the file content
    for ch in data:
        # Check if the character is a vowel (both lowercase and uppercase)
        if ch in "aeiouAEIOU":
            count = count + 1
            
    print("No. of vowels:", count)