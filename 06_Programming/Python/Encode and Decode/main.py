# TODO-1: Import and print the logo from art.py when the program starts.
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    encode_or_decode = encode_or_decode.lower()

    if encode_or_decode == "en":
        shift_amount *= +1
        for letter in original_text:

            if letter in alphabet:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
            else:
                output_text += letter
        print(f"Here is the encoded result: {output_text}")

    elif encode_or_decode == "de":
        shift_amount *= -1

        for letter in original_text:

            if letter in alphabet:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
            else:
                output_text += letter
        print(f"Here is the decoded result: {output_text}")

    else:
        print("Wrong Input")
# TODO-3: Can you figure out a way to restart the cipher program?

repeat="y"
while repeat == "y":
    print("Welcome to the Caesar Cipher. Please follow the Instruction to ENCODE or DECODE your message:\n")
    caesar(original_text=input("type your message:\n").lower(),
           shift_amount=int(input("type the shift amount:\n")),
           encode_or_decode=input("what do you want 'en' for encode and 'de' for decode:\n")
           )

    re = input("Do you want to repeat this code? (y/n): ")
    if re == "y":
        repeat="y"
    else:
        repeat="n"
print("thank you for using this code")



