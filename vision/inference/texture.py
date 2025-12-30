import numpy as np
from skimage.filters.rank import entropy
from skimage.morphology import disk

def surface_entropy(gray):
    return float(entropy(gray, disk(5)).mean())
