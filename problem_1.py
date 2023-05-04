# YOUR NAME
# CTEC 121
# Problem Set 3 - Problem 1
# Simple Pay Program

"""
Inputs, Processes and Outputs (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Input(s):
Processes:
Output(s)
"""

from pilha import Pilha

def main():
    pilha = Pilha()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            pilha.push(item[:-1])

    pilha.list_items()
    
if __name__ == "__main__":
    main()