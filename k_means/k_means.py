# encoding:utf-8
from numpy import *


# 将文本文件导入一个列表中
def load_data_set(filename):
    data_mat = []
    fr = open(filename)
    for line in fr.readlines():
        cur_line = line.strip().split('\t')
        flt_line = map(float, cur_line)
        data_mat.append(flt_line)
    return data_mat


# 计算欧拉距离
def dist_eclud(vec_a, vec_b):
    return sqrt(sum(power(vec_a, vec_b, 2)))


# 构建一个包含k个随机质心的集合
def rand_cent(data_set, k):
    n = shape(data_set)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        min_j = min(data_set[:, j])
        range_j = float(max(data_set[:, j]) - min_j)
        centroids[:, j] = min_j + range_j * random.rand(k, 1)
    return centroids


# k_means算法
def k_means(data_set, k, dist_meas=dist_eclud, create_cent=rand_cent):
    m = shape(data_set)[0]
    cluster_assignment = mat(zeros((m, 2)))     # 簇分配结果矩阵：第一列记录簇索引值，第二列存储误差
    centroids = create_cent(data_set, k)
    cluster_changed = True
    while cluster_changed:
        cluster_changed = False
        for i in range(m):
            min_dist = inf
            min_index = -1
            for j in range(k):
                dist_j_i = dist_meas(centroids[j, :], data_set[i, :])
                if dist_j_i < min_dist:
                    min_dist = dist_j_i
                    min_index = j
            if cluster_assignment[i, 0] != min_index:
                cluster_changed = True
            cluster_assignment[i, :] = min_index, min_dist ** 2
        print(centroids)
        for cent in range(k):
            pts_in_cluster = data_set[nonzero(cluster_assignment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(pts_in_cluster, axis=0)
    return centroids, cluster_assignment
