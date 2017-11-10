# encoding:utf-8

from diff_mat.diff_mat import *
from k_means.k_means import *
from hierarchical.agnes import *
from isodata.isodata import *
from max_min_dist.mm_dist import *


# 测试所有用例
def test():
    while 1:
        print("---------------------")
        print("请选择一项操作：")
        print("1. 计算混合型属性差异性矩阵")
        print("2. 最大最小距离算法")
        print("3. 层次聚类算法")
        print("4. K-means算法")
        print("5. ISODATA算法")
        print("6. 退出")
        choice = input("请输入您的选择：")
        print("---------------------")

        if choice == '1':
            # 混合型属性差异性矩阵
            print("正在处理数据文件data/diff_mat.txt...")
            print()
            get_diff_mat("data/diff_mat.txt")
        elif choice == '2':
            # 最大最小距离算法
            print("正在处理数据文件data/test_data2.txt...")
            data_set, data_mat = load_data_mat("data/test_data2.txt")
            print()
            show_mm_dist(data_mat)
        elif choice == '3':
            # 层次聚类算法
            print("正在处理数据文件data/test_data2.txt...")
            print()
            data_set, data_mat = load_data_mat("data/test_data2.txt")
            show_agnes(data_set)
        elif choice == '4':
            # K-means算法
            print("正在处理数据文件data/test_data2.txt...")
            data_set, data_mat = load_data_mat("data/test_data2.txt")
            print()
            show_k_means(data_mat)
        elif choice == '5':
            # ISODATA算法
            print("正在处理数据文件data/test_data2.txt...")
            data_set, data_mat = load_data_mat("data/test_data2.txt")
            print()
            show_isodata(data_mat)
        elif choice == '6':
            return
        else:
            print("[ERROR]输入非法，请输入1-6")
    return


# 将文本文件导入一个列表中(k-means)
def load_data_mat(filename):
    data_set = []
    fr = open(filename)
    for line in fr.readlines():
        cur_line = line.strip().split(',')
        flt_line = map(float, cur_line)
        data_set.append(list(flt_line))
    data_mat = mat(data_set)
    return data_set, data_mat


# 计算欧拉距离
def dist_eclud(vec_a, vec_b):
    return sqrt(sum(power(vec_a - vec_b, 2)))


if __name__ == '__main__':
    test()
