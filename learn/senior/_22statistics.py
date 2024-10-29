# !/usr/local/bin/python3.12
# Python statistics 模块
# Python statistics 是标准库中的一个模块，模块提供了许多基本统计计算的函数。
# statistics 模块是在 Python 3.4 版本中新增加的，可以帮助我们分析和计算数据集的统计特征。
# 要使用 statistics 函数必须先导入：
# import statistics
# 查看 statistics 模块中的内容:
import statistics

print(dir(statistics))

# statistics 模块方法
# 方法	                        描述
# statistics.harmonic_mean()	计算给定数据集的调和平均值。
# statistics.mean()	            计算数据集的平均值
# statistics.median()	        计算数据集的中位数
# statistics.median_grouped()	计算给定分组数据集的分组中位数
# statistics.median_high()	    计算给定数据集的高位中位数
# statistics.median_low()	    计算给定数据集的低位中位数。
# statistics.mode()	            算数据集的众数（出现频率最高的值）
# statistics.pstdev()	        计算给定数据集的样本标准偏差
# statistics.stdev()	        计算数据集的标准差
# statistics.pvariance()	    计算给定数据集的样本方差
# statistics.variance()	        计算数据集的方差
# statistics.quantiles()	    计算数据集的分位数，可指定分位数的数量（默认为四分位数）
