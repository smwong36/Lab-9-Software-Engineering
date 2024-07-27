def encode(password):
# Takes a string of numbers, and returns a string of the numbers after adding 3.
    new_string =""
    for i in range(len(password)):
        x = int(password[i]) +3
        new_string += str(x)
    return new_string