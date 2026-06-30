def encode(message,shift):
    encoded_message=""
    ascii_values = [ord(ch) for ch in message ]
    shift = shift%26
    for val in ascii_values:
        if 122>=val>=97:
            encoded_message+= chr((val+shift-97)%26+97)
        else :
            encoded_message+=chr(val)
    return encoded_message

def decode(message,shift):
    decoded_message=""
    ascii_values = [ord(ch) for ch in message ]
    shift = shift%26
    for val in ascii_values:
        if 122>=val>=97:
            decoded_message+= chr((val-shift-97)%26+97)
        else :
            decoded_message+=chr(val)
    return decoded_message

while True:
    type = input("Type 'encode' to encode the message and 'decode' for decoding the message : ")
    message = input("Enter your message : ").lower()
    shift = int(input("ENter shift number : "))
    if(type=='encode'):
        message = encode(message,shift)
    elif type=='decode':
        message = encode(message,-shift)
    else :
        print("Invalid input!")
    print("Your Encoded message : "+message)
    if input("do you wanna go again? Yes").lower() != 'yes':
        break

