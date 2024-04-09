# ----------------------------------------------------------------------------------------------------------------- FILE WORD COUNT PROGRAM

# import module 
import os
import shutil

# Accept file name from user
file_name = input("Enter the file name: ")

# Check if file exists
if os.path.isfile(file_name):
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Initialize word count
        total_words = 0
        
        # Read lines from the file
        lines = file.readlines()
        
        # Iterate over each line
        for line in lines:
            # Split the line into words
            words = line.split()
            
            # Update word count
            total_words += len(words)
    
    # Open another file in write mode to store word count
    with open("word_count.txt", 'w') as output_file:
        # Write total word count to the file
        output_file.write(str(total_words))
    
    print("Word count saved to 'word_count.txt'")
else:
    print("File not found.")  

