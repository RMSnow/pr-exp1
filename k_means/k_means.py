# encoding:utf-8
import matplotlib.pyplot as plt
from numpy import *
from test import dist_eclud
import pylab as pl


# 构建一个包含k个随机质心的集合
def rand_cent(data_mat, k):
    n = shape(data_mat)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        min_j = min(data_mat[:, j])
        range_j = float(max(data_mat[:, j]) - min_j)
        centroids[:, j] = mat(min_j + range_j * random.rand(k, 1))
    return centroids


# k_means算法
def k_means(data_mat, k, dist_meas=dist_eclud, create_cent=rand_cent):
    m = shape(data_mat)[0]
    cluster_assignment = mat(zeros((m, 2)))  # 簇分配结果矩阵：第一列记录簇索引值，第二列存储误差
    centroids = create_cent(data_mat, k)
    cluster_changed = True
    while cluster_changed:
        cluster_changed = False
        for i in range(m):
            min_dist = inf
            min_index = -1
            for j in range(k):
                dist_j_i = dist_meas(centroids[j], data_mat[i])
                if dist_j_i < min_dist:
                    min_dist = dist_j_i
                    min_index = j
            if cluster_assignment[i, 0] != min_index:
                cluster_changed = True
            cluster_assignment[i, :] = min_index, min_dist ** 2
        # print(centroids)
        for cent in range(k):
            pts_in_cluster = data_mat[nonzero(cluster_assignment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(pts_in_cluster, axis=0)
    return centroids, cluster_assignment


# 主流程
def show_k_means(data_mat, k=3):
    num_samples, dim = data_mat.shape
    centroids, cluster_assignment = k_means(data_mat, k)
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    for i in range(num_samples):
        mark_index = int(cluster_assignment[i, 0])
        plt.plot(data_mat[i, 0], data_mat[i, 1], mark[mark_index], marker='x')
    plt.show()
    return
