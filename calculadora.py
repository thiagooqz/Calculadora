import tkinter as tk
from math import sin, cos, tan, sqrt, log

# Função para processar as teclas pressionadas
def clique_botao(event):
    global expressao
    texto = event.widget.cget("text")
    if texto == "=":
        try:
            expressao = eval_expression(expressao)
            expressao = str(eval(expressao))
            visor_var.set(expressao)
        except Exception as e:
            expressao = ""
            visor_var.set("Erro")
    elif texto == "C":
        expressao = ""
        visor_var.set("")
    else:
        expressao += texto
        visor_var.set(expressao)

# Funções adicionais para seno, cosseno, tangente, raiz quadrada, logaritmo e potência
def eval_sin(x):
    return sin((x))

def eval_cos(x):
    return cos((x))

def eval_tan(x):
    return tan((x))

def eval_sqrt(x):
    return sqrt((x))

def eval_log(x):
    return log((x))

# Dicionário de funções para substituir nomes de funções em expressões
func_map = {
    "sin": "eval_sin",
    "cos": "eval_cos",
    "tan": "eval_tan",
    "sqrt": "eval_sqrt",
    "log": "eval_log",
    "^": "**"
}

def eval_expression(expr):
    for key, value in func_map.items():
        expr = expr.replace(key, value)
    return expr

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Científica")
janela.geometry("400x600")
janela.resizable(True, True)

expressao = ""
visor_var = tk.StringVar()

# Configuração do visor
visor = tk.Entry(janela, textvar=visor_var, font="Arial 20 bold", bd=10, insertwidth=2, width=14, borderwidth=4)
visor.grid(row=0, column=0, columnspan=5, sticky="nsew")

# Lista de botões com seus textos
botoes = [
    "7", "8", "9", "/", "sin",
    "4", "5", "6", "*", "cos",
    "1", "2", "3", "-", "tan",
    "0", ".", "=", "+", "sqrt",
    "C", "(", ")", "^", "log"
]

# Criação dos botões e posicionamento
linha = 1
coluna = 0
for botao in botoes:
    b = tk.Button(janela, text=botao, font="Arial 15 bold")
    b.grid(row=linha, column=coluna, sticky="nsew")
    b.bind("<Button-1>", clique_botao)
    coluna += 1
    if coluna == 5:
        coluna = 0
        linha += 1

# Configurar as linhas e colunas para expandir com o redimensionamento
for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
for i in range(5):
    janela.grid_columnconfigure(i, weight=1)

janela.mainloop()