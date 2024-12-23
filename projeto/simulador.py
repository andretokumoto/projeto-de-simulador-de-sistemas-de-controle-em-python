import tkinter as tk
from tkinter import messagebox
import analise_de_sistemas as analise

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
        else:
            raise ValueError("Tipo inválido.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Cria a janela principal
window = tk.Tk()
window.title("Simulador de sistemas de controle")

# entrada de numerador e denominador
tk.Label(window, text="Numerador:").grid(row=0, column=0, padx=10, pady=10)
entry_numerador = tk.Entry(window)
entry_numerador.grid(row=0, column=1, padx=10, pady=10)
entry_numerador.insert(0, "1")

tk.Label(window, text="Denominador:").grid(row=1, column=0, padx=10, pady=10)
entry_denominador = tk.Entry(window)
entry_denominador.grid(row=1, column=1, padx=10, pady=10)
entry_denominador.insert(0, "1 1")

# Opções de tipo de análise
var_tipo = tk.StringVar(value='impulso')
tk.Radiobutton(window, text="Impulso", variable=var_tipo, value='impulso').grid(row=2, column=0, padx=10, pady=5)
tk.Radiobutton(window, text="Degrau", variable=var_tipo, value='degrau').grid(row=2, column=1, padx=10, pady=5)
tk.Radiobutton(window, text="Bode", variable=var_tipo, value='bode').grid(row=3, column=0, padx=10, pady=5)
tk.Radiobutton(window, text="Polos e Zeros", variable=var_tipo, value='polos_e_zeros').grid(row=3, column=1, padx=10, pady=5)

# Botão para executar a análise
button_executar = tk.Button(window, text="Executar", command=criar_funcao)
button_executar.grid(row=4, column=0, columnspan=2, pady=10)

# Inicia o loop principal da interface gráfica
window.mainloop()
