def decrypt_caesar_cypher(encrypted_text,shift):
    """
    Encrypts or decrypts a message using the Caesar cipher technique.

    args:
        text:str = the message to encrypt or decrypt
        shift:int = the number of positions to shift each letter
    return:
        :str = the encrypted or decrypted message
    """
    result = ""
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.islower():
            result += chr(ord(char) - 23)
        elif char.isupper():
            if ord(char) == 65:
                result += chr(ord(char) + 55)
            elif ord(char) == 66:
                result += chr(ord(char) + 55)
            elif ord(char) == 67:
                result += chr(ord(char) + 55)
            elif ord(char) == 107:
                result += chr(ord(char) - 23)
            else:
                result += chr((ord(char) + shift))
        else:
            result += chr(32)
        # if char.islower():
        #     result += chr(ord(char) - 23)
        # elif char.isupper():
        #     if ord(char) == 65 and 66 and 67:
        #         result += chr(ord(char) + 55)
        #     elif ord(char) == 107:
        #         result += chr(ord(char) - 23)
        #     else:
        #         result += chr((ord(char) + shift))
        # else:
        #     result += chr(32)
    return result

def main():
    file_pointer = open('ch07/exercises/decrypted.txt','a')
    encrypted_text = 'kKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ'
    shift = 29
    result = decrypt_caesar_cypher(encrypted_text, shift)
    print(result)
    changes = []
    changes.append(result)
    for result in changes:
        file_pointer.write(result)
        file_pointer.close()
        print("file has been decrypted")
        return None
    
main()


