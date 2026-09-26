# -*- coding: utf-8 -*-
# 全课程 14 个微型实验。依赖: numpy。

print("\n===== 第 1 章：看数据的维数与散布 =====")
import numpy as np
rng = np.random.default_rng(7)
X = rng.normal(size=(20, 100))
print("样本、特征:", X.shape, "矩阵秩:", np.linalg.matrix_rank(X))
print("第一列均值和样本方差:", X[:,0].mean(), X[:,0].var(ddof=1))
# 改成 (100,20)，再解释为什么秩的上界改变。

print("\n===== 第 2 章：手算与最小二乘核对 =====")
import numpy as np
x = np.array([0,1,2,3,4.])
y = np.array([1,2,2,4,6.])
X = np.column_stack([np.ones(len(x)), x])
b = np.linalg.lstsq(X,y,rcond=None)[0]
e = y-X@b
print("截距、斜率:", b, "RSS:", e@e, "残差和:", e.sum())
assert np.allclose(b,[.6,1.2])
# 加大一个 y，先预测斜率会怎样变化，再重跑。

print("\n===== 第 3 章：共线性、标准误与预测 =====")
import numpy as np
rng=np.random.default_rng(7)
x=rng.normal(size=40)
x2=x+.03*rng.normal(size=40)
X=np.column_stack([np.ones(40),x,x2])
y=1+2*x+rng.normal(scale=.3,size=40)
b=np.linalg.lstsq(X,y,rcond=None)[0]
e=y-X@b
s2=e@e/(40-X.shape[1])
cov=s2*np.linalg.inv(X.T@X)
print("系数:",b,"标准误:",np.sqrt(np.diag(cov)))
print("两个斜率之和:",b[1]+b[2])
# 把 .03 改成 .3，比一比单个斜率的稳定性。

print("\n===== 第 4 章：生成多项式设计列 =====")
import numpy as np
x=np.array([-2,-1,0,1,2.])
X=np.column_stack([np.ones(5),x,x*x])
y=1+2*x-x*x
b=np.linalg.lstsq(X,y,rcond=None)[0]
print("设计矩阵:\n",X,"\n系数:",b)
assert np.allclose(b,[1,2,-1])
# 曲线对 x 非线性，却对 b 线性。先解释再运行。

print("\n===== 第 5 章：验证选择复杂度 =====")
import numpy as np
rng=np.random.default_rng(7)
x=np.linspace(-1,1,24); y=np.sin(3*x)+rng.normal(0,.2,24)
train=np.arange(24)%3!=0; valid=~train
for degree in [1,3,8]:
    X=np.vander(x,degree+1,increasing=True)
    b=np.linalg.lstsq(X[train],y[train],rcond=None)[0]
    print(degree,"训练MSE",np.mean((y[train]-X[train]@b)**2),
          "验证MSE",np.mean((y[valid]-X[valid]@b)**2))
# 这是一次验证划分，不是最终无偏的模型性能报告。

print("\n===== 第 6 章：高维 Ridge 与 Lasso 的小实验 =====")
import numpy as np
rng=np.random.default_rng(7)
X=rng.normal(size=(100,200)); beta=np.r_[np.ones(5),np.zeros(195)]
y=X@beta+rng.normal(size=100)
A=X[:70]; B=X[70:]; ya=y[:70]; yb=y[70:]
mu=A.mean(0); scale=A.std(0); A=(A-mu)/scale; B=(B-mu)/scale
mean_y=ya.mean(); yc=ya-mean_y
# Ridge: ||y-Xb||²/(2n)+lam*||b||²/2
lam=.1; n=len(ya)
br=np.linalg.solve(A.T@A/n+lam*np.eye(200),A.T@yc/n)
# Lasso: 同一损失尺度 + lam*||b||1，近端梯度
step=1/(np.linalg.norm(A,2)**2/n); bl=np.zeros(200)
for _ in range(3000):
    z=bl-step*(A.T@(A@bl-yc)/n)
    new=np.sign(z)*np.maximum(np.abs(z)-step*lam,0)
    if np.linalg.norm(new-bl)<1e-7: bl=new; break
    bl=new
for name,b in [("Ridge",br),("Lasso",bl)]:
    print(name,"测试MSE",np.mean((yb-mean_y-B@b)**2),"非零",np.sum(abs(b)>1e-6))
# 同样数值 lam 不等于两种方法具有同等有效复杂度；正式比较需分别调参。

