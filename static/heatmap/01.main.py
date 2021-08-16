from flask import Flask
import requests
import json
import math
from flask_cors import *
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/heartmap')
@cross_origin(supports_credentials=True)
def heart_map():
    #获取token
    url = "https://117.78.31.209:26335/rest/plat/smapp/v1/oauth/token"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "grantType": "password",
        "userName": "18960126262",
        "value": "huawei12#$"
    }
    response = requests.put(url, headers=headers, data=json.dumps(data), verify=False)
    token = response.json()['accessSession']
    print(token)
    # 拿到热力图
    url = "https://117.78.31.209:26335/rest/campusrtlswebsite/v1/clientlocation/heatmap"
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": token,
        "Accept": "application/json"
    }
    url = url+"?startTime=1624323600000&endTime=1624327200000"
    res = requests.post(url, headers=headers, verify=False)
    data = res.json()['data']
    print(data)

    # 处理data
    min_data = 10000
    max_data = 0
    for d in data:
        if min_data > d['count']:
            min_data = d['count']

        if max_data < d['count']:
            max_data = d['count']

    print(min_data, max_data)
    error = max_data - min_data
    res_data = []
    for d in data:
        d['value'] = math.floor(d['count'] / error * 40)
        d['x'] = d['x']*0.37
        d['y'] = d['y']*0.37
        d.pop('count')

    print(data)
    return json.dumps(data)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8899", debug=True)