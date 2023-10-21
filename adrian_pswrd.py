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
        elif menu_option == 2:
            pass
        elif menu_option == 3:
            break
