# encoding:utf-8
from numpy import *


# 参数说明：
# （1）exp_clusters：希望的聚类中心数目
# （2）theta_n：每个聚类中最少的样本数（判断是否可以作为独立的聚类）
# （3）theta_s：聚类域中样本的标准差阈值（判断是否要分裂）
# （4）theta_c：两聚类中心之间的最短距离（判断是否要合并）
# （5）comb_l：在一次迭代中允许合并的聚类中心的最大对数
# （6）max_its：允许迭代的次数


# 迭代自组织算法
def isodata(data_set, exp_clusters=3, theta_n=3, theta_s=0.5, theta_c=2, comb_l=2, max_its=5):
    # Step1：从数据集中随机选取exp_clusters个样本作为初始中心
    # Step2：对每个样本，按照最小距离分至其所属的聚类中心
    # Step3：根据theta_n进行判断s是否需丢弃某类
    # Step4：针对每个类，重新计算其聚类中心（属于该类所有样本的质心）
    # Step5：若clusters <= exp_clusters ／ 2，则前往分裂操作
    # Step6：若clusters > exp_clusters * 2，则前往合并操作
    # Step7：如果到达最大迭代次数则终止，否则返回Step2

    pass


# 合并操作
def merge():
    # Step1：计算当前聚类中心两两之间的距离，用矩阵D表示
    # Step2：合并，并计算新的聚类中心
    pass


# 分裂操作
def divide():
    # Step1：计算每个类别下，所有样本在每个维度下的方差sigma
    # Step2：得到sigma_max
    # Step3：分裂
    pass
