# --- STEP 1: Create the file with some initial names ---
with open("a.txt", "w") as f1:
    for i in range(1, 4):
        nm = input(f"Enter name {i}: ")
        f1.write(nm + "\n")

# --- STEP 2: Ask user for the word to search for ---
sew = input("Enter the word to search for: ")
flag = False

# Read the file contents to perform a search and match
with open("a.txt", "r") as f2:
    for line in f2:
        # Strip the trailing newline '\n' to accurately match the word
        if line.strip() == sew:
            print("Match found!!")
            flag = True

# --- STEP 3: Replace the word if it exists ---
if not flag:
    print(sew, "was not found in the file.")
else:
    # Ask for the replacement word
    r_word = input("Enter the word to replace it with: ")
    
    # Read the full file content
    with open("a.txt", "r") as f2:
        data = f2.read()
    
    # Replace the old word with the new word safely
    # Using word boundaries or matching lines precisely prevents accidental partial overrides
    lines = data.splitlines()
    updated_lines = [r_word if line == sew else line for line in lines]
    data = "\n".join(updated_lines) + "\n"
    
    # Write the updated text back to the file
    with open("a.txt", "w") as f2:
        f2.write(data)
        
    print(f"'{sew}' has been replaced with '{r_word}'.")

# --- STEP 4: Display the final modified file content ---
print("\n--- Displaying Updated File ---")
with open("a.txt", "r") as f1:
    print(f1.read())