# !/usr/local/bin/python3.12
# Python3 pip
# pip 是 Python 包管理工具，该工具提供了对 Python 包的查找、下载、安装、卸载的功能。
# 查看是否已经安装 pip 可以使用以下命令：
# pip --version

# 下载安装包使用以下命令：
# pip install some-package-name
# 例如我们安装 numpy 包：
# pip install numpy

# 我们也可以轻易地通过以下的命令来移除软件包：
# pip uninstall some-package-name
# 例如我们移除 numpy 包：
# pip uninstall numpy

# 如果要查看我们已经安装的软件包，可以使用以下命令：
# pip list


# 导出当前 Python 环境的配置
# 要导出当前 Python 环境的配置，你可以使用 pip freeze 命令。
# pip freeze 命令会列出当前环境中已安装的所有 Python 包及其版本信息，你可以将其保存到文件中，例如 requirements.txt，如下所示：
# pip freeze > requirements.txt
# 以上命令将在当前目录下创建一个名为 requirements.txt 的文件，其中包含当前环境中已安装的所有包及其版本信息。
# 然后，你可以在其他地方使用该文件来重新创建相同的环境，运行以下命令：
# pip install -r requirements.txt
# 以上命令会根据 requirements.txt 中列出的包及其版本信息重新安装所有必需的包，从而重建相同的环境。

# 扩展内容
# Anaconda 介绍
# Anaconda 发行版包含了 Python。
# Anaconda 是一个集成的数据科学和机器学习环境，其中包括了 Python 解释器以及大量常用的数据科学库和工具。
# Anaconda 包及其依赖项和环境的管理工具为 conda 命令，文与传统的 Python pip 工具相比 Anaconda 的 conda 可以更方便地在不同环境之间进行切换，环境管理较为简单。
#
