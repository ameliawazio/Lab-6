#Amelia Wazio

# Encoding method
def encode(password):
    print("papuga")
    enc_string = ''
    for num in password: # Has to be string to iterate, change to integer after
        num = int(num)
        password = int(password)
        if num <= 6:
            enc_num = num + 3
            enc_num = str(enc_num)
            enc_string += enc_num
        else:
            enc_num = ((num + 3) % 10) # For numbers going over 9
            enc_num = str(enc_num)
            enc_string += enc_num
    return enc_string
# Decoding method, for partner
def decode(password):
    
    return_password = ''
    for char in password:
        temp_num = int(char)
        temp_num = temp_num + 10 if temp_num <= 3 else temp_num
        return_password += str(temp_num - 3)
    
    return return_password

program = True
# Printing menu and options
if __name__ == '__main__':

    stored_password = ''

    while program == True: # Loop of menu until exit
        print('Menu\n-------------\n 1. Encode\n 2. Decode\n3. Quit ')
        user_input = int(input('Please enter an option: '))

        if user_input == 1:
            password = input('Please enter your password to encode: ')
            stored_password = encode(password)
            print('Your password has been encoded and stored!')
        if user_input == 2:# Decoding, partner work
            # enter decode here
            password = decode(stored_password)
            print(f'The encoded password is {stored_password}, and the original password is {password}')
        if user_input == 3:
            exit()




