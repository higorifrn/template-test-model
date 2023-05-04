# NÃO ALTERE O CÓDIO DESSE ARQUIVO

# Tests for Stack Task
# Simple Array Stack

import os.path
import sys
from pilha import Pilha


def test_pilha_peek():

    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha(5)

    with open('entrada_dados.txt') as reader:
        for item in reader:
            pilha.push(item[:-1])

    assert pilha.peek().dado == '5'
