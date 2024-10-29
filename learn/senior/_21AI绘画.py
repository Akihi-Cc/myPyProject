# !/usr/local/bin/python3.12
# Python AI 绘画
# 本文我们将为大家介绍如何基于一些开源的库来搭建一套自己的 AI 作图工具。
# 需要使用的开源库为 Stable Diffusion web UI，它是基于 Gradio 库的 Stable Diffusion 浏览器界面
# Stable Diffusion web UI GitHub 地址：https://github.com/AUTOMATIC1111/stable-diffusion-webui
# 运行 Stable Diffusion 需要硬件要求比较高，运行时会消耗较大的资源，特别是显卡。
# Windows 环境安装
# 本地环境要求安装 Python 3.10.6 或以上版本，并把它加入到本机的环境变量中。
# 下载 Stable Diffusion web UI GitHub 源码 https://github.com/AUTOMATIC1111/stable-diffusion-webui。
# git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git

# Civitai 介绍
# Civitai 有许多定制好的模型，而且可以免费下载，我们使用国风3模型来测试，下载地址：https://civitai.com/models/10415/3-guofeng3?modelVersionId=36644
# 下载完后，我们将模型移动到 stable-diffusion-webui/models/Stable-diffusion 目录下，重新启动 stable-diffusion-webui ：
# ./webui.sh
# 这样我们就可以在模型列表中选择国风3模型了：
# 选择后，我们可以到模型介绍页面去拷贝一些提示词和测试参数：
