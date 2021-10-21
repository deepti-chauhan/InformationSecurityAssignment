#----------------------------------------FREQUENCY ATTACT----------------------------#

def frequency_attack(str, length):
  ''' function to print the top ten possible plain texts 
      that can be decrypted from the given monoalphabetic 
      cipher using a letter frequency attack '''
  plain_text = ['']*10
  char_frequency = [0]*26 #frequency of letters
  freq = ['']*26
  used_alphabet = [0]*26

  #find frequency of each character of string and store in a variable char_frequency[]
  for i in range(len(str)):
    if str[i] != ' ':
      char_frequency[ord(str[i]) - 65] += 1
  
  #copy the frequency of array
  for i in range(26):
    freq[i] = char_frequency[i]


  sample_str = "ETAOINSHRDLCUMWFGYPBVKJXQZ" # intialize a string

  freq.sort(reverse = True)# store the array in descending order


  #iterate over range[0,10]
  for i in range(10):
    word = -1

    # Iterate over the range [0, 26]
    for j in range(26):
      if freq[i] == char_frequency[j] and used_alphabet[j] == 0:
        used_alphabet[j] = 1
        word = j
        break
  
    if word == -1:
      break
# Store the numerical equivalent of letter
# at ith index of array letter_frequency     
    x = ord(sample_str[i]) - 65
    x = x-word

    current = "" #temporary string

    # Generate the probable ith plaintext
    # string using the shift calculated above
    for k in range(len(str)):
      if str[k] == ' ': #for whitespaces
        current += " "
        continue

      y = ord(str[k]) - 65 #shift kth letter of cipher by x
      y += x
      if y < 0:
        y += 26
      if y > 25:
        y -= 26
         
      current += chr(y + 65)# add kth shifted letter to temporary string
      
    plain_text[i] = current

    # Print the generated 10 possible plaintexts    
  for i in range(10):
        print(plain_text[i])
 


Str = "B TJNQMF NFTTBHF"
length = len(Str)
frequency_attack(Str, length)
