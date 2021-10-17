#---------------------------------ADDITIVE CIPHER(Ceasar Cipher)---------------------------------#
''' The Caesar Cipher technique is one of the earliest and simplest method of encryption technique.
    It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter
    some fixed number of positions down the alphabet. '''
def additive_encrypt(txt,m):
    word = txt # String of lower case letters, called Text.
    c = '' # initialize an empty string 
    # Traverse the given text one character at a time
    for i in word:

      # for space between the words
        if (i == ' '):
            c += ' '
      # For each character, transform the given character as per the rule, 
      # depending on whether we’re encrypting or decrypting the text.
        else:
            c += (chr(ord(i) + m))
    return c

def additive_decrypt(txt,m):
    word = txt # String of encrypted words.
    c = '' #empty string

    # traverse the given encrypted string.
    for i in word:
        if (i == ' '): # to maintain space
            c += ' '
      # For each character, transform the given character as per the rule, 
      # depending on whether we’re encrypting or decrypting the text.
        else:
            c += (chr(ord(i) - m))
    return c
def main():
    while True:
        print(f'\n{"-" * 15}\n     Menu\n{"-" * 15}')
        print(*["1. Encryption", "2. Decryption", "3. exit"], sep="\n")
        # user input
        choice = input("\nEnter your choice : ").strip()

        # menu driven choice.
        if choice not in ("1", "2", "3"):
            print("-"*10,"Invalid choice","-"*10)
        elif choice == "1":
            user_input = input("\nenter some Text to be encrypted: ")
            key = int(input("enter Shift or Key : ").strip())

            print("\nEncrypted Text is : " + additive_encrypt(user_input, key))
        elif choice == "2":
            user_input = input("enter some Text to be decrypted: ")
            key = int(input("enter Shift or Key : ").strip())

            print("\nDecrypted Text is : " + additive_decrypt(user_input, key))
        elif choice == "3" : 
          break
if __name__ == "__main__":
  main()