# The program below is supposed to perform a Caesar shift on a whole string of lowercase letters.
# Included with the code is an encoded message (spaces removed, shifted by 17). 

alphabet = "abcdefghijklmnopqrstuvwxyz"
code_string = "kfgjvtivkzewfidrkzfe"

translated_string = ""
for i in range(len(code_string)):
    index = (alphabet.find(code_string[i]) + 9) % 26
    translated_string = translated_string+alphabet[index]
print(translated_string)