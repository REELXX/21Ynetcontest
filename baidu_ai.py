'''
Author: your name
Date: 2021-02-28 21:40:45
LastEditTime: 2021-04-27 22:24:50
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python02\.vscode\baidu_ai.py
'''
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

# aiff文件转换成mp3编码文件模块
from pydub import AudioSegment

# 这里的三个参数,对应在百度语音创建的应用中的三个参数
APP_ID = "23721149"
API_KEY = "PVCVwFs9TO7CMHvWVw8oac9M"
SECRET_KEY = "GhKxkUGLhUTEieXeRZYgphgao0QQcKTL"

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 协议  | 高压 | 低压 | 血糖 | 体温 | 预留1 |预留2  | 校验位 |

physical_information = [0 for x in range(0, 8)]
physical_information[0] = 0xAA
physical_information[1] = 0x55

send_information = {'blood_presure_high': 0, 'blood_presure_low': 0, 'blood_glucose': 0, 'body_temperature': 0,
                    'address': 0, 'sphygmus': 0}

# pyrec 参数
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5


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
    data = json.dumps(physical_information)
    physical_information[7] = 0
    header = {
        'Content-Type': 'application/json; charset=utf-8'
    }
    requests.post(url, data=data, headers=header)


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
    keyword_bloode_pressure = ['血压', '高压', '低压']
    keyword_bloode_glucose = '血糖'
    keyword_temper = '检测'
    keyword_sphygmus = '脉搏'
    # text_txt = json.loads(voice_file)

    # ----检测字符串中是否 有 血压 高压 低压  等关键词--------------------------
    for i in keyword_bloode_pressure:
        if i in voice_file:  # 判断出 血 字 标志位 为1
            print("识别到", i)
            s = re.findall("\d+", voice_file)
            pressure_flag = 1

    # ----检测字符串中是否 有 血糖  等关键词--------------------------
    if keyword_bloode_glucose in voice_file:  # 判断出 血 字 标志位 为1
        print('开始检测')
        s = re.findall("\d+", voice_file)
        glucos_flag = 1

    # ----检测字符串中是否 有 体温  等关键词--------------------------
    if keyword_temper in voice_file:  # 判断出 血 字 标志位 为1
        print('开始检测')
        s = re.findall("\d+", voice_file)
        temper_flag = 1
    # ----检测字符串中是否 有 脉搏  等关键词--------------------------
    if keyword_sphygmus in voice_file:  # 判断出 血 字 标志位 为1
        s = re.findall("\d+", voice_file)
        sphygmus_flag = 1
    #  血压赋值



engine = pyttsx3.init()

rec("1.wav")

wav2pcm("1.wav", "1.pcm")

with open("1.pcm", 'rb') as fp:
    file_context = fp.read()

res = client.asr(file_context, 'pcm', 16000, {
    'dev_pid': 1537,
})

print(res['result'][0])  # 提取字典中 result 后信息
res_str = res["result"][0]

voice_recognition(res_str)  # 数据处理
print(send_information)

# json_send //发送至服务器
# json_send()
