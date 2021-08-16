import json
import requests
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

# 查询用户列表
url = "https://117.78.31.209:26335/rest/campusclientservice/v1/event/userlist"
data = {
    "regionType": "site", "level": "1", "tenantId": "default-organization-id", "startTime": "1624202262000",
    "id": "857b706e-67d9-49c0-b3cd-4bd1e6963c07",
    "endTime": "1624461462433",
    "sortColumn": "totalcount",
    "currPage": "1",
    "pageSize": "100",
    "sortType": "desc"
}
header = {
    "X-Auth-Token": token,
    "Accept": "application/json;charset=UTF8",
    "Content-Type": "application/json",
}
res = requests.post(url, headers=header, data=json.dumps(data), verify=False)
# print(res.json())
people_dir = res.json()
# 修改用户列表中的时间戳和用户名
a = 1
for i in people_dir['data']['tableData']:
    # 时间戳处理
    timestamp = float(i['accTime']) / 1000
    Etimestamp = float(i['minAccTime']) / 1000
    timeArray = time.localtime(timestamp)
    EtimeArray = time.localtime(Etimestamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    EotherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", EtimeArray)
    i['accTime'] = otherStyleTime
    i['minAccTime'] = EotherStyleTime
    # 用户名处理
    i['userName'] = 'User' + str(a)
    a = a + 1

    # new_starttime_list.append(otherStyleTime)
    # new_endtime_list.append(EotherStyleTime)
# print(people_dir['data']['tableData'])
"""    接入AP信息提取完成   """

url = "https://117.78.31.209:26335/rest/campusclientservice/v1/protocoltrace/sessionlist"
data = {
    "intervals": "[2020-08-27T16:00:00.000Z/2020-08-28T06:52:21.000Z]",
    "level": "0",
    "tenantId": "default-organization-id",
    "id": "/",
    "accType": "1",
    "usermac": "30-00-00-00-00-22"
}
header = {
    "X-Auth-Token": token,
    "Accept": "application/json",
    "Content-Type": "application/json"
}
# 数据
res = requests.post(url, headers=header, data=json.dumps(data), verify=False)
# 字典化
res_dict = res.json()


# 接入AP数据 获取到了列表数据
# print(res_dict["resultData"])


def APinformation(request):
    return JsonResponse({"infom": res_dict["resultData"]})


def UserListServlet(request):
    if request.method == 'POST':
        tenantId = request.POST.get('tenantId')
        id = request.POST.get('id')
        startTime = request.POST.get('startTime')
        endTime = request.POST.get('endTime')
    # 时间戳转换现实时间

    totalsize = people_dir['data']['totalSize']
    pagesize = people_dir['data']['pageSize']
    # print(totalsize, pagesize)
    return JsonResponse({
        "tenantId": tenantId,
        "id": id,
        "startTime": startTime,
        "totalSize": totalsize,
        "pageSize": pagesize,
        "tableData": people_dir["data"]["tableData"],
    })


""""""
# 2.4 用户趋势
url = 'https://117.78.31.209:26335/rest/campusclientservice/v1/clientoverview/userstatistics/trend? '
param = {"regionType": "site", "level": "1", "tenantId": "default-organization-id", "showType": "radio",
         "startTime": "1624053600000", "id": "857b706e-67d9-49c0-b3cd-4bd1e6963c07", "endTime": "1624453200000",
         "isAutoRefresh": "false"}
header = {
    "X-Auth-Token": token,
    "Accept": "application/json;charset=UTF8",
    "Content-Type": "application/json",
}
res1 = requests.get(url, headers=header, params={'param': json.dumps(param)}, verify=False)


# print(res1.json())


# AP_res = res_dict['resultData']
# # print(type(AP_res), AP_res)
# # print(type(res.text),res.text)
# # print(type(res.json()),res.json())
# accessAP = []
# accessAPmac = []
# ssid = []
# # 让每种数据都组成专门的列表 再从列表里一个一个拿 综合成 AP_Info
# for i in AP_res:
#     print(i['accessAp'], i['accessApMac'])
#     accessAP.append(i['accessAp'])
#     accessAPmac.append(i['accessApMac'])
#     ssid.append(i['ssid'])
# # 这样每台AP的数据就能放一起了
# AP_Info = []
# for i in range(len(accessAPmac)):
#     AP_Info.append([])
#     AP_Info[i].append(accessAP[i])
#     AP_Info[i].append(accessAPmac[i])
#     AP_Info[i].append(ssid[i])
# print(np.array(AP_Info))
# print(type(AP_Info))
# for a in AP_Info:
#     print(a)
#     for i in a:
#         print(i)
# print(a)

def errorDetect(request):
    return render(request, 'Home/errorDetect.html')


def userlist(request):
    return render(request, 'Home/userlist.html')