print("\n===== 第 7 章：Logistic 概率与优势比 =====")
import numpy as np
x=np.array([-2,-1,0,1,2.]); intercept=0.; slope=np.log(2)
eta=intercept+slope*x; p=1/(1+np.exp(-eta))
print("x:",x,"概率:",p,"odds:",p/(1-p))
print("相邻odds比:",(p[1:]/(1-p[1:]))/(p[:-1]/(1-p[:-1])))
# 每增加1，odds乘2，但概率不一定增加一倍。

print("\n===== 第 8 章：阈值怎样改变错误类型 =====")
import numpy as np
p=np.array([.05,.12,.2,.32,.42,.55,.65,.75,.85,.95])
y=np.array([0,0,1,0,1,0,1,1,0,1])
for t in [.2,.5,.8]:
    pred=p>=t; tp=np.sum(pred&(y==1)); fp=np.sum(pred&(y==0)); fn=np.sum(~pred&(y==1))
    print(t,"TP FP FN",tp,fp,fn,"precision",tp/(tp+fp),"recall",tp/(tp+fn))
# 先写下漏报与误报的代价，再决定目标指标。

print("\n===== 第 9 章：PCA 的载荷、得分和重建 =====")
import numpy as np
X=np.array([[-3,-2],[-2,-.6],[-.5,-1],[1,.8],[2,1.6],[3,1.2]])
mean=X.mean(0); Xc=X-mean
U,s,Vt=np.linalg.svd(Xc,full_matrices=False)
load=Vt[0]; scores=Xc@load; reconstruction=np.outer(scores,load)
print("载荷:",load,"得分:",scores)
print("首方向方差比例:",s[0]**2/(s@s))
print("重建平方误差:",np.sum((Xc-reconstruction)**2),"丢掉奇异值平方:",s[1]**2)
# 整个载荷向量改成负号，重建会改变吗？

print("\n===== 第 10 章：三节点图的拉普拉斯 =====")
import numpy as np
A=np.array([[0,1,0],[1,0,1],[0,1,0.]])
L=np.diag(A.sum(1))-A
values,vectors=np.linalg.eigh(L)
print("L:\n",L,"\n特征值:",values)
assert np.allclose(L@np.ones(3),0)
# 删掉 (2,3) 那条边，再看零特征值的个数。

print("\n===== 第 11 章：低秩矩阵的重建误差 =====")
import numpy as np
M=np.diag([5.,3.,1.]); U,s,Vt=np.linalg.svd(M,full_matrices=False)
for r in [1,2,3]:
    R=(U[:,:r]*s[:r])@Vt[:r]
    err=np.sum((M-R)**2)
    print("秩",r,"平方误差",err,"理论",sum(s[r:]**2))
    assert np.isclose(err,sum(s[r:]**2))
# 这是完整观测的近似，不是把缺失矩阵直接填0的依据。

print("\n===== 第 12 章：一次注意力与一次高斯更新 =====")
import numpy as np
scores=np.array([0.,1.]); weights=np.exp(scores-scores.max()); weights/=weights.sum()
print("注意力权重:",weights,"输出:",weights@np.array([2.,6.]))
K=np.array([[1.]]); noise=1.; y=np.array([2.]); kstar=np.array([.5])
mean=kstar@np.linalg.solve(K+noise*np.eye(1),y)
var=1-kstar@np.linalg.solve(K+noise*np.eye(1),kstar)
print("GP潜在均值/方差:",mean,var)
# 新观测方差还要加噪声；这里没有训练任何大型模型。

print("\n===== 第 13 章：最小范数插值与梯度下降 =====")
import numpy as np
X=np.array([[1.,1.]]); y=np.array([2.])
bmin=X.T@np.linalg.solve(X@X.T,y)
b=np.zeros(2)
for _ in range(100): b-=.25*(X.T@(X@b-y))
print("公式:",bmin,"零初始化GD:",b)
assert np.allclose(b,bmin)
# 改成非零初始化，观察零空间分量会不会保留。

print("\n===== 第 14 章：LoRA：实际构造一个更新 =====")
import numpy as np
rng=np.random.default_rng(7); d=k=64; r=2
A=rng.normal(size=(r,k)); B=rng.normal(size=(d,r)); delta=B@A
print("A/B/BA形状:",A.shape,B.shape,delta.shape)
print("更新秩:",np.linalg.matrix_rank(delta),"因子参数:",A.size+B.size,"完整参数:",d*k)
assert np.linalg.matrix_rank(delta)<=r
# 注意BA通常每个元素都非零：低秩不等于稀疏。