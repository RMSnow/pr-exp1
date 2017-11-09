# encoding:utf-8

from diff_mat.diff_mat import *


# 测试所有用例
def test():
    # 混合型属性差异性矩阵
    get_diff_mat("data/diff_mat.txt")
    return


# 将文本文件导入一个列表中(k-means)
def load_data_set(filename):
    data_mat = []
    fr = open(filename)
    for line in fr.readlines():
        cur_line = line.strip().split('\t')
        flt_line = map(float, cur_line)
        data_mat.append(flt_line)
    return data_mat


# 将文本文件导入一个列表中(mm_dist)(最终得到一个列表，其中的元素就是每一个向量)
def load_data_set(filename, choice):
    pass

# 计算欧拉距离
def dist_eclud(vec_a, vec_b):
    return sqrt(sum(power(vec_a, vec_b, 2)))

if __name__ == '__main__':
    test()
