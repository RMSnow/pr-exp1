# encoding: utf-8
from numpy import *


# 处理diff_mat.txt得到数据列表
def get_data_list(filename):
    data_list = []
    fr = open(filename)

    # 第一行：将属性名映射为相应的标签
    first_line = fr.readline().strip().split('\t')
    first_list = []
    for attr in first_line:
        if get_tag(attr) != 0:
            first_list.append(get_tag(attr))
    data_list.append(first_list)

    # 其余行：将对象标识符删去
    for line in fr.readlines():
        value = line.strip().split('\t')
        del value[0]
        data_list.append(value)

    return data_list


# 将各属性用tag来代替
def get_tag(attr):
    if attr == '类别' or attr == '颜色':  # 标称属性
        return 1
    elif attr == '质量级别':  # 序数属性
        return 2
    elif attr == '价格' or attr == '重量':  # 数值属性
        return 3
    elif attr == '等外':  # 非对称的二元属性
        return 4
    else:  # 其他
        return 0


# 处理序数属性(1-8)
def sequence_to_value(sequence):
    sequence_max = 8.0
    return (float(sequence) - 1.0) / (sequence_max - 1.0)


# 计算混合类型的差异性矩阵
def cal_diff_mat(data_list):
    n = len(data_list) - 1  # 共有n个对象
    p = len(data_list[0])  # 每个对象有p个属性
    print("数据文件中共有", n, "个对象，每个对象有", p, "个属性.")

    diff_mat = mat(zeros((n, n)))  # 生成n阶方阵
    attr_tag = data_list[0]  # 属性的标识符

    # 处理序数属性与数值属性
    value_attr_dict = {}
    for f in range(p):
        if attr_tag[f] == 2 or attr_tag[f] == 3:
            data_list_f = []
            max_key = '%d%s' % (f, '_max')
            min_key = '%d%s' % (f, '_min')

            if attr_tag[f] == 2:  # 序数属性
                for k in range(1, n + 1):
                    data_list[k][f] = sequence_to_value(data_list[k][f])
                    data_list_f.append(data_list[k][f])

            if attr_tag[f] == 3:  # 数值属性
                for k in range(1, n + 1):
                    data_list_f.append(float(data_list[k][f]))

            value_attr_dict[max_key] = max(data_list_f)
            value_attr_dict[min_key] = min(data_list_f)

    # 对矩阵的行进行遍历
    for i in range(n):
        # 对矩阵的列进行遍历
        for j in range(i):
            indicator = []  # 指示符
            d_i_j = []  # 相异性贡献
            sum_number = 0.0
            sum_fraction = 0.0

            # 对每个属性进行遍历
            for f in range(p):
                indicator_f = 1
                d_i_j_f = 0
                x_i_f = data_list[i + 1][f]
                x_j_f = data_list[j + 1][f]

                if attr_tag[f] == 1:  # 标称属性
                    if x_i_f == x_j_f:
                        d_i_j_f = 0
                    else:
                        d_i_j_f = 1
                elif attr_tag[f] == 2 or attr_tag[f] == 3:  # 处理后的序数属性／数值属性
                    max_key = '%d%s' % (f, '_max')
                    min_key = '%d%s' % (f, '_min')
                    max_f = value_attr_dict[max_key]
                    min_f = value_attr_dict[min_key]
                    d_i_j_f = abs(float(x_i_f) - float(x_j_f)) / (max_f - min_f)
                elif attr_tag[f] == 4:  # 非对称的二元属性
                    if x_i_f == x_j_f:
                        if x_j_f == 0:
                            indicator_f = 0
                    else:
                        d_i_j_f = 1

                indicator.append(indicator_f)
                d_i_j.append(d_i_j_f)

                sum_number += indicator_f * d_i_j_f
                sum_fraction += indicator_f

            diff_mat[i, j] = sum_number / sum_fraction

    print("得到的差异性矩阵如下：")
    print(diff_mat)
    print()
    return diff_mat


# 整个流程
def get_diff_mat(filename):
    data_list = get_data_list(filename)
    cal_diff_mat(data_list)
    return
