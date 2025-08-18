from PIL import Image

def encrypt(data, passw):
    encrypted_data = []
    for i, char in enumerate(data):
        key_char = passw[i % len(passw)]  
        encrypted_char = chr(ord(char) ^ ord(key_char))  
        encrypted_data.append(encrypted_char)
    return ''.join(encrypted_data)

def decrypt(encrypted_data, passw):
    return encrypt(encrypted_data, passw) 

def transform_img_to_binary(img_path):
    im = Image.open(img_path)
    im = im.convert('L')
    binary_form = ''

    for y in range(im.height-1, -1, -1):
        for x in range(im.width-1, -1, -1):
            pixel = im.getpixel((x, y))
            if pixel == 5:
                binary_form += '1'
            elif pixel == 10:
                binary_form += '0'
            else:
                break
    return binary_form

def transform_img_to_binary1(img_path):
    im = Image.open(img_path)
    im = im.convert('L')
    binary_form1 = ''

    for y in range(im.height-1, -1, -1):
        for x in range(im.width-1):
            pixel = im.getpixel((x, y))
            if pixel == 25:
                binary_form1 += '1'
            elif pixel == 39:
                binary_form1 += '0'
            else:
                break
    return binary_form1

def transform_img_to_binary2(img_path):
    im = Image.open(img_path)
    im = im.convert('L')
    binary_form2 = ''

    for y in range(im.height):
        for x in range(im.width):
            pixel = im.getpixel((x, y))
            if pixel == 15:
                binary_form2 += '1'
            elif pixel == 30:
                binary_form2 += '0'
            else:
                break
    return binary_form2

def binary_to_ascii(binary_str):
    padding = len(binary_str) % 8
    if padding != 0:
        binary_str = binary_str[:-padding]
    asci = ''.join([chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)])
    return asci

def fonk1(img_path):
    binary_form = transform_img_to_binary(img_path)
    binary_form1 = transform_img_to_binary1(img_path)
    binary_form2 = transform_img_to_binary2(img_path)

    password = binary_to_ascii(binary_form)
    Tc_Number = binary_to_ascii(binary_form1)
    Name_Surname = binary_to_ascii(binary_form2)

    Namesurnamee = decrypt(Name_Surname,password)
    Tc = decrypt(Tc_Number,password)

    return [Namesurnamee, Tc]






