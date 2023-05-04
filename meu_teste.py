from pilha import Pilha

pilha = Pilha(5)
    
with open('entrada_dados.txt') as reader:
    for item in reader:
        pilha.push(item)

print(pilha.push(6))