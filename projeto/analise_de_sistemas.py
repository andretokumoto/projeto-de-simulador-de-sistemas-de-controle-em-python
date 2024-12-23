import matplotlib.pyplot as plt
import control as ct
import numpy as np
from scipy import signal

#retorna a função transferencia para os indices da função
def funcao_transferencia(numerador,denominador):
    return ct.TransferFunction(numerador,denominador)

def plota_resposta(funcao_transferencia,tipo):
    
    #resposta ao impulso
    if tipo == 'impulso':     
        t,y = ct.impulse_response(funcao_transferencia)
 
     #resposta ao impulso
    if tipo == 'degrau':     
        t,y = ct.step_response(funcao_transferencia)  
        
    title = 'Resposta ao '+tipo
    plt.plot(t,y)
    plt.xlabel('Tempo (s)')
    plt.ylabel('Resposta')
    plt.title(title)
    plt.grid(True)
    plt.show()   

def plota_bode(funcao_transferencia):
    
    # Resposta em frequência (Bode)
    mag, phase, omega = ct.bode(funcao_transferencia, plot=False)
    
    # Cria a figura
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    
    # Magnitude
    ax1.semilogx(omega, 20 * np.log10(mag))
    ax1.set_title('Diagrama de Bode')
    ax1.set_ylabel('Magnitude (dB)')
    ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Fase
    ax2.semilogx(omega, phase * (180.0 / np.pi))
    ax2.set_xlabel('Frequência (rad/s)')
    ax2.set_ylabel('Fase (graus)')
    ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Exibe o gráfico
    plt.tight_layout()
    plt.show()


def plota_zero_polo(funcao_transferencia):     

        #polos e zeros
        poles = ct.poles(funcao_transferencia)
        zeros = ct.zeros(funcao_transferencia)
        
        # Plotar polos e zeros
        plt.figure()
        plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='red', label='Zeros')
        plt.scatter(np.real(poles), np.imag(poles), marker='x', color='blue', label='Polos')

        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(0, color='black', lw=0.5)
        plt.grid(True, which='both', linestyle='--', lw=0.5)

        plt.xlabel('Parte Real')
        plt.ylabel('Parte Imaginária')
        plt.title('Polos e Zeros')
        plt.legend()
        plt.show()