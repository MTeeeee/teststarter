#### Decoder

# encode = True

#############################

print('''Decoder online''')

#encode = input("(E)ncode or (D)ecode? ")
user_input = input("Please enter your code: ")
key = int(input("Please enter key: "))


array_input = list(user_input)

print(array_input)

output = []

for i in array_input: 
    transform = ord(i)

    if transform >= 65 and transform <=90:
        transform += key
        if transform > 90:
            transform -= 26
        elif transform < 65:
            transform += 26
        output.append(chr(transform))
    
    elif transform >= 97 and transform <= 122:
        transform += key
        if transform > 122:
            transform -= 26
        elif transform < 97:
            transform += 26
        output.append(chr(transform))

    else:
        output.append(chr(transform))

output_string = ''.join(str(e) for e in output)


print(output_string)

