import string

def encrypt(message,key):
    
        shift = key%26
        cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

        encrypted = message.lower().translate(cipher)
        return encrypted
    
def decrypt(encrypted,key):
        shift = 26-(key%26)
        cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift] )
        
        message = encrypted.translate(cipher)
        return message

message = 'hello world'
key = 3

encrypted = encrypt(message,key)
print(f"Encrypted message:{encrypted}")

decrypted = decrypt(encrypted , key)
print(f"Decrypted message:{decrypted}")
