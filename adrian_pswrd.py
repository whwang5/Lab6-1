#Adrian Garcia

def encode(pswrd):
    encode_key = {
        10: 0,
        11: 1,
        12: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9
    }

    global encoded_str_pswrd
    for i in range(8):
        encoded_pswrd.append(encode_key[(int(pswrd[i]) + 3)])
        encoded_digit = str(encoded_pswrd[i])
        encoded_str_pswrd = encoded_str_pswrd + encoded_digit
    return encoded_str_pswrd

encoded_pswrd = []
encoded_str_pswrd = ''

#William Wang
def decode_password(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password


if __name__ == '__main__':
    while True:
        print("Menu")
        print('------------')
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        menu_option = int(input("Please enter an option: "))
        if menu_option == 1:
            pswrd = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            print()
            new_encoded_pswrd = encode(pswrd)
    elif choice == "2": #William Wang
        if 'encoded_password' in locals():
            decoded_password = decode_password(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        else:
            print("No encoded password available. Please encode a password first.")
        elif menu_option == 3:
            break
