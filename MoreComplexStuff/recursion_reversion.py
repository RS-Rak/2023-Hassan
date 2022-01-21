string = str(input("Please enter a string."))

def reverse_string(string):
    if len(string) == 1: 
        return string
    else: 
        return reverse_string(string[1:]) + string[0]
    
print(reverse_string(string))