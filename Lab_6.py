#Amelia Wazio

# Encoding method
def encode(password):
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
    
    char_string = ''
    for char in password:
        char = int(char)
        password = int(password)
        if char >= 3:
            dec_char = (char - 3)
            dec_char = str(dec_char)
            char_string += dec_char
        else:
            dec_char = ((char + 10)-3)
            dec_char = str(dec_char)
            char_string += dec_char
    
    return char_string

program = True
# Printing menu and options
if __name__ == '__main__':

    

    while program == True: # Loop of menu until exit
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit ')
        user_input = int(input('Please enter an option: '))
        
        if user_input == 1:
            password = input('Please enter your password to encode: ')
            encode(password)
            stored_password = encode(password)
            print('Your password has been encoded and stored!')
        if user_input == 2:# Decoding, partner work
            # enter decode here
            decode(password)
            char_string = decode(stored_password)
            print(f'The encoded password is {stored_password}, and the original password is {char_string}')
        if user_input == 3:
            exit()




