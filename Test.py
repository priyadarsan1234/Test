# Function to reverse a string
def reverse_string(input_str):
    # Using string slicing to reverse the string
    reversed_str = input_str[::-1]
    return reversed_str

# Input from the user
user_input = 'priyadarsan'

# Call the reverse_string function and print the reversed string
reversed_input = reverse_string(user_input)
print("Reversed string:", reversed_input)
