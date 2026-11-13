alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
logo = """
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           
"""

def caesar(string, shift = 3, decrypt = False):
    word = ""
    for i in string:
        i2 = i.lower()
        if i2 not in alphabet:
            word += i2
            continue
        letter_idx = alphabet.index(i2)
        if decrypt == True:
            word += alphabet[(letter_idx - shift) % len(alphabet)]
        else:
            word += alphabet[(letter_idx + shift) % len(alphabet)]
    return word
def main():
    print(logo)
    while True:
        direction = input("Type \'encode\' to encrypt, type \'decode\' to decrypt:\n")
        if direction.lower() == "decode":
            print(f"Here's the decoded result: {caesar(input("Type your message:\n"), int(input("Type the shift number:\n")), True)}")
        else:
            print(f"Here's the encoded result: {caesar(input("Type your message:\n"), int(input("Type the shift number:\n")))}")
        if input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower() == "yes":
            continue
        else:
            break
    print("Goodbye.")


if __name__ == '__main__':
    main()