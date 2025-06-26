import easygui as eg
import pyautogui
import random
import time
import tqdm
import json
import sys, os

sfp = open(r"./setting.json", 'r')  # 打开设置文件
setting = json.load(sfp)  # 加载设置文件

COUNT = PAUSE = None

try:  # 尝试做以下事，遇到错误执行except里面的内容：

    COUNT = int(setting["count"])  # 读取刷屏次数
    PAUSE = 1 / (float(setting["speed"]))  # 读取速度，转换成停顿时长
except KeyError as e:  # 遇到错误，将错误信息存到“e”里面
    raise
    # eg.msgbox(  # 弹出弹窗，提示错误
    #     "设置出错啦！请不要乱动设置文件哦！您可以重置设置文件 重置网址：http://mtw.so/6dg2Tb",
    #     title=f"{e}")
    # print("出现错误，将使用默认设置")  # 退出程序
    # COUNT = 50
    # PAUSE = 1 / (20 * 2)

print("请在3秒内将光标聚焦（点击）在要输入的文本框上.刷屏间隔：", PAUSE)  # 输出提示信息

time.sleep(3)  # 等待3秒

# 开始刷屏：
for i in tqdm.trange(  # 创建进度条，并创建循环：
        COUNT,         # 循环上文的“次数”次，
        ascii=' =',    # 用等于号填充进度条，
        colour='blue',  # 蓝色的等于号，
        unit='pcs',    # 以“pcs”为单位，
        unit_scale=True):  # 附加设置，
    # 循环做以下事情COUNT次：
    # x = random.randint(1, 3)  # 随机选择本次消息发送多少个字符（仿真人），
    # pyautogui.PAUSE = PAUSE / x  # 根据本行内容多少设定合适的速度，
    # for j in range(x):  # 循环<选择的字符数>次做以下事：
    #     # 每次从这些字符随机选择一个（仿真人）并输入。
    #     pyautogui.press(random.choice(["t", '3', '4', 's', 'b']));
    pyautogui.hotkey('ctrl', 'v');
    pyautogui.press('enter')  # 发送。
    time.sleep(PAUSE)

eg.msgbox('刷屏结束', title='Finish.')  # 弹窗提示刷屏结束。
