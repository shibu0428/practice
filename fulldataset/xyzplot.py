import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    x_values = []
    y_values = []
    z_values = []

    for line in lines:
        data = line.split()
        x_values.append(float(data[0]))
        y_values.append(float(data[1]))
        z_values.append(float(data[2]))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_values, y_values, z_values)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

if __name__ == "__main__":
    filename = input("ファイル名を入力してください: ")
    plot_3d_line(filename)