import matplotlib.pyplot as plt
import control as ct

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
        
    plt.xlabel('Tempo (s)')
    plt.ylabel('Resposta')
    plt.title('Resposta ao ',tipo)
    plt.grid(True)
    plt.show()   

def plota_bode(funcao_transferencia):
    
    #resposta em frequencia(bode)
    mag, phase, omega = ct.bode(funcao_transferencia)    

def plota_zero_polo(funcao_transferencia):     

        #polos e zeros
        poles = ct.pole(funcao_transferencia)
        zeros = ct.zero(funcao_transferencia)
        
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

            
    
