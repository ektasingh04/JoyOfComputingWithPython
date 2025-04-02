sentence = input("Enter a sentence: ")
tokens = []
current_token = ""


for char in sentence:
    if char.isspace():
        if current_token:
            tokens.append(current_token)
            current_token = ""
    else:
        current_token += char




if current_token:
    tokens.append(current_token)


print("Tokens:", tokens)