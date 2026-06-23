# 📊 数理统计期末复习资料
**上海财经大学 · 信息管理与工程学院 · 2026春季**
**主讲：袁洪松 | 整理：施婧**

---

## 📁 仓库结构

```
SUFE-notes-calculus/
├── README.md                              ← 本文件
├── DASHBOARD.md                           ← Markdown看板（章节进度、打卡清单）
├── dashboard.html                         ← 交互式HTML看板（可打卡，需GitHub Pages）
├── notes/
│   ├── 数理统计完整笔记.md                ← 第2-14讲全知识点（含公式、定理、速查表）
│   ├── 题型汇总与例题精讲.md              ← 13类题型 + 精选作业例题详解
│   └── 数理统计完整复习资料（原版）.html  ← 老师版原始复习资料（含MathJax公式）
├── exams/
│   ├── 数理统计_Spring26_期末样卷.pdf     ← 老师发布的原版样卷
│   ├── 模拟卷第1套.pdf                    ← 选择+填空+计算，接近真题水平
│   ├── 模拟卷第2套.pdf
│   ├── 模拟卷第3套.pdf
│   ├── 模拟卷第4套.pdf
│   └── 模拟卷第5套.pdf
└── solutions/
    ├── 数理统计_Spring26_期末样卷_解析.pdf ← 原版样卷参考解析
    ├── 模拟卷第1套_答案解析.pdf            ← 含知识点标注+解题思路+详细步骤
    ├── 模拟卷第2套_答案解析.pdf
    ├── 模拟卷第3套_答案解析.pdf
    ├── 模拟卷第4套_答案解析.pdf
    └── 模拟卷第5套_答案解析.pdf
```

---

## 📚 知识体系覆盖（第2-14讲）

| 章节 | 主题 | 重要程度 |
|------|------|---------|
| 第2讲 | 三大分布（χ², t, F）& 统计量 | ⭐⭐⭐ |
| 第3讲 | 学生定理 & 两总体抽样分布 | ⭐⭐⭐⭐⭐ |
| 第3-4讲 | 矩估计 & 极大似然估计（MLE） | ⭐⭐⭐⭐⭐ |
| 第4讲 | 无偏性、MSE、有效性 | ⭐⭐⭐⭐ |
| 第5讲 | 区间估计（枢轴量法） | ⭐⭐⭐⭐⭐ |
| 第6-7讲 | 假设检验（z/t/χ²/F + 成对数据 + 拟合优度） | ⭐⭐⭐⭐⭐ |
| 第8讲 | 单因素ANOVA & 线性回归 | ⭐⭐⭐⭐ |
| 第9讲 | Fisher信息量 & Rao-Cramer下界 | ⭐⭐⭐⭐⭐ |
| 第10-11讲 | 三大渐近检验（LRT/Wald/Score） | ⭐⭐⭐⭐ |
| 第12讲 | 充分统计量（因子分解定理） | ⭐⭐⭐⭐ |
| 第13讲 | 完备性 & Lehmann-Scheffe定理 | ⭐⭐⭐⭐⭐ |
| 第13-14讲 | 正则指数分布类 & CSS | ⭐⭐⭐⭐⭐ |
| 第14讲 | MVUE两种求法 | ⭐⭐⭐⭐⭐ |

---

## ⚠️ 高频失分点（10条必看）

**1. Fisher信息量忘乘 n**

$$n \text{ 个样本的Fisher信息量} = n \cdot I(\theta) \text{，不是 } I(\theta)$$

**2. LRT自由度搞错**

$$-2\log\Lambda \xrightarrow{D} \chi^2(q), \quad q = \text{约束个数，不是参数维数}$$

**3. 正态 MLE 有偏**

$$\hat{\sigma}^2_{\text{MLE}} = B_2 = \frac{1}{n}\sum(X_i-\bar{X})^2 \quad \text{（有偏，分母 } n \text{）}$$

$$S^2 = \frac{1}{n-1}\sum(X_i-\bar{X})^2 \quad \text{（无偏，分母 } n-1 \text{）}$$

**4. 完备性验证方向不可颠倒**

$$E_\theta[u(Z)] = 0 \text{ 对所有 } \theta \Rightarrow u \equiv 0 \quad \text{（方向不可反过来）}$$

**5. 均匀分布与正则指数族**

$$U[0,\theta] \text{ 支撑含 } \theta \Rightarrow \text{不属于正则指数族，但 } X_{(n)} \text{ 仍是CSS}$$

**6. t 分布对称性**

$$t_{1-\alpha}(n) = -t_{\alpha}(n)$$

**7. F 分布互倒（注意自由度互换）**

$$F_{1-\alpha}(n_1, n_2) = \frac{1}{F_{\alpha}(n_2, n_1)}$$

**8. 置信区间的正确理解**

$$\theta \text{ 是固定常数，} L \text{ 和 } U \text{ 是随机变量，不是 "}\theta\text{ 落在区间内的概率为 }1-\alpha\text{"}$$

**9. MSE 分解**

$$\text{MSE}(\hat{\theta}) = \text{Var}(\hat{\theta}) + \text{Bias}^2(\hat{\theta}) \quad \text{有偏估计的MSE可能比无偏更小}$$

**10. Wald 与 Score 检验分母不同**

$$\chi^2_W = \frac{n(\hat{\theta}-\theta_0)^2}{1/I(\hat{\theta})} \quad \text{（分母用 } \hat{\theta} \text{）}$$

$$\chi^2_R = \frac{[l'(\theta_0)]^2}{n \cdot I(\theta_0)} \quad \text{（分母用 } \theta_0 \text{）}$$

---

## 📝 试卷资料

| 文件 | 来源 | 说明 |
|------|------|------|
| 数理统计_Spring26_期末样卷.pdf | 老师发布 | 官方样卷，最接近真实考试风格 |
| 模拟卷第1套.pdf | 自制 | 重点：Gamma分布、两总体检验、三大渐近检验 |
| 模拟卷第2套.pdf | 自制 | 重点：Laplace分布、ANOVA、几何分布MVUE |
| 模拟卷第3套.pdf | 自制 | 重点：均匀分布CSS、N(μ₀,θ)有效性、Poisson R-B |

---

*Last updated: 2026年6月 | For academic use only*
