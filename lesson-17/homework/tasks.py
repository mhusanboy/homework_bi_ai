import matplotlib.pyplot as plt
import numpy as np 

def problem1():
    x = np.linspace(-10, 10, 10000)
    y = x**2 - 4*x + 4
    plt.plot(x, y, label = 'f(x) = x^2 - 4x + 4')
    plt.xlabel('x')
    plt.ylabel('y', rotation = 0)
    plt.legend()
    plt.title('f(x)')
    plt.show()

def problem2():
    x = np.linspace(0, np.pi*2, 10000)
    plt.plot(x, np.sin(x), 'r--',label = 'sin(x)')
    plt.plot(x, np.cos(x), 'b:',label = 'cos(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('sin(x) and cos(x)')
    plt.show()

def problem3():
    x = np.linspace(-10, 10, 10000)
    plt.subplot(3, 3, 1)
    plt.plot(x, x**3, 'r')
    plt.title('x^3')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.subplot(3, 3, 3)
    plt.plot(x, np.sin(x), 'b')
    plt.title('sin(x)')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.subplot(3, 3, 7)
    plt.plot(x, np.e**x, 'g')
    plt.title('e^x')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.subplot(3, 3, 9)
    x = np.linspace(0, 10, 10000)
    plt.plot(x, np.log(x + 1), 'm')
    plt.title('log(x + 1)')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

def problem4():
    x = np.random.uniform(0, 10, 100)
    y = np.random.uniform(0, 10, 100)
    c = np.random.rand(100)     
    markers = np.random.choice(['o', 's', 'D', '^', 'v', 'p', '*', 'x'], 100)
    for i in range(100):
        plt.scatter(x[i], y[i], c = [c[i]],marker = markers[i], cmap = 'viridis', edgecolors='black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Scatter plot of 100 random points')
    plt.grid(True)
    plt.show()

def problem5():
    values = np.random.randn(1000)
    plt.hist(values, bins = 30, alpha = 0.8, color = 'blue', edgecolor = 'black')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of random numbers')
    plt.show()

def problem6():
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    x = np.linspace(-5, 5, 1000)
    y = np.linspace(-5, 5, 1000)
    xx, yy = np.meshgrid(x, y)
    zz = np.cos(xx**2 + yy**2)
    surf = ax.plot_surface(xx, yy, zz, cmap = 'viridis')
    fig.colorbar(surf, fraction=0.02, pad=0.11)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.set_title('3D Surface Plot of f(x, y) = cos(x^2 + y^2)')
    plt.show()

    
def problem7():
    categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    colors = ['r', 'm', 'b', 'g', 'y']
    values = [200, 150, 250, 175, 225]
    plt.bar(categories, values, color = colors, width = 0.3)
    plt.xlabel('Products')
    plt.ylabel('Sale values')
    plt.title('Sale valuse for company products')
    plt.show()

def problem8():
    categories = ['Category A', 'Category B', 'Category C']
    periods = ['T1', 'T2', 'T3', 'T4']
    datas = np.array([
        [2, 4, 6, 8],
        [3, 9, 12, 6],
        [20, 15, 10, 5]
    ])
    plt.bar(periods, datas[0], label = 'Category A')
    plt.bar(periods, datas[1], bottom = datas[0], label = 'Category C')
    plt.bar(periods, datas[2], bottom=datas[0] + datas[1], label = 'Category C')

    plt.title('Contribution of three different categories over four periods')
    plt.legend()
    plt.show()
problem8()