import matplotlib.pyplot as plt
import numpy as np

a = 0.5
b = 2
c = 1

def weather_model(x):
    return a * x**2 + b * x + c

x_values = np.linspace(-10, 10, 100)  

y_values = weather_model(x_values)

plt.plot(x_values, y_values, label='Weather Model')

plt.title('Weather Model')
plt.xlabel('Time')
plt.ylabel('Temperature')

plt.legend()

plt.grid(True)
plt.show()
