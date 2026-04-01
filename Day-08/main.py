
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
ask=True
while ask==True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

  
    def encrypt(original_text, shift_amount):
        cipher_text = ""
        for letter in original_text:
            if letter in alphabet:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            else:
                cipher_text+=letter
        print(f"Here is the encoded result: {cipher_text}")

    def decrypt(original_text, shift_amount):
        newtext=""
        for x in original_text:
            if x in alphabet:
                value=alphabet.index(x) - shift_amount
                newtext=newtext+alphabet[value]
            else:
                newtext=newtext+x

        print(f"Here is the decrypted message: {newtext}")


    def cesar(my_direction):
        if direction == 'encode':
            encrypt(original_text=text, shift_amount=shift)
        elif direction == 'decode':
            decrypt(original_text=text, shift_amount=shift)
        else:
            print("please check your entry")


    cesar(my_direction=direction)

    redo=input("WOULD YOU LIKE TO CONTINUE ENCRYPTING OR DECRYPTING : type 'yes' or 'no':\n").lower()
    if redo=="no":
        ask=False
    else:
        ask=True
        print("THANK YOU FOR USING CIPHER")












