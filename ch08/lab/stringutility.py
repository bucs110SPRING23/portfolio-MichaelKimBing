class StringUtility:
    def __init__(self,string):
        self.string = string
    def __str__(self):
        return self.string
    

    def vowels(self):
        count = 0
        vowel_test_string = self.string

        for i in vowel_test_string:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                count += 1
            elif i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
                count += 1
            
        if count >= 5:
            return str("many")
        else:
            return str(count)
        
        
    def bothEnds(self):
        bothends_test_string = self.string

        if len(bothends_test_string) <= 2:
            return ''
        
        bothends_string = bothends_test_string[0] + bothends_test_string[1] + bothends_test_string[-2] + bothends_test_string[-1] 
        return bothends_string
    

    def fixStart(self):
        a = self.string[1:]
        a.replace(self.string[0], "*")
        return self.string[0]+a

    def asciiSum(self):
        asciisum_string = self.string
        ascii_value = 0
        for i in asciisum_string:
            ascii_value += ord(i)
        return ascii_value
    
    def cipher(self):
        cipher_text = self.string
        length_cipher = len(cipher_text)
        encrypted_text = ''
        for i in cipher_text:
            if i.isupper():
                encrypted_text += chr((ord(i) + length_cipher - 84) % 15 + 37)
            else:
                encrypted_text += chr((ord(i) + length_cipher - 95) % 14 + 19)
        return encrypted_text




        
