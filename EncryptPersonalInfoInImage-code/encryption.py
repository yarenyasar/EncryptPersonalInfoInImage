from PIL import Image
import numpy as np
import random

def randomPassw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password=[]

    nr_letters=2
    nr_symbols=2
    nr_numbers=2

    for letter in range(0,(nr_letters)):
        a=(random.choice(letters))
        password.append(a)
    else:
        pass

    for symbol in range(0,(nr_symbols)):
        b=(random.choice(symbols))
        password.append(b)
    else:
        pass

    for numberr in range(0,(nr_numbers)):
        c=(random.choice(numbers))
        password.append(c)
    else:
        pass

    random.shuffle(password)

    passw=""
    for char in password:
        passw += char
    return passw

def encrypt(data, passw):
    encrypted_data = []
    for i, char in enumerate(data):
        key_char = passw[i % len(passw)]  
        encrypted_char = chr(ord(char) ^ ord(key_char))  
        encrypted_data.append(encrypted_char)
    return ''.join(encrypted_data)

def fonk(image, NameSurname, TcNumber):
    img = Image.open(image)
    image_array = np.array(img)

    encryption_key = randomPassw()

    data_to_hide = encrypt(NameSurname, encryption_key) 
    data_to_hide1 = encrypt(TcNumber, encryption_key) 
    data_to_hide2 = encryption_key

    binary_dataNameSurname = ''.join(format(ord(char), '08b') for char in data_to_hide)  
    binary_data1Tc = ''.join(format(ord(char), '08b') for char in data_to_hide1)
    binary_data2Passw = ''.join(format(ord(char), '08b') for char in data_to_hide2)

    blc_i = 0
    blc_j = 0

    for bit in binary_dataNameSurname:
        if 0 <= blc_i < image_array.shape[0] and 0 <= blc_j < image_array.shape[1]:
            if bit == '1':
                image_array[blc_i, blc_j] = 15
            elif bit == '0':
                image_array[blc_i, blc_j] = 30
            blc_j += 1
        elif blc_i >= 0:
            blc_i -= 1
            blc_j = 0
        else:
            break
    

    blc_i = image_array.shape[0] - 1
    blc_j = 0

    for bit in binary_data1Tc:
        if blc_i >= 0 and blc_j < image_array.shape[1]:
            if bit == '1':
                image_array[blc_i, blc_j] = 25
            elif bit == '0':
                image_array[blc_i, blc_j] = 39
            blc_j += 1
        elif blc_i >= 0:
            blc_i -= 1
            blc_j = 0
        else:
            break


    brc_i = image_array.shape[0] - 1
    brc_j = image_array.shape[1] - 1

    for bit in binary_data2Passw:
        if brc_i >= 0 and brc_j >= 0:
            if bit == '1':
                image_array[brc_i, brc_j] = 5
            elif bit == '0':
                image_array[brc_i, brc_j] = 10
            brc_j -= 1
        elif brc_i >= 0:
            brc_i -= 1
            brc_j = image_array.shape[1] - 1
        else:
            break
    
    encoded_image = Image.fromarray(image_array)
    return encoded_image
