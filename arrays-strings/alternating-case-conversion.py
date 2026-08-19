def convert_alternating_case(s):
    new_string = list(s)
    
    for i in range(len(new_string)):
        if new_string[i].islower():
            new_string[i] = new_string[i].upper()
        else:
            new_string[i] = new_string[i].lower()
    return "".join(new_string)
        
