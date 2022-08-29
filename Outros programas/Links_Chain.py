#Desafio para verificar se um lado da corrente é maior que o outro
#Challenge to check if the side of the chain is longer than the other
from enum import Enum
from itertools import count

class Side(Enum):
    none = 0
    left = 1
    right = 2

class ChainLink:

    def __init__(self):
        self._left = None
        self._right = None

    def append(self, link):
        if self._right is not None: raise Exception('Link already connected!')
        self._right = link
        link._left = self

    def longer_side(self):
        direita = []
        esquerda = []
        x = self
        while x is not None:
            if x._right in direita:
                break
            else:
                x = x._right
                direita = direita + [x]
             
        x = self
        while x is not None:
            if x._left in esquerda:
                break
            else:
                x = x._left
                esquerda = esquerda + [x]      

        if len(direita) > len(esquerda):
            resultado = Side.right
        elif len(esquerda) > len(direita):
            resultado = Side.left
        else:
            resultado = Side.none
        print (resultado)    
        return resultado
        
            
        

if __name__ == "__main__":
    left = ChainLink()
    middle = ChainLink()
    right = ChainLink()

    left.append(middle)
    middle.append(right)


    print(left.longer_side() == Side.right)
