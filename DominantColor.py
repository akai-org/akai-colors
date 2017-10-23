import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.cluster import KMeans

# https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097

class DominantColor(object):
    def __init__(self, file):
        file = self.prepareFile(file)
        clt = self.performKMeans(file)
        hist = self.findHistogram(clt)
        dominant = self.findDominant(hist, clt)
        self.color = self.nameColor(dominant)

    def prepareFile(self, file):
        file = cv2.imdecode(file, cv2.IMREAD_COLOR)
        file = cv2.cvtColor(file, cv2.COLOR_BGR2RGB)
        file = file.reshape(file.shape[0] * file.shape[1],3)
        return file

    def performKMeans(self, file):
        clt = KMeans(n_clusters=3) #cluster number
        return clt.fit(file)


    def findHistogram(self, clt):
        numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
        (hist, _) = np.histogram(clt.labels_, bins=numLabels)

        hist = hist.astype("float")
        hist /= hist.sum()
        return hist

    def findDominant(self, hist, clt):
        zipped = zip(hist, clt.cluster_centers_)
        return max(zipped, key=lambda tup: tup[0])[1]

    def get(self):
        return self.color

    def nameColor(self, dominant):
        df = -1
        c = ''

        for color in colors:
            color_rgb = color[1]
            cdf = math.pow(color_rgb[0] - dominant[0], 2) + math.pow(color_rgb[1] - dominant[1], 2) + math.pow(color_rgb[2] - dominant[2], 2)
            if df == -1 or df > cdf:
                df = cdf
                c = color[0]
        return (c, [int(round(x)) for x in dominant])

colors = [
    ('Black', (0, 0, 0)),
    ('White', (255, 255, 255)),
    ('Red', (255, 0, 0)),
    ('Green', (0, 0, 255)),
    ('Blue', (0, 0, 255)),
    ('Yellow', (255, 255, 0)),
    ('Purple', (128, 0, 128)),
    ('Orange', (100, 65, 0)),
    ('Pink', (100, 75, 80)),
    ('Grey', (128, 128, 128))
]
