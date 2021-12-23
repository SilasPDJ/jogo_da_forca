message = 'Banana'
count = {}

for character in message:
    """
    Ele vai settando no dicionário quando muda de caractere
    dentro do loop
    
    O count[character] recebe ele mesmo (o dicionário de uma letra recebe ela mesma) 
    + o 1, que incrementao 0 quando é achado o valor
    
    """
    count.setdefault(character, 0)
    # print(count.keys())
    count[character] = count[character] + 1

print(count)