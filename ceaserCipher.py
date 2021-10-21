from collections import defaultdict

def freqAtt(A):
    # calculating the length of string & converting the string to uppercase to avoid any snag in frequency attack
    N, A = (len(A), A.upper())

    # List to store the top blank texts
    blanktxt = []              

    # storing the english letters in their decreasing order of frequency
    eng_ltr_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    # dictionary to store frequency of the letters in cipher text  
    freq = defaultdict(int)    

    # calculating the frequency of the letters in cipher text
    for k in A: freq[c] += 1
    
    # Sorting frequency and storing it in a tuple
    sorted_freq = tuple(sorted(frequency.items(), key = lambda i: i[1], reverse=True))


    for i in range(26):
        # calculating the key
        key = (26 + ord(sorted_freq[0][0]) - ord(eng_ltr_freq[i])) % 26
        txt = ""

        # time complexity : O(26 * N)
        for j in range(len(S)):
            # traversing on string and decoding it
            if(S[j] >= 'A' and S[j] <= 'Z'):
                txt += chr(65 + (ord(S[j]) - 65 + key) % 26)
            else: 
                txt += S[j]

        blanktxt.append(txt)

    return blanktxt

# S = input("Enter encoded string: ")
pt = int(input("please enter how many plane txt you what (max limit is : 26): "))

S = "nsdvhjfbsdv gfbusdhjgb visgjuhb jhvb shgerbdfs cigsbiug aiwkliouegiolgf ipggblk igfbi bfikljghb riful gbfikjhb filkgerb kij gbi wekabvstfvser vbkgjkl"

# calling the function to get blanktexts
blanktxt = freqAtt(A)

print("\n\nPLAIN TEXTS DECODED :\n")
# printing the blankntexts
for i in range(pt % 26):
    print( i + 1, end = ": ")
    print( blanktxt[i], end = "\n\n")