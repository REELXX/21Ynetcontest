import json
import requests
import math
import time
import numpy as np
from django.shortcuts import render, redirect
from django.http import JsonResponse

requests.packages.urllib3.disable_warnings()
# if __name__ == "__main__":
# 获取token
url = "https://117.78.31.209:26335/rest/plat/smapp/v1/oauth/token"
headers = {
    "Content-Type": "application/json"
}
data = {
    "grantType": "password",
    "userName": "15659299492",
    "value": "zhenglinxinA100_"
}
response = requests.put(url, headers=headers, data=json.dumps(data), verify=False)
token = response.json()['accessSession']
print(token)

# 3.1智能评估体系
id_list = ['c94e9196-3686-4d4c-a7de-8117f581f63e', '9fc9253f-33a4-40db-8afc-825f383e54e8',
           '0504b1cb-e368-452c-8b43-2c8be81b3d14', '857b706e-67d9-49c0-b3cd-4bd1e6963c07']
test_inform = ['coverage', 'successCon', 'timeCon', 'throughput', 'capacity']
num = 0
eveg_are_inform = [[], [], [], []]
for i in id_list:
    url = ' https://117.78.31.209:26335/rest/campuswlanqualityservice/v1/expmonitor/overview/rate'
    param_0 = {"regionType": "site", "level": "0", "tenantId": "default-organization-id", "startTime": "1624053600000",
               "id": i, "endTime": "1624453200000"}
    header = {
        "X-Auth-Token": token,
        "Accept": "application/json;charset=UTF8",
        "Content-Type": "application/json",
    }
    res = requests.get(url, headers=header, params={'param': json.dumps(param_0)}, verify=False)
    #  print(res.json())
    res_inform = res.json()
    area_in = []
    for i in test_inform:
        area_in.append(res_inform['data']['values'][i])
    eveg_are_inform[num] = area_in
    num = num + 1


def rada(request):
    return JsonResponse({"inf1": [eveg_are_inform[0]], "inf2": [eveg_are_inform[1]], "inf3": [eveg_are_inform[2]],
                         "inf4": [eveg_are_inform[3]]})


# 3.2健康度趋势

trend_num = 0
trend_request_inform = ['coverage', 'rate', 'successCon', 'throughput', 'capacity']
rateall = [[], [], [], []]
coverageall = [[], [], [], []]
successConall = [[], [], [], []]
capacityall = [[], [], [], []]
throughputall = [[], [], [], []]
for i in id_list:
    url = ' https://117.78.31.209:26335/rest/campuswlanqualityservice/v1/expmonitor/rate/basictable?'
    param_0 = {"regionType": "site", "level": "0", "tenantId": "default-organization-id", "startTime": "1624053600000",
               "id": i, "endTime": "1624453200000"}
    header = {
        "X-Auth-Token": token,
        "Accept": "application/json;charset=UTF8",
        "Content-Type": "application/json",
    }
    res = requests.get(url, headers=header, params={'param': json.dumps(param_0)}, verify=False)

    res_inf = res.json()
    coverage_in = []
    rate_in = []
    successCon_in = []
    throughput_in = []
    capacity_in = []
    # print(res_inf['data'])
    # print(res_inf['data']['values'])
    # print(res_inf['data']['values'][2])

    for i in range(26):
        coverage_in.append(res_inf['data']['values'][i]['coverage'])
        rate_in.append(res_inf['data']['values'][i]['rate'])
        successCon_in.append(res_inf['data']['values'][i]['successCon'])
        throughput_in.append(res_inf['data']['values'][i]['throughput'])
        capacity_in.append(res_inf['data']['values'][i]['capacity'])

    rateall[trend_num] = rate_in
    coverageall[trend_num] = coverage_in
    successConall[trend_num] = successCon_in
    throughputall[trend_num] = throughput_in
    capacityall[trend_num] = capacity_in
    trend_num = trend_num + 1


def trendmap(request):
    return JsonResponse({"ratess": rateall, 'cover': coverageall, 'successcon': successConall, 'through': throughputall,
                         'capa': capacityall})


def monitor(request):
    return render(request, 'Home/monitor.html')


def other(request):
    return render(request, 'Home/other.html')


def satisfaction(request):
    return render(request, 'Home/satisfaction.html')


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
    print(C)
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
    list = [n1,n2,n3]
    n = len(list)
    for i in range(n):

        # Last i elements are already in place
        for j in range(0,n-i-1):

            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


satisF = main()


def manyidu(request):
    return JsonResponse({'STSF': satisF})

    # 热力图

    # 获取token
    # 拿到热力图


url = "https://117.78.31.209:26335/rest/campusrtlswebsite/v1/clientlocation/heatmap"
headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": token,
    "Accept": "application/json"
}
url = url + "?startTime=1624323600000&endTime=1624327200000"
res = requests.post(url, headers=headers, verify=False)
data = res.json()['data']

# 处理data
min_data = 10000
max_data = 0
for d in data:
    if min_data > d['count']:
        min_data = d['count']

    if max_data < d['count']:
        max_data = d['count']

error = max_data - min_data
res_data = []
for d in data:
    d['value'] = math.floor(d['count'] / error * 50)
    d.pop('count')


def heart_map(request):
    return JsonResponse({'sss': data})
