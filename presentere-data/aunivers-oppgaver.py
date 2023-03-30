import matplotlib.pyplot as plt
import numpy as np

'''def f(x):
    return (4)*(x**3) - (x**5)

xverdier = []
yverdier = []

for xverdi in range(-2, 3):
    xverdier.append(xverdi)
    yverdier.append(f(xverdi))

plt.plot(xverdier, yverdier)
plt.show()'''

def f(x):
    return 4*(x**3) - (x**5)

xverdier = np.linspace(-3, 3, 1000)
yverdier = f(xverdier)

plt.plot(xverdier, yverdier)
plt.show()
print(xverdier)