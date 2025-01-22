import tkinter as tk
from tkinter import messagebox
import analise_de_sistemas as analise


def simular_malha_fechada():
    try:
        num_planta = list(map(float, entry_numerador_planta.get().split()))
        den_planta = list(map(float, entry_denominador_planta.get().split()))
        planta = analise.funcao_transferencia(num_planta, den_planta)

        num_sensor = list(map(float, entry_numerador_sensor.get().split()))
        den_sensor = list(map(float, entry_denominador_sensor.get().split()))
        sensor = analise.funcao_transferencia(num_sensor, den_sensor)

        num_controlador = list(map(float, entry_numerador_controlador.get().split()))
        den_controlador = list(map(float, entry_denominador_controlador.get().split()))
        controlador = analise.funcao_transferencia(num_controlador, den_controlador)

        analise.simular_malha_fechada(planta, sensor, controlador)

    except Exception as e:
        messagebox.showerror("Erro", str(e))


# Interface gráfica
def criar_funcao():
    try:
        num = list(map(float, entry_numerador.get().split()))
        den = list(map(float, entry_denominador.get().split()))
        ft = analise.funcao_transferencia(num, den)
        tipo = var_tipo.get()
        if tipo == 'impulso' or tipo == 'degrau':
            analise.plota_resposta(ft, tipo)
        elif tipo == 'bode':
            analise.plota_bode(ft)
        elif tipo == 'polos_e_zeros':
            analise.plota_zero_polo(ft)
        elif tipo == 'equacao_caracteristica':
            analise.equacao_caracteristica(den)
        elif tipo == 'desempenho':
            analise.criterios_desempenho(den)  
        elif tipo=='malha_fechada':
            simular_malha_fechada()
        else:
            raise ValueError("Tipo inválido.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


# Cria a janela principal
window = tk.Tk()
window.title("Simulador de Sistemas de Controle")

# Entrada de numerador e denominador
tk.Label(window, text="Numerador:").grid(row=0, column=0, padx=10, pady=10)
entry_numerador = tk.Entry(window)
entry_numerador.grid(row=0, column=1, padx=10, pady=10)
entry_numerador.insert(0, "1")

tk.Label(window, text="Denominador:").grid(row=1, column=0, padx=10, pady=10)
entry_denominador = tk.Entry(window)
entry_denominador.grid(row=1, column=1, padx=10, pady=10)
entry_denominador.insert(0, "1 1")

# Entrada de numerador e denominador da planta
tk.Label(window, text="Numerador Planta:").grid(row=2, column=0, padx=10, pady=10)
entry_numerador_planta = tk.Entry(window)
entry_numerador_planta.grid(row=2, column=1, padx=10, pady=10)
entry_numerador_planta.insert(0, "1")

tk.Label(window, text="Denominador Planta:").grid(row=3, column=0, padx=10, pady=10)
entry_denominador_planta = tk.Entry(window)
entry_denominador_planta.grid(row=3, column=1, padx=10, pady=10)
entry_denominador_planta.insert(0, "1 2 1")

# Entrada de numerador e denominador do sensor
tk.Label(window, text="Numerador Sensor:").grid(row=4, column=0, padx=10, pady=10)
entry_numerador_sensor = tk.Entry(window)
entry_numerador_sensor.grid(row=4, column=1, padx=10, pady=10)
entry_numerador_sensor.insert(0, "1")

tk.Label(window, text="Denominador Sensor:").grid(row=5, column=0, padx=10, pady=10)
entry_denominador_sensor = tk.Entry(window)
entry_denominador_sensor.grid(row=5, column=1, padx=10, pady=10)
entry_denominador_sensor.insert(0, "1")

# Entrada de numerador e denominador do controlador
tk.Label(window, text="Numerador Controlador:").grid(row=6, column=0, padx=10, pady=10)
entry_numerador_controlador = tk.Entry(window)
entry_numerador_controlador.grid(row=6, column=1, padx=10, pady=10)
entry_numerador_controlador.insert(0, "1 1")

tk.Label(window, text="Denominador Controlador:").grid(row=7, column=0, padx=10, pady=10)
entry_denominador_controlador = tk.Entry(window)
entry_denominador_controlador.grid(row=7, column=1, padx=10, pady=10)
entry_denominador_controlador.insert(0, "1 0")

# Opções de tipo de análise
var_tipo = tk.StringVar(value='impulso')
tk.Radiobutton(window, text="Impulso", variable=var_tipo, value='impulso').grid(row=8, column=0, padx=10, pady=5)
tk.Radiobutton(window, text="Degrau", variable=var_tipo, value='degrau').grid(row=8, column=1, padx=10, pady=5)
tk.Radiobutton(window, text="Bode", variable=var_tipo, value='bode').grid(row=9, column=0, padx=10, pady=5)
tk.Radiobutton(window, text="Polos e Zeros", variable=var_tipo, value='polos_e_zeros').grid(row=9, column=1, padx=10, pady=5)
tk.Radiobutton(window, text="Equação Caracteristica", variable=var_tipo, value='equacao_caracteristica').grid(row=10, column=0, padx=10, pady=5)
tk.Radiobutton(window, text="Fatores de desempenho", variable=var_tipo, value='desempenho').grid(row=10, column=1, padx=10, pady=5)
tk.Radiobutton(window, text="Malha Fechada", variable=var_tipo, value='malha_fechada').grid(row=11, column=0, padx=10, pady=5)

# Botão para executar a análise
button_executar = tk.Button(window, text="Executar", command=criar_funcao)
button_executar.grid(row=12, column=0, columnspan=2, pady=10)

# Botão para simular malha fechada
#button_simular = tk.Button(window, text="Simular Malha Fechada", command=simular_malha_fechada)
#button_simular.grid(row=13, column=0, columnspan=2, pady=10)

# Inicia o loop principal da interface gráfica
window.mainloop()
