Choice = input("Please Select Your Action | Create ='C' | Bypass ='B': ").upper()

def Ceaser(Text):
    cipher_Text = ""
    for word in Text:
        if word.isalpha():
            cipher_word = chr(ord(word) + 1)
            if word == 'z':  # Küçük harf 'z' olursa 'a' yap
                cipher_word = 'a'
            elif word == 'Z':  # Büyük harf 'Z' olursa 'A' yap
                cipher_word = 'A'
            cipher_Text += cipher_word
        else:
            cipher_Text += word  # Harf değilse olduğu gibi ekle
    return cipher_Text

def Bypass(Text):
    decipher_Text = ""
    for word in Text:
        if word.isalpha():
            decipher_word = chr(ord(word) - 1)
            decipher_Text += decipher_word
        else:
            decipher_Text += word
    return decipher_Text

# Kullanıcıdan metni al
Text = input("Enter the text: ")

# Kullanıcının seçimine göre şifreleme veya çözme işlemi yap
if Choice == 'C':
    cipher = Ceaser(Text)
    print("Cipher Text:", cipher)
elif Choice == 'B':
    original = Bypass(Text)
    print("Decrypted Text:", original)
else:
    print("Invalid choice. Please enter 'C' or 'B'.")
