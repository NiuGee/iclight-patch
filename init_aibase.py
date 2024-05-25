import subprocess
import imageio
import json
import os
import ctypes 
import webbrowser
import torch

def print_panda():
    panda = """
      ／＞　 フ
      | 　_　_|   _<  看到我代表基本环境没问题了，如果有问题浏览器手动访问 http://127.0.0.1:8866
    ／` ミ＿xノ      \ 支持牛哥，给牛哥充个电 https://niugee.com/make_a_love/  
   /　　　　 |
  /　 ヽ　　 ﾉ
 │　　|　|　|
 ／￣|　　 |　|
(￣ヽ＿_ヽ_)__)
 """
    print(panda)

def print_free_info():
    print("  -------------------------------------------------------------------------------------------")
    print("  | 这个程序是免费的！！如果你是花钱买的，赶紧退款，去 https://niugee.com 直接下载最新版本! |")
    print("  | 这个程序是免费的！！如果你是花钱买的，赶紧退款，去 https://niugee.com 直接下载最新版本! |")
    print("  | 这个程序是免费的！！如果你是花钱买的，赶紧退款，去 https://niugee.com 直接下载最新版本! |")
    print("  | 要支持也是支持牛哥，给牛哥充电 ：https://niugee.com/make_a_love/ !                      |")
    print("  | 要支持也是支持牛哥，给牛哥充电 ：https://niugee.com/make_a_love/ !                      |")
    print("  | 要支持也是支持牛哥，给牛哥充电 ：https://niugee.com/make_a_love/ !                      |")
    print("  --------------------------------------------------------------------------------------------")

# 检查 ffmpeg 是否安装
def is_ffmpeg_installed():
    try:
        # 尝试执行 ffmpeg 命令并获取其版本信息
        result = subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # 如果命令执行成功，返回 True
        return result.returncode == 0
    except FileNotFoundError:
        # 如果执行失败（找不到文件），返回 False
        return False

def auto_install_ffmpeg():
    try:
        if not is_ffmpeg_installed():
            # 如果没有安装，则下载 ffmpeg
            imageio.plugins.ffmpeg.download()
            print("没安装ffmpeg，牛哥帮你装好了.")
        else:
            print("ffmpeg is already installed.")
    except Exception as e:
        print("安装ffmpeg失败:", e)

def get_gradio_cfg():
    cfg = {
        "share": False,
        "port": 8866,
    }

    try:
        # 当前目录下的 config.json 文件
        cfg_file = os.path.join(os.path.dirname(__file__), "config.json")
        if os.path.exists(cfg_file):
            print(f"读取配置文件: {cfg_file}")
            with open(cfg_file, "r") as f:
                cfg = json.load(f)
                print(f"配置文件内容: {cfg}")
    except Exception as e:
        print(f"读取配置文件失败: {e}")

    return cfg

def show_message(message, title="牛哥提示"):
    # 弹出一个Windows MessageBox，提示用户
    ctypes.windll.user32.MessageBoxW(0, message, title, 0)

def show_niugee_tip():
    try:
        # 弹出一个Windows MessageBox，提示用户     
        show_message("看到这个提示，说明你已经成功 98% 了！所有的基础资源装载完毕，接下来就是享受牛哥的AI服务啦！")

        print("-------")
        print(">>>> 如果网页没有自动打开，或此时出现错误，请检查你的防火墙，或者关闭代理再次尝试。")
        print(">>>> 如果要向牛哥反馈问题，请提供这个窗口内的相关内容，越详细越好，你可以用鼠标选中很多行（从这一行开始），然后发给牛哥。")
        print("-------")

        # 打开一个网址：https://niugee.com
        # webbrowser.open('https://niugee.com?source=iclight1.0')
    except Exception as e:
        print("显示提示失败:", e)
    
def detect_cuda_info():
    try:
        # 打印PyTorch版本
        print("PyTorch 版本:", torch.__version__)

        # 打印CUDA的可用性
        print("CUDA 状态:", torch.cuda.is_available())

        # 打印当前为PyTorch选择的CUDA版本（如果可用）
        if torch.cuda.is_available():
            print("CUDA 版本:", torch.version.cuda)
    except Exception as e:
        print("检测CUDA信息失败:", e)