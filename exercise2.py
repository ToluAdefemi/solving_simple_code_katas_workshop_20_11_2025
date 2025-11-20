# Build a program that calculates the number of characters in a string
# eg. count_characters("its a fantastic day", "a") #=> 4

# Parameters
#    - text, a string (eg. "life is amazing")
#    - character, a string (eg. "e")
# Returns
#    - integer (eg. 4)
# Side effects
#    - None
def count_characters(text, character):
    count = 0 # task 1 

    for char in text: #task 2
        if char == character: 
            count +=1 # task 3
    return count # task 4


print(count_characters("Its a fantastic day", "a"))
print(count_characters("Checking if answer works well", "w"))

# Tasks 
# Create a variable to track number of characters 
# Find the characters in the string (Likely through looping through)
# Update the tracker each time the variable appears 
# return the final result of the tracker 

