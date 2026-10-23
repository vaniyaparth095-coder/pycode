# Open the file in read mode ('r')
with open("story.txt", "r") as file:
    data = file.read()  # Read the entire file content
    print("File Content:")
    print(data)
    
    # Initialize all counters
    ccount = 0  # Counter for alphabets (characters)
    digcnt = 0  # Counter for numeric digits
    spccnt = 0  # Counter for spaces
    symcnt = 0  # Counter for special symbols/characters
    
    # Loop through each character in the text
    for ch in data:
        if ch.isalpha():
            ccount = ccount + 1
        elif ch.isdigit():
            digcnt = digcnt + 1
        elif ch.isspace():
            spccnt = spccnt + 1
        else:
            symcnt = symcnt + 1

    # Print the final counts
    print("Total characters are:", ccount)
    print("Total digits used:", digcnt)
    print("Total spaces are:", spccnt)
    print("Total symbols are:", symcnt)