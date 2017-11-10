# encoding:utf-8
from numpy import *
from k_means.k_means import rand_cent
from test import dist_eclud
from isodata.Cluster import Cluster


# 参数说明：
# （1）exp_clusters：希望的聚类中心数目
# （2）theta_n：每个聚类中最少的样本数（判断是否可以作为独立的聚类）
# （3）theta_s：聚类域中样本的标准差阈值（判断是否要分裂）
# （4）theta_c：两聚类中心之间的最短距离（判断是否要合并）
# （5）comb_l：在一次迭代中允许合并的聚类中心的最大对数
# （6）max_its：允许迭代的次数


# 迭代自组织算法
def isodata(data_set, init_clusters=5, exp_clusters=3, theta_n=3, theta_s=0.5, theta_c=2, comb_l=2, max_its=5):
    # Step1：从数据集中随机选取clusters个样本作为初始中心
    centroids = rand_cent(data_set, init_clusters)
    clusters = []
    for centroid in centroids:
        cluster = Cluster(centroid)
        clusters.append(cluster)

    its = 0
    while (its <= max_its):
        cluster_flag = False
        while (cluster_flag == False):
            # Step2：对每个样本，按照最小距离分至其所属的聚类中心
            for vec in data_set:
                dists = []
                for cluster in clusters:
                    dists.append(dist_eclud(vec, cluster.centroid))
                clusters[[i for i, x in enumerate(dists) if x == min(dists)]].add_vec(vec)

            # Step3：根据theta_n进行判断是否需丢弃某类
            for cluster in clusters:
                if cluster.size < theta_n:
                    clusters.remove(cluster)
                else:
                    if cluster == clusters[-1]:
                        cluster_flag == True

        # Step4：针对每个类，重新计算其聚类中心（属于该类所有样本的质心）
        for cluster in clusters:
            cluster.centroid = sum(cluster.vec_set) / len(cluster.vec_set)

        # Step5：若clusters <= exp_clusters ／ 2，则前往分裂操作
        # Step6：若clusters > exp_clusters * 2，则前往合并操作
        if len(clusters) <= exp_clusters / 2:
            clusters = divide(clusters, theta_s, theta_n)
        elif len(clusters) > exp_clusters * 2:
            clusters = merge(clusters, theta_c, comb_l)

        # Step7：如果到达最大迭代次数则终止，否则返回Step2
        its += 1

    return


# 合并操作
def merge(clusters, theta_c, comb_l):
    comb = 0
    return m_merge(clusters, theta_c, comb_l, comb)


def m_merge(clusters, theta_c, comb_l, comb):
    # Step1：计算当前聚类中心两两之间的距离，用矩阵D表示
    clusters_dist_mat = mat(zeros((len(clusters), len(clusters))))
    for i in range(shape(clusters_dist_mat)[0]):
        for j in range(i):
            clusters_dist_mat[i, j] = dist_eclud(clusters[i].centroid, clusters[j].centroid)
            # Step2：将距离低于阈值的(i, j)合并至i，并计算新的聚类中心
            if clusters_dist_mat[i, j] < theta_c:
                if comb == comb_l:
                    return clusters
                else:
                    n_i = len(clusters[i].vec_set)
                    n_j = len(clusters[j].vec_set)
                    m_i = clusters[i].centroid
                    m_j = clusters[j].centroid
                    clusters[i].centroid = (n_i * m_i + n_j * m_j) / (n_i + n_j)
                    clusters.pop(j)
                    return m_merge(clusters, theta_c, comb_l, comb + 1)


# 分裂操作
def divide(clusters, theta_s, theta_n):
    # Step1：计算每个类别下，所有样本在每个维度下的方差sigma
    # Step2：在每个类别的所有方差中，得到sigma_max
    for cluster in clusters:
        sigmas = []
        for dimension in range(len(cluster.centroid)):
            vec_dimension = []
            for vec in cluster.vec_set:
                vec_dimension.append(vec[dimension])
            sigmas.append(var(vec_dimension))
        sigma_max = max(sigmas)
        # Step3：将sigma_max高于阈值theta_s的类别分裂
        if sigma_max > theta_s and cluster.size >= theta_n * 2:
            new_cluster = Cluster(cluster.centroid + sigma_max)
            clusters.append(new_cluster)
            cluster.centroid -= sigma_max
            return clusters
        else:
            continue

    return clusters
