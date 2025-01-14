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
        
def simular_malha_fechada(planta,sensor,controlador):
 
        sistema_aberto = controlador * planta
        sistema_malha_fechada = ct.feedback(sistema_aberto, sensor)

        t, y = ct.step_response(sistema_malha_fechada)
        plt.plot(t, y)
        plt.xlabel('Tempo (s)')
        plt.ylabel('Resposta')
        plt.title('Resposta ao Degrau do Sistema em Malha Fechada')
        plt.grid(True)
        plt.show()
        
def equacao_caracteristica(denominador):
    
    termo_s_ordem_zero = denominador[2]
    termo_s_ordem_um = denominador[1]
    wn = np.sqrt(termo_s_ordem_zero)
    fator_amortecimento = termo_s_ordem_um / (2*wn)

    # plota a eq normalizada e os valores de wn e quissi
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off') #remove eixos
    
    texto = (
        "Resultados Para o Sistema de Segunda Ordem\n\n"
        f"Equação característica: {denominador[0]}s² + {denominador[1]}s + {denominador[2]}\n\n"
        f"Fator de Amortecimento (ξ): {fator_amortecimento:.4f}\n"
        f"Frequência Natural (ωn): {wn:.4f} rad/s\n\n"   
    )
    ax.text(0.5, 0.5, texto, ha='center', va='center', fontsize=12, wrap=True)
    
    #plt.savefig("resultados_sistema.jpeg", dpi=300, bbox_inches='tight')
    plt.show()
    
    
def criterios_desempenho(denominador):
    
    termo_s_ordem_zero = denominador[2]
    termo_s_ordem_um = denominador[1]
    wn = np.sqrt(termo_s_ordem_zero)
    fator_amortecimento = termo_s_ordem_um / (2*wn)
    
    num_omega = np.sqrt(1 - (pow(fator_amortecimento,2)))
    omega = np.arctan(num_omega/fator_amortecimento)
    wd = wn*num_omega
    

    #classificação do sistema
    if 0 < fator_amortecimento < 1: #resposta subamortecido

        tempo_subida = (np.pi - omega) / wd
        tempo_pico = np.pi/wd
        expoente_mp = -(np.pi*( fator_amortecimento/num_omega))
        mp = pow(np.e,expoente_mp)
        
        den_acomodacao = fator_amortecimento*wn
        ts_2 = 4 / den_acomodacao
        ts_5 = 3 / den_acomodacao
    
        texto = (
            f"Fator de Amortecimento (ξ): {fator_amortecimento:.4f}\n"
            f"Tempo de Subida (tr): {tempo_subida:.4f} s\n\n" 
            f"Tempo de Pico (tp): {tempo_pico:.4f} s\n\n"
            f"Sobressinal (Mp): {mp:.4f} \n\n" 
            f"Tempo de Acomodação 2% (ts(2%)): {ts_2:.4f} s\n\n"
            f"Tempo de Acomodação 5% (ts(5%)): {ts_5:.4f} s\n\n"    
        )
    
    elif fator_amortecimento < 0 : #sistema instavel
        texto = "Sistema Instavel !! "
        
    else: #sistema oscilatorio poro
        
        den_acomodacao = fator_amortecimento*wn
        ts_2 = 4 / den_acomodacao
        ts_5 = 3 / den_acomodacao
     
        texto = (
            f"Tempo de Acomodação 2% (ts(2%)): {ts_2:.4f} s\n\n"
            f"Tempo de Acomodação 5% (ts(5%)): {ts_5:.4f} s\n\n"    
        )   
      
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off') #remove eixos  
    ax.text(0.5, 0.5, texto, ha='center', va='center', fontsize=12, wrap=True)
    #plt.savefig("Desempenho.jpeg", dpi=300, bbox_inches='tight')
    plt.show()
    
def plota_lugar_de_raizes(num,den):
    ft = ct.tf(num,den)
        
    plt.figure()
    ct.rlocus(ft, klist=np.linspace(0, 10, 100))
    plt.grid(True)
    plt.xlabel('Parte Real')
    plt.ylabel('Parte imaginaria')
    plt.title('Diagrama de Lugar das Raízes')
    plt.show()
    #ainda falhando, não consegue variar o klist

#plota_lugar_de_raizes([1],[1,2,0])