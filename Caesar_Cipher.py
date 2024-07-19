def encode(text, steps):
    encoded_text = ''
    for i in text:
        encoded_text += chr(((ord(i)-65) + steps % 26) + 65) if text.isupper() else chr(((ord(i)-97) + steps % 26) + 97)
    return encoded_text

def decode(text, steps):
    encoded_text = ''
    for i in text:
        encoded_text += chr(((ord(i)-65) - steps % 26) + 65) if text.isupper() else chr(((ord(i)-97) - steps % 26) + 97)
    return encoded_text

def main():
    print("""
.-----------------------------------------------------------------.
| ▄▄·  ▄▄▄· ▄▄▄ ..▄▄ ·  ▄▄▄· ▄▄▄       ▄▄· ▪   ▄▄▄· ▄ .▄▄▄▄ .▄▄▄  |
|▐█ ▌▪▐█ ▀█ ▀▄.▀·▐█ ▀. ▐█ ▀█ ▀▄ █·    ▐█ ▌▪██ ▐█ ▄███▪▐█▀▄.▀·▀▄ █·|
|██ ▄▄▄█▀▀█ ▐▀▀▪▄▄▀▀▀█▄▄█▀▀█ ▐▀▀▄     ██ ▄▄▐█· ██▀·██▀▐█▐▀▀▪▄▐▀▀▄ |
|▐███▌▐█ ▪▐▌▐█▄▄▌▐█▄▪▐█▐█ ▪▐▌▐█•█▌    ▐███▌▐█▌▐█▪·•██▌▐▀▐█▄▄▌▐█•█▌|
|·▀▀▀  ▀  ▀  ▀▀▀  ▀▀▀▀  ▀  ▀ .▀  ▀    ·▀▀▀ ▀▀▀.▀   ▀▀▀ · ▀▀▀ .▀  ▀|
'-----------------------------------------------------------------'
""")
    while True:
        try:
            option = input("\n\nSelect 'encode / -e' or 'decode / -d' or 'quit' to exit: ")
            if option.lower() == "encode" or option.lower() == "-e":
                plain_text = input("Enter the plain text to be encoded or decoded : ")
                shift_steps = int(input("The number of Steps to be shifted: "))
                print(f"The Encode Text is {encode(plain_text, shift_steps)}")
            elif option.lower() == "decode" or option.lower() == "-d":
                plain_text = input("Enter the plain text to be encoded or decoded : ")
                shift_steps = int(input("The number of Steps that was used to be shifted: "))
                print(f"The Decoded Text is {decode(plain_text, shift_steps)}")
            elif option.lower() == "quit" or option.lower()=='exit':
                print("\nExiting..")
                exit()
            else:
                print("Kindly provide right input to encode or decode the text!!")
        except ValueError:
            print('You are expected to give a number!!')



if __name__ == "__main__":
    main()