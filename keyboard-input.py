import numpy as np
import matplotlib.pyplot as plt
def weather_model(x, a, b, c):
    return a*x**2 + b*x + c #equation
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

x_values = np.linspace(-10, 10, 400)
y_values = weather_model(x_values, a, b, c)
x_specific = float(input("Enter the specific value of x: "))
y_specific = weather_model(x_specific, a, b, c)
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c}')   
plt.plot([x_specific], [y_specific], 'ro')  
plt.title('Weather Model') 
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()
