import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageShow
from tqdm import tqdm
########################################################################################################################


# Shape of Model
n = 100

# lattice Maker
lattice = np.array(np.random.choice([1, -1], size=(n, n)))


# Image Maker Function
def img(x):
    image = Image.fromarray(np.uint8(lattice * 255))
    ImageShow.show(image, title=None)


# Calling Image Maker
# img(lattice)

def E_checker(x, T):
    Kb = 1.3806 * 1e-23
    r = np.random.random()
    if x < 0:
        return "flip"
    if (x > 0) and (np.exp((-1 * x) / Kb * T) > r):
        return "flip"
    else:
        return "same"


# Hamiltonian Calculator
def Hamiltonian(lattice, T):
    global ham
    hams = []
    for i in range(10):
        for j in range(10000):
            x = np.random.randint(0, n)
            y = np.random.randint(0, n)
            ham = -1 * (lattice[(x + 1) % n][y] + lattice[(x - 1) % n][y] + lattice[x][(y + 1) % n] + lattice[x][
                (y - 1) % n])

            check = E_checker(ham, T)
            if check == "flip":
                lattice[x][y] *= -1
            if check == "same":
                pass

        hams.append(ham)
    return hams


def graph(x, y):
    plt.plot(x, y)
    plt.legend()
    plt.grid()
    plt.show()

img(lattice)
Temps = np.linspace(1.0, 200, 50)

Energy = []
for i in tqdm(Temps):
    E = Hamiltonian(lattice, i)
    Energy.append(E)


graph(Temps, Energy)
img(lattice)

