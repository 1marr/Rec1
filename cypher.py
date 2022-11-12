# Division of PEMaCS
# CSCI-121 Elements of Computer Programming II
# Recitation 1 - Encryption with a password
# *******************************************************

import string

alphabet = string.printable
ordinal_value = {ch: i for i, ch in enumerate(alphabet)}


def encrypt(message, password):
    encrypted_message = ''
    j = 0
    for i in message:
        if j == len(password):
            j = 0
        x = alphabet[(ordinal_value[i] + ordinal_value[password[j]]) % len(alphabet)]
        encrypted_message += x
        j += 1

    return encrypted_message


def decrypt(message, password):
    decrypted_message = ''
    j = 0
    for i in message:
        if j == len(password):
            j = 0
        k = password[j % len(password)]
        x = alphabet[(ordinal_value[i] - ordinal_value[k]) % len(alphabet)]
        j += 1
        decrypted_message += x

    return decrypted_message


print(ordinal_value)
print(encrypt('This is my message', 'My#1Secret Password'))
