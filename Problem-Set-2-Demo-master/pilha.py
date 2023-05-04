# -*- coding:UTF-8 -*-
from no import No

class Pilha:
  def __init__(self, capacidade=5):
    self.__topo = None
    self.__capacidade = capacidade
    self.__qtdItens = 0


  def is_empty(self) -> bool:
    # implementação do método
    return True if not self.__topo else False
  

  def push(self, valor) -> bool:
    # implementação do método
    novo = No(valor)
    msg = f"Item ({novo}) inserido na Pilha!"
    resultado = True

    if self.is_empty():
      self.__topo = novo
      self.__qtdItens += 1
    else:
      if self.__capacidade > self.get_size():
        novo.prox = self.__topo
        self.__topo = novo
        self.__qtdItens += 1
      else:
        msg = f"Pilha Cheia! Item ({novo}) Não inserido na Pilha!"
        resultado = False

    print(msg)

    return resultado


  def pop(self):
    # implementação do método
    pass

  def peek(self):
    # implementação do método
    pass

  def list_items(self):
    # implementação do método
    pass

  def get_size(self): 
    # implementação do método
    return self.__qtdItens

# from No import No

# class Pilha:
#   def __init__(self):
#       self.topo = None

#   def is_empty(self):
#     # implementação do método
#     if not self.topo:
#       return True
#     else:
#       return False
  
#   def push(self, item):
    # novo = No(item)
    # if self.is_empty():
    #   self.topo = novo
    # else:
    #   novo.prox = self.topo
    #   self.topo = novo

#   def pop(self):
#     if self.is_empty():
#       print('Pilha vazia')
#       return None
#     else:
#       item = self.topo
#       self.topo = item.prox
#       # print('Novo topo: ', self.topo.dado)
#       del item
#       return self.topo.dado

#   def peek(self):
#     return self.topo.dado

#   def list_items(self):
#     item = self.topo
#     print('Topo da Pilha')
#     while item:
#       print(item.dado, end=' ')
#       item = item.prox
#     print('Fim da pilha')
