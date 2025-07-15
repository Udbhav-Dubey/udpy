import numpy as np
def gaussian_filter(kernel_size, sigma=1, muu=0):
    x, y = np.meshgrid(np.linspace(-1, 1, kernel_size),
                       np.linspace(-1, 1, kernel_size))
    dst = np.sqrt(x**2 + y**2)

    normal = 1 / (2 * np.pi * sigma**2)
    gauss = np.exp(-((dst - muu)**2 / (2.0 * sigma**2))) * normal

    return gauss  
kernel_size = 5
gaussian = gaussian_filter(kernel_size)
print("Gaussian filter of {} X {}:".format(kernel_size, kernel_size))
print(gaussian)
