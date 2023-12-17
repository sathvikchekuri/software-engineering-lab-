import matplotlib.pyplot as plt
import numpy as np

def weather_model(x, a, b, c):
    return a * x**2 + b * x + c

with open('multi.txt', 'r') as f:
    lines = f.readlines()

x_values = np.linspace(-10, 10, 400)

plt.figure(figsize=(10, 6))

for line in lines:
    x_specific, a, b, c = map(float, line.split())

    y_values = weather_model(x_values, a, b, c)

    y_specific = weather_model(x_specific, a, b, c)

    plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c}')

    plt.plot(x_specific, y_specific, 'ro')

plt.title('Quadratic Functions')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()

plt.grid(True)

plt.show()
