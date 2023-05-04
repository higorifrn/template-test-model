# NÃO ALTERE O CÓDIO DESSE ARQUIVO

# Tests for Stack Task
# Simple Array Stack

import os.path
import sys
from pilha import Pilha

def test_pilha_vazia_true():

    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha()

    assert pilha.is_empty() == True


def test_pilha_vazia_false():

    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha()
    pilha.push(1)

    assert pilha.is_empty() == False


def test_pilha_push_cheia():

    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha(1)

    pilha.push(1)

    assert pilha.push(2) == False


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


def test_pilha_pop_com_itens():

    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            pilha.push(item[:-1])

    pilha.pop()
    assert pilha.pop().dado == '4'


def test_pilha_pop_sem_itens():
    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha()

    assert pilha.pop() == None


def test_pilha_list_items():
    try:
        exists = os.path.exists("pilha.py")
        assert exists == True
    except:
        sys.exit()

    pilha = Pilha()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            pilha.push(item[:-1])

    output = pilha.list_items()
    
    assert output == [
        "Topo da Pilha:\n",
        "5\n",
        "4\n",
        "3\n",
        "2\n",
        "1\n",
        "Base da Pilha\n",
    ]

