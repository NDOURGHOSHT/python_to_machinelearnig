# Écrivez votre code pour le défi ici
import numpy as np
temperatures = np.array([22.5, 18.0, 25.3, 19.8])
print(temperatures)
print("Temperature 1D:",temperatures.shape)
print("convertir de Celsius en Fahrenheit", temperatures*9/5+32 )
print("-"*10)

print("la température maximale du tableau final ",(temperatures*9/5+32).max())