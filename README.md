# 中原银行个贷违约预测
## 赛题背景
```
为进一步促进金融普惠的推广落地，金融机构需要服务许多新的客群。
银行作为对风险控制要求很高的行业，因为缺乏对新客群的了解，
对新的细分客群的风控处理往往成为金融普惠的重要阻碍。如何利用银行现有
信贷行为数据来服务新场景、新客群成了一个很有价值的研究方向，
迁移学习是其中一个重要手段。
```
## 任务描述
```
本赛题要求利用已有的与目标客群稍有差异的另一批信贷数据，
辅助目标业务风控模型的创建，两者数据集之间存在大量相同的字段和极少的共同用户。
此处希望大家可以利用迁移学习捕捉不同业务中用户基本信息与违约行为之间的关联，
帮助实现对新业务的用户违约预测。
```
## 数据描述
- 训练数据
    - train_public.csv：个人贷款违约记录数据
    - ![image-20220426223359806](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220426223359806.png)
    - ![image-20220426223430897](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220426223430897.png)
    - train_internet_public.csv：某网络信用贷产品违约记录数据
    - ![image-20220426223503868](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220426223503868.png)
    - ![image-20220426223543059](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20220426223543059.png)
- 测试数据
    - test_public.csv：测试数据集

## 评价指标

使用ROC曲线下面积AUC（Area Under Curve）作为评价指标。AUC值越大，预测越准确。



