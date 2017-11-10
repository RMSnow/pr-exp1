# encoding:utf-8
from numpy import *
from test import dist_eclud, plt


# 最大最小距离算法(theta表示比例系数，默认为0.5)
def mm_dist(data_mat, theta=0.5):
    cluster_assignment = []  # 簇分配结果
    # 选取第一个样本为聚类中心
    centroids = []
    centroids.append(data_mat[0])

    # 选取距离第一个样本最远的点为第二个聚类中心
    dist_to_first = []
    for vec in data_mat:
        dist_to_first.append(dist_eclud(vec, centroids[0]))
    max_to_first = max(dist_to_first)
    centroids.append(data_mat[[i for i, x in enumerate(dist_to_first) if x == max_to_first]])
    first_to_second = dist_eclud(centroids[0], centroids[1])

    while 1:
        # 计算其余各点到聚类中心的最小距离
        min_dists = []
        for vec in data_mat:
            min_dists.append(min_to_centroids(vec, centroids))

        # 判断最大距离
        max_min_dist = max(min_dists)
        if max_min_dist > theta * first_to_second:
            centroids.append(data_mat[[i for i, x in enumerate(min_dists) if x == max_min_dist]])
        else:
            print("得到的聚类中心为：", centroids)
            # 将样本集按最小距离原则分到各类中去
            for vec in data_mat:
                dists = []
                for centroid in centroids:
                    dists.append(dist_eclud(vec, centroid))
                min_index = 0
                for dist in dists:
                    if dists[min_index] == min(dists):
                        break
                    else:
                        min_index += 1
                # print("向量", vec, "属于聚类中心：", centroids[min_index])
                cluster_assignment.append(min_index)
            return
    return cluster_assignment


# 计算某个点到聚类中心的最小距离
def min_to_centroids(vec, centroids):
    dists = []
    for centroid in centroids:
        dists.append(dist_eclud(vec, centroid))
    return min(dists)


# 主流程
def show_mm_dist(data_mat):
    num_samples, dim = data_mat.shape
    cluster_assignment = mm_dist(data_mat)
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    for i in range(num_samples):
        # mark_index = int(cluster_assignment[i, 0])
        mark_index = int(cluster_assignment[i])
        plt.plot(data_mat[i, 0], data_mat[i, 1], mark[mark_index], marker='x')
    plt.show()
    return
