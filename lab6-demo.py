#Harit Palta
def encode(password):
    # string to store encoded password
    encoded_pass = ""

    # encoding  each digit
    for char in password:
        encoded_pass = encoded_pass + str((int(char) + 3) % 10)  # shifting 3 digit up and mod keeps value within 0-9

    # return encoded password
    return encoded_pass

def main():
    run = True
    while run:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!")
            print()
        if option == 2:
            print(f"The encoded password is {encode(password)}, and the original password is {password}.")
            print()
        if option == 3:
            run = False
