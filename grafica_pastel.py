import matplotlib.pyplot as plt

# Lista de etiquetas para cada categoría
frutas = ["manzana", "mango", "fresa"]
# Lista de pesos para cada categoría
cantidades = [10, 40, 25]

# Sintaxis: plt.pie(pesos, labels=etiquetas)
plt.pie(cantidades, labels=frutas)

# Mostramos la gráfica
plt.show()

