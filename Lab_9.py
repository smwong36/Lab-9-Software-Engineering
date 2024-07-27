
def encode(password):
# This function is written by Samantha Wong
    new_string =""
    for i in range(len(password)):
        x = int(password[i]) +3
        new_string += str(x)
    return new_string

# decode by rohan david

def decode(password):
    decoded_str = []
    for i in password:
        digit = chr(ord(i) - 3)
        decoded_str.append(digit)
    return ''.join(decoded_str)

def main(): # This function is written by Samantha Wong
    
    encrypt = True
    while encrypt:
    # print menu
        print("Menu")
        print('-------------')
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
    # input option
        option = input("Please enter an option: ")
    # encode
        if int(option) == 1:
            password = input('Please enter the password to encode: ')
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!")
            print()
    # decode
        elif int(option) == 2:
            decoded_pass = decode(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}.")
            print()
    # quit
        elif int(option) == 3:
            encrypt = False
            
            
if __name__ == "__main__":
    main()
