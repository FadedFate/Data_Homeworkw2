### 学院：计算机学院&emsp;学号：3220190894&emsp;姓名：吴嘉豪
# 互评作业2: 频繁模式与关联规则挖掘
**数据分析要求：**  
	- 对数据集进行处理，转换成适合进行关联规则挖掘的形式；  
	- 找出频繁模式；  
	- 导出关联规则，计算其支持度和置信度;  
	- 对规则进行评价，可使用Lift、卡方和其它教材中提及的指标, 至少2种；  
	- 对挖掘结果进行分析；  
	- 可视化展示。  

------------

**使用的Dataset：**
- [Wine Reviews](https://www.kaggle.com/zynicide/wine-reviews "Wine Reviews")

------------

**使用的环境：**
对于.ipynb文件(直接使用mlxtend库)，需要引用：  
```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules
from mlxtend.plotting import stacked_barplot,scatterplotmatrix
```

对于.py文件(频繁项集挖掘---Apriori算法)，需要引用：  
```python
import pandas as pd
import numpy as np
import itertools
import json
```
------------

**仓库文件介绍：**  
- **分析过程报告**
	- __homeworkw2.html__: 对应使用mlxtend库函数完成的频繁项集与关联规则挖掘的报告，更加简洁与方便.  
- **程序**：  
	- __homeworkw2.ipynb__: 处理Wine Review对应数据集对应notebook代码(使用mlxtend库函数).  
	- __WineR_Apriori.py__: 频繁项集挖掘程序(未使用mlxtend库函数).  
	- __wine_review_w2.json__: WineR_Apriori.py中min_support = 0.0772的结果，对应与ipynb文件中mlxtend的执行结果(一致).


