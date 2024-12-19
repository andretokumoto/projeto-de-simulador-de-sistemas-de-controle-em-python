import analise_de_sistemas as analise
import numpy as np
from scipy import signal


def main():
    
    numerador = 1
    denominador = [1,1]
    
    transferencia = analise.funcao_transferencia(numerador,denominador)
    print(type(transferencia))
    print()
    print(transferencia)
    
main()

