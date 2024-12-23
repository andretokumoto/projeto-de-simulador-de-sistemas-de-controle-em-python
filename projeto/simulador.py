import analise_de_sistemas as analise
from scipy import signal


def main():
    
    numerador = 1
    denominador = [1,2]
    
    transferencia = analise.funcao_transferencia(numerador,denominador)
    analise.plota_resposta(transferencia,'degrau')
    #analise.plota_zero_polo(transferencia)
    
main()

