# R 零基础：第一次完整练习
# 先装 R，再装 RStudio。在脚本窗口逐行 Run。
# 不需要安装第三方包。不要复制控制台的 > 或 [1]。
2 + 3
x <- c(1, 2, 3)
y <- c(2, 4, 5)
length(x) # 数个数，结果 3
mean(x)   # 求平均数，结果 2
x[2]      # 取第二个数，结果 2
d <- data.frame(x=x, y=y)
names(d)  # 看列名
dim(d)    # 3 行、2 列
head(d)   # 看前几行
plot(d$x, d$y, xlab="x", ylab="y")
fit <- lm(y ~ x, data=d)
coef(fit) # 截距约 0.6667，斜率 1.5
abline(fit) # 在刚才的散点图上加回归线
summary(fit) # 后续结合 SE 与 t 检验单元阅读
predict(fit, newdata=data.frame(x=4)) # 约 6.6667，属于外推
# 熟悉以上流程后再练 CSV。去掉下一行前面的 # 才会运行：
# d <- read.csv(file.choose())
# 然后先检查 names(d)、dim(d)、head(d)、str(d)。
