### 学院：计算机学院&emsp;学号：3220190894&emsp;姓名：吴嘉豪
# 互评作业2: 频繁模式与关联规则挖掘
**数据分析要求：**  
-对数据集进行处理，转换成适合进行关联规则挖掘的形式；  
-找出频繁模式；  
-导出关联规则，计算其支持度和置信度;  
-对规则进行评价，可使用Lift、卡方和其它教材中提及的指标, 至少2种；  
-对挖掘结果进行分析；  
-可视化展示。  

------------

**使用的Dataset：**
- [Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews "Wine Reviews")

------------

**使用的环境：**
'''python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules
from mlxtend.plotting import stacked_barplot,scatterplotmatrix
'''

------------

**仓库文件介绍：**
- **分析过程报告**：Wine Reviews.html，Consumer & Visitor Insights For Neighborhoods.html分别为两个数据集的分析过程报告
- **程序**：
	- Wine Reviews.ipynb，Wine Reviews.py为第一个数据集的程序；
	- Consumer & Visitor Insights For Neighborhoods.ipynb，Consumer & Visitor Insights For Neighborhoods.py为第二个数据集的程序；
	- .ipynb后缀的是使用 Jupyter Notebook 来编写Python程序时的文件；
	- .py后缀的是源代码文件。


