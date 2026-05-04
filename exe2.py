import json
import random

try:
    arquivo = open("score.json", "r")
    recorde = json.load(arquivo)
    arquivo.close()
except:
    recorde = 999

numero_sorteado = random.randint(1, 100)
minhas_tentativas = 0

print("Tente adivinhar o número!")

while True:
    try:
        chute = int(input("Qual seu palpite? "))
    except:
        print("Digite apenas números, por favor!")
        continue # Volta para o início do laço
    
    minhas_tentativas = minhas_tentativas + 1

    if chute < numero_sorteado:
        print("É maior!")
    elif chute > numero_sorteado:
        print("É menor!")
    else:
        print("Você acertou!")
        print("Tentativas desta vez:", minhas_tentativas)

        if minhas_tentativas < recorde:
            print("NOVO RECORDE!")
            # Salva o novo recorde no arquivo
            arquivo = open("score.json", "w")
            json.dump(minhas_tentativas, arquivo)
            arquivo.close()
            
        break