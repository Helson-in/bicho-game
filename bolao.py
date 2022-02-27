import random as rm
import numpy as np
import pandas as pd

name = input("Nome: ")
logra = input("Endr: ")
cartel = input("Cartela: ")
teste1 = np.array(
    [name, logra, cartel]
)

name
logra
cartel
# a = np.shape() --> Visualizar numero de Linhas e Colunas da matriz
# slice = Corte de matriz / Inicio e termino de Matriz // Linha, Coluna, Intervalo de elementos
# Matriz2 = (a[0:1:2, 2:3]); Matriz1 = (a[0:1:-2, 2:3])
# Função de Array para colocar numeros de 0 à X de forma automatica(ARANJOS)
# Parametros = Inicio, Fim, Intervalo
b = np.arange(0, 10, 1)
# Função de Array para elementos em determinado intervalo
# Parametros = Elem Inicial, Final, Quantidade de elementos entre o Inicial e o Final
# endpoint = Não incluir elemento final
c = np.linspace(1, 5, 10, endpoint=False)
# Criação de matriz de 1 ou 0
d = np.ones((2, 2))
g = np.zeros(10)
# Matriz de ordem X com elementos aleatorios
e = np.random.rand(5)

print(teste1)
