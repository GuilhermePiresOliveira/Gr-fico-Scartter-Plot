# Import
import matplotlib.pyplot as plt
import numpy as np

# Massa de Dados.
x = np.random.rand(50)
y = 2 * x + 1 + 0.1 * np.random.randn(50)

#Define o tamanho
plt.figure(figsize=(4,4))

#Configurações
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()