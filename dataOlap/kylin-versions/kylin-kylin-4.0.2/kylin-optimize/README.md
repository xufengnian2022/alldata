# Kylin optimization iteration

## 1、维度裁剪

## 2、模型设计

## 3、资源适配

## 4、优化

> 4.1 原理解读
> 
> 解读了Kylin构建原理，包含了预计算思想以及By-layer逐层算法
> 根据维度组合出所有可能的维度，对多维分析可能用到的指标进行预计算，将计算好的结果保存成Cube。假设我们有4个维度，
> 这个Cube中每个节点（称作Cuboid）都是这4个维度的不同组合，每个组合定义了一组分析的维度（如group by），
> 指标的聚合结果就保存在每个Cuboid上。查询时，我们根据SQL找到对应的Cuboid，读取指标的值，即可返回
> 
> 4.2 过程拆解
> 
> 4.3 实施路线
> 
> 引擎选择 数据读取 构建字典 分层构建 文件转换