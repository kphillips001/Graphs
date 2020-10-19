# Lets implement two functions called Encrypt and Decrypt
# these functions will take a string and return another string


# Encrypt will take a normal english string and jumble it using Caesar Cipher
# (substitution Cipher)

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S',
    ' ': ' '
}

decode_table = {}

def build_decode_table(encode_table):
    for key,value in encode_table.items():
        decode_table[value] = key
    
build_decode_table(encode_table)



def encrypt(string):
    # create a new string
    encrypted_str = ""
    # loop through the string
    for char in string:
        encrypted_str += encode_table[char]
    
    return encrypted_str

def decrypt(string):
    # create a new string
    encrypted_str = ""
    # loop through the string
    for char in string:
        encrypted_str += decode_table[char]
    
    return encrypted_str

encrypted_message = encrypt("HELLO WORLD")
print(encrypted_message)

print(decrypt(encrypted_message))