# encoding:utf-8
from numpy import *
from test import dist_eclud


# 最大最小距离算法(t表示比例系数，默认为0.5)
def mm_dist(data_set, t=0.5):
    # 选取第一个样本为聚类中心
    centroids = []
    centroids.append(data_set[0])

    # 选取距离第一个样本最远的点为第二个聚类中心
    dist_to_first = []
    for vec in data_set:
        dist_to_first.append(dist_eclud(vec, centroids[0]))
    max_to_first = max(dist_to_first)
    centroids.append(data_set[[i for i, x in enumerate(dist_to_first) if x == max_to_first]])
    first_to_second = dist_eclud(centroids[0], centroids[1])

    while (True):
        # 计算其余各点到聚类中心的最小距离
        min_dists = []
        for vec in data_set:
            min_dists.append(vec, centroids)

        # 判断最大距离
        max_min_dist = max(min_dists)
        if max_min_dist > t * first_to_second:
            centroids.append(data_set[[i for i, x in enumerate(min_dists) if x == max_min_dist]])
        else:
            print("得到的聚类中心为：", centroids)
            # 将样本集按最小距离原则分到各类中去
            for vec in data_set:
                dists = []
                for centroid in centroids:
                    dists.append(vec, centroid)
                print("向量", vec, "属于聚类中心：", centroids[[i for i, x in enumerate(dists) if x == min(dists)]])
            return

    return


# 计算某个点到聚类中心的最小距离
def min_to_centroids(vec, centroids):
    dists = []
    for centroid in centroids:
        dists.append(vec, centroid)
    return min(dists)
