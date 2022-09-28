import numpy as np

km = np.loadtxt('carros-km.txt')

km

anos = np.loadtxt('anos.txt')

anos

km_media = km/(2019 - anos)

km_media