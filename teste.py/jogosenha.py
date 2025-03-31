import random

senha = random.sample(range(0, 10), 4)
senha_str = ''.join(map(str, senha)) 

while True:
    palpite = input("Digite 4 números: ")

    for i, num in enumerate(palpite):
        if int(num) == senha[i]:
            print(num, end="")
        elif int(num) in senha:
            print("?", end="")
        else:
            print("x", end="")
    print()

    if palpite == senha_str: 
        print("Acertou!", palpite)
        break