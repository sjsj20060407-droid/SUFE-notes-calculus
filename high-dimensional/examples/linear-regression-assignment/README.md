# 线性回归作业复现实例

这个实例展示两组数据的回归建模、相关性、共线性诊断和图表生成，可配合高维数据分析工作台的回归单元学习。运行 `homework_code.py` 后，计算表和图表写入 `results/`；仓库内保留了一次运行的结果，便于对照。

```bash
python -m pip install -r requirements.txt
python homework_code.py
```

`Boston.csv` 保留课程作业提供的列名 `NX`。`water.csv` 由 CRAN `alr4` 包的 `water.rda` 转换，来源与获取日期见 [原使用说明](使用说明.txt)。两份数据是教学复现资料；使用或再发布时请核对原始来源及适用许可。

本目录是练习代码与数据，不代替正式作业提交。计算方法和结果应结合原题要求核查。
