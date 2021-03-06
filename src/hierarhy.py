#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "esemi"

from scipy.spatial.distance import pdist
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

from shared import get_data


def hierarchy_draw(Z, labels, level):
    """Рисуем дендрограмму и сохраняем её"""

    plt.figure()
    hierarchy.dendrogram(Z, labels=labels, color_threshold=level, leaf_font_size=5, count_sort=True)
    plt.show()

if __name__ == '__main__':
    names, data = get_data()

    dist = pdist(data, 'euclidean')
    plt.hist(dist, 500, color='green', alpha=0.5)
    Z = hierarchy.linkage(dist, method='average')

    hierarchy_draw(Z, names, .25)