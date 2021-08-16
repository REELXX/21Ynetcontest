from django.shortcuts import render, redirect
from datetime import date
from aip import AipSpeech
import numpy as np
import pyaudio
import wave
import json

import requests
import re
# 语音播报模块
import pyttsx3
from django.http import JsonResponse
# aiff文件转换成mp3编码文件模块
from pydub import AudioSegment
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header

"""
注册，登录，注销
"""


def admin(request):

    return render(request, 'Home/intro.html')


def Sign(request):
    if request.method == 'POST':
        name = request.POST.get('accountSignIn')
        pwd = request.POST.get('passwordSignIn')
        print(name, pwd)
        # if request.POST.get('username') == CISCO123 and request.POST['password'] == CISCO123:
        if name == 'huawei' and pwd == 'huawei':
            return render(request, 'Home/overview.html')
    return render(request, 'Home/Sign_IN&UP.html')


# 返回
def overview(request):
    return render(request, 'Home/overview.html')


# def twoone(request):
#     return render(request, 'Home/2.1.html')

# Create your views here.


'''
语音输入模块
'''
APP_ID = "23721149"
API_KEY = "PVCVwFs9TO7CMHvWVw8oac9M"
SECRET_KEY = "GhKxkUGLhUTEieXeRZYgphgao0QQcKTL"

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
warn = [0]  # 0不用发告警邮件 1发告警邮件
user = [0]  # 1的时候跳转界面


def wav2pcm(wavfile, pcmfile, data_type=np.int16):
    f = open(wavfile, "rb")
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype=data_type)
    data.tofile(pcmfile)


def rec(file_name):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("开始录音,请说话......")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("录音结束！")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def json_send():  # 发送函数
    url = 'http://47.106.23.116:7788'  # 改为服务器Ip
    header = {
        'Content-Type': 'application/json; charset=utf-8'
    }
    requests.post(url, headers=header)


def voice_play(voice_str):
    content = voice_str
    try:
        # 输出文件格式
        outFile = 'out.aiff'

        print('准备开始语音播报...')

        # 设置要播报的Unicode字符串
        engine.say(content)

        # 等待语音播报完毕
        engine.runAndWait()

        # 将文字输出为 aiff 格式的文件
        # engine.save_to_file(content, outFile)

        # 将文件转换为mp3格式
        # AudioSegment.from_file(outFile).export("Python.mp3", format="mp3")
    except Exception:
        print("出现错误")


def voice_recognition(voice_file):  # 语音识别
    keyword_warm = '检测'
    keyword_user = '用户'

    # text_txt = json.loads(voice_file)

    # ----检测字符串中是否 有 检测  等关键词--------------------------
    if keyword_warm in voice_file:
        print('开始检测')
        # s = re.findall("\d+", voice_file)
        warn[0] = 1
    if keyword_user in voice_file:
        user[0] = 1
        print(user)
        print('跳转页面')


# json_send //发送至服务器
# json_send()
engine = pyttsx3.init()


# def touserlist(request):
#     # 跳转用户界面
#     return render(request, 'Home/userlist.html')


def voice_detect(request):
    rec("1.wav")

    wav2pcm("1.wav", "1.pcm")

    with open("1.pcm", 'rb') as fp:
        file_context = fp.read()

    res = client.asr(file_context, 'pcm', 16000, {
        'dev_pid': 1537,
    })

    print(res['result'][0])  # 提取字典中 result 后信息
    res_str = res["result"][0]
    # print(user)
    voice_recognition(res_str)  # 数据处理
    # 跳转到用户界面
    # if user[0] == 1:
    #     user[0] = 0
    #     print("开始跳转页面")
    #     return redirect('/touserlist')
    color = 'greenyellow'
    if warn[0] == 1:
        warning()
        warn[0] = 0
    # print(user)
    return JsonResponse({'voice_detect': res_str, 'color': color})


# voice_detect(requests)  # 测试语音服务

'''
语音输入模块结束
'''

'''
邮箱告警模块
'''


def send_email(SMTP_host, from_addr, password, to_addrs, subject, content):
    """
    port = 587
    在登陆邮箱前加上email_client.starttls()这句话
    """
    email_client = SMTP(SMTP_host, 587)
    email_client.starttls()
    email_client.login(from_addr, password)

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_addr
    msg['to'] = ''.join(to_addrs)
    email_client.sendmail(from_addr, to_addrs, msg.as_string())

    email_client.quit()


def warning():
    # qq发送qq

    receiver = ["943996316@qq.com"]
    send_email("smtp.qq.com", "943996316@qq.com", "wbzsqseidgoibcgb", receiver, "异常告警", "发现深圳站点出现流量异常")
