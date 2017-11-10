# encoding: utf-8

import math
import pylab as pl


# 计算欧几里得距离
def dist(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


# dist_min
def dist_min(c_i, c_j):
    return min(dist(i, j) for i in c_i for j in c_j)


# dist_max
def dist_max(c_i, c_j):
    return max(dist(i, j) for i in c_i for j in c_j)


# dist_avg
def dist_avg(c_i, c_j):
    return sum(dist(i, j) for i in c_i for j in c_j) / (len(c_i) * len(c_j))


# 找到距离最小的下标
def find_min(m):
    min = 1000
    x = 0;
    y = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i != j and m[i][j] < min:
                min = m[i][j];
                x = i;
                y = j
    return (x, y, min)


# agnes算法
def agnes(data_set, dist_meas, k):
    c = []
    m = []
    for i in data_set:
        c_i = []
        c_i.append(i)
        c.append(c_i)
    for i in c:
        m_i = []
        for j in c:
            m_i.append(dist_meas(i, j))
        m.append(m_i)
    q = len(data_set)
    # 合并更新
    while q > k:
        x, y, min = find_min(m)
        c[x].extend(c[y])
        c.remove(c[y])
        m = []
        for i in c:
            m_i = []
            for j in c:
                m_i.append(dist_meas(i, j))
            m.append(m_i)
        q -= 1
    return c


# 主流程
def show_agnes(data_set, k=5):
    c = agnes(data_set, dist_avg, k)
    col_value = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
    for i in range(len(c)):
        coo_x = []  # x坐标列表
        coo_y = []  # y坐标列表
        for j in range(len(c[i])):
            coo_x.append(c[i][j][0])
            coo_y.append(c[i][j][1])
        pl.scatter(coo_x, coo_y, marker='x', color=col_value[i % len(col_value)])

    pl.legend(loc='upper right')
    pl.show()
    return
