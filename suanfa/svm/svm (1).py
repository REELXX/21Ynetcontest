#网络链接状态稳定性
import numpy as np
import random

def loadDataSet(fileName):      #得到数据集的数据
    dataMat,labelMat = [],[]
    fr = open(fileName)
    for line in fr.readlines():
        lineArray = line.strip().split(' ')
        dataMat.append([float(lineArray[0]), float(lineArray[1])])  # 添加数据
        labelMat.append(float(lineArray[2]))
    return  dataMat,labelMat

def selectalpha(i,m):     #随机选择alpha
    j = i
    while(j == i):
        j = int(random.uniform(0, m))
        return j

def clipAlpha(aj,H,L):   #修剪alpha的值根据范围
    if aj>H:
        aj = H
    if aj<L:
        aj = L
    return aj

#简单的smo算法
def smoSimple(dataMatIn, classLabels, C, toler, maxIter):    #传入两个数据集，c，松驰项,最大迭代数
    # 转换为numpy的mat存储
    data = np.mat(dataMatIn)
    label = np.mat(classLabels).transpose()
    # 初始化b参数，统计data的维度
    b = 0; m,n = np.shape(data)
    #初始化alphas令其为零
    alphas = np.mat(np.zeros((m,1)))
    inter_num = 0
    while(inter_num <=maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            #计算误差Ei
            fi = float(np.multiply(alphas,label).T*(data * data[i,:].T)) + b
            Ei = fi - float(label[i])

            if ((label[i]*Ei < -toler) and (alphas[i] < C)) or ((label[i]*Ei > toler) and (alphas[i] > 0)):
                #随机选择另一个与alpha_i成对优化的alpha_j
                j = selectalpha(i,m)
                # 计算误差Ei
                fj = float(np.multiply(alphas,label).T*(data * data[j,:].T)) + b
                Ej = fj - float(label[j])
                # 保存更新前的aplpha值，使用深拷贝
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                #计算上下界L和H
                if label[i] != label[j]:
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H:
                    continue
                #计算eta
                eta = 2.0 * data[i,:] * data[j,:].T - data[i,:] * data[i,:].T - data[j,:] * data[j,:].T
                if eta >= 0: continue
                #更新aj
                alphas[j] -= label[j]*(Ei - Ej)/eta
                #根据取值范围修剪αj
                alphas[j] = clipAlpha(alphas[j], H, L)
                if (abs(alphas[j] - alphaJold) < 0.00001):continue
                #更新aj
                alphas[i] += label[i]*label[j]*(alphaJold - alphas[j])
                #更新b1和b2
                b1 = b - Ei - label[i]*(alphas[i]-alphaIold)*data[i,:]*data[i,:].T - label[j]*(alphas[j]-alphaJold)*data[i,:]*data[j,:].T
                b2 = b - Ej - label[i]*(alphas[i]-alphaIold)*data[i,:]*data[j,:].T - label[j]*(alphas[j]-alphaJold)*data[j,:]*data[j,:].T
                #根据b1和b2更新b
                if 0<alphas[i] and alphas[i]<C:
                    b = b1
                elif 0<alphas[j] and alphas[j]<C:
                    b = b2
                else:
                    b = (b1+b2)/2.0
                alphaPairsChanged += 1
        if(alphaPairsChanged == 0):
            inter_num += 1
    return  b,alphas

def get_w(dataMat, labelMat, alphas):
    alphas, dataMat, labelMat = np.array(alphas), np.array(dataMat), np.array(labelMat)
    w = np.dot((np.tile(labelMat.reshape(1, -1).T, (1, 2)) * dataMat).T, alphas)
    return w

def main():
    dataMat,labelMat = loadDataSet('testSet.txt')   #提取数据集
    b,aplphas =  smoSimple(dataMat, labelMat, 0.6, 0.001, 40)
    W = get_w(dataMat,labelMat,aplphas)

    data = []#时延,链路质量
    if W.T*data +b >=0:
        fl = 1
    else: fl = -1
    print(fl)
if __name__ == '__main__':
    main()