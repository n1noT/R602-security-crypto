import random

# Exercice 1 : Chiffrement de César
# 1.

# minsucule 97-122
# majuscule 65-90

def cesar(message, shift):
    result = ""
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def decrypt_cesar(crypted, shift):
    result = ""
    for i in range(len(crypted)):
        char = crypted[i]
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return result

shift = 5
message_crypted = cesar("Hola", shift)
messa_decrypted = decrypt_cesar(message_crypted, shift)

# print(message_crypted)
# print(messa_decrypted)

# 2. (a)

def char_shift_min(c, n):
    result = ""
    if 0 > n or n > 26:
        return print("n must be between 0 and 26 include")
    else:
        if c.islower():
            result = chr((ord(c) + n - 97) % 26 + 97)
        else:
            result = c
    return result

char = char_shift_min("N" , 2)

# print(char) 

# 2. (b)

def KGen():
    return random.randint(0, 26)

def Enc(message, shift):
    result = ""
    for i in range(len(message)):
        char = message[i]
        result += char_shift_min(char, shift)
    return result

def char_unshift_min(c, n):
    result = ""
    if 0 > n or n > 26:
        return print("n must be between 0 and 26 include")
    else:
        if c.islower():
            result = chr((ord(c) - n - 97) % 26 + 97)
        else:
            result = c
    return result

def Dec(crypted, shift):
    result = ""
    for i in range(len(crypted)):
        char = crypted[i]
        result += char_unshift_min(char, shift)
    return result

m = "Message Officiel" 
sk = KGen()
c = Enc(m, sk)
d = Dec(c, sk)

# print(c)
# print(d)

# 2. (c)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

file_path = 'exo-cesar/cesar.txt'
message = read_file(file_path)

sk = 9
dec = Dec(message, sk)

print(dec)