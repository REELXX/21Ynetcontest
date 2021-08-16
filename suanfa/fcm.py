import numpy as np
import matplotlib.pyplot as plt


# 求隶属度
def fcm_u(c, n, data, m):
    u = np.array([[float(0) for i in range(n)] for j in range(c)])
    for i in range(c):
        for j in range(n):
            sum = 0
            for k in range(c):
                temp = (np.linalg.norm(data[j, :] - c_new[i, :]) / np.linalg.norm(data[j, :] - c_new[k, :])) ** (
                        2.0 / (m - 1))
                sum += temp
            u[i][j] = float(1.0 / sum)
    u = np.array(u)
    return u


# 求聚类中心
def fcm_c(c, u, m, n, data):
    c_new = []
    for i in range(c):
        sum0 = np.sum(np.power(u[i], m))
        ci = 0
        for j in range(n):
            sum = data[j] * (u[i][j] ** m / sum0)
            ci += sum
        ci = ci.tolist()
        c_new.append(ci)
    c = len(c_new)
    c_new = np.array(c_new)
    return c_new, c


def fcm(inter, n, m, data, C):  # inter:迭代次数 n:样本数  m:一般为2  data：数据集  c:类数
    global c_new
    data = np.array(data)
    # 初始化隶属度
    u = []
    for i in range(n):
        uij = np.random.dirichlet(np.ones(C), size=1)  #
        uij.tolist()
        num = uij[0]
        u.append(num)
    u = np.array(u)
    c = len(u[0])
    u = u.T
    for t in range(inter):
        # 求聚类中心Ci
        c_new, c = fcm_c(c, u, m, n, data)
        # 求隶属度uij
        u = fcm_u(c, n, data, m)
    return u, c_new


def loadDataSet(fileName):  # 得到数据集的数据
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArray = line.strip().split('\t')
        dataMat.append(
            [float(lineArray[0]), float(lineArray[1]), float(lineArray[2]), float(lineArray[3]), float(lineArray[4]),
             float(lineArray[5])])  # 添加数据
    return dataMat


# 主函数
def main():
    # 生成高斯分布的随机点
    means1 = [-72.3043478260869, 147.739130434782, 509.826086956521, 2755.65217391304, 16.8695652173913,
              3.72255980730278]
    cov1 = np.eye(6) * 2
    means2 = [-76.9545454545454, 168.818181818181, 503.454545454545, 2363.63636363636, 18.5000000000000,
              3.17694369973190]
    cov2 = np.eye(6) * 2
    means3 = [-76.9545454545454, 168.818181818181, 503.454545454545, 2363.63636363636, 18.5000000000000,
              3.17694369973190]
    cov3 = np.eye(6) * 2
    data1 = np.random.multivariate_normal(means1, cov1, 100)
    data2 = np.random.multivariate_normal(means2, cov2, 100)
    data3 = np.random.multivariate_normal(means3, cov3, 100)
    data = data1 + data2 + data3
    U, C = fcm(100, len(data), 2, data, 3)  # inter:迭代次数 n:样本数  m:一般为2  data：数据集  c:类数
    U = U.T
    Dis = []
    num = 0;
    n1 = 0;
    n2 = 0;
    n3 = 0
    for i in data:
        dis = []
        for j in C:
            dis.append(((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 + (i[2] - j[2]) ** 2 + (i[3] - j[3]) ** 2 + (
                    i[4] - j[4]) ** 2 + (i[5] - j[5]) ** 2) ** 0.5)
        Dis.append(dis)
    for i in range(len(Dis)):
        if Dis[i][0] < Dis[i][1] and Dis[i][0] < Dis[i][2]:
            n1 = n1 + 1
        elif Dis[i][1] < Dis[i][0] and Dis[i][1] < Dis[i][2]:
            n2 = n2 + 1
        elif Dis[i][2] < Dis[i][0] and Dis[i][2] < Dis[i][1]:
            n3 = n3 + 1
    return n1,n2,n3



x = main()
y = list(x)
print(y,type(y))

if __name__ == '__main__':
    main()
