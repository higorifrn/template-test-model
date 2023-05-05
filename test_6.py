# NÃO ALTERE O CÓDIO DESSE ARQUIVO

# Tests for Stack Task
# Simple Array Stack

import os.path
import sys
from pilha import Pilha


def test_pilha_get_size_com_itens():

    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha(5)

    with open('entrada_dados.txt') as reader:
        for item in reader:
            pilha.push(item[:-1])

    assert pilha.get_size() == 5


def test_pilha_get_size_sem_itens():

    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha(5)

    assert pilha.get_size() == 0
