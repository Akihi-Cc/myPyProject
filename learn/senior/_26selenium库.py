# !/usr/local/bin/python3.12
# Python selenium 库
# Selenium 是一个用于自动化 Web 浏览器操作的强大工具，广泛应用于 Web 应用程序测试、网页数据抓取和任务自动化等场景。
# Selenium 为各种编程语言提供了 API，用作测试。 目前的官方 API 文档有 C#、JavaScript、Java、Python、Ruby。
# 安装 Selenium 和 WebDriver
# 安装 Selenium
# 要开始使用 Selenium，首先需要安装 selenium 库，并下载适用于你浏览器的 WebDriver。

# 使用 pip 安装 Selenium：
# pip install selenium
# 安装完成后，可以使用以下命令查看 selenium 的版本信息：

# pip show selenium
# 也可以使用 Python 代码查看：

import selenium

print(selenium.__version__)

# 下载WebDriver
# Selenium 需要一个 WebDriver 来与浏览器进行交互。
# 不同的浏览器需要不同的 WebDriver，例如 Chrome 浏览器需要 ChromeDriver，你需要根据你使用的浏览器下载相应的 WebDriver，并确保它在你的系统 PATH 中。

# Chrome: ChromeDriver
# Firefox: GeckoDriver
# Edge: EdgeDriver
# Safari: SafariDriver
# 选择浏览器并初始化 WebDriver：
from selenium import webdriver

# 使用 Chrome 浏览器
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# 或者使用 Firefox 浏览器
# driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

# 或者使用 Edge 浏览器
# driver = webdriver.Edge(executable_path='/path/to/msedgedriver')

# 从 Selenium 4 开始，在浏览器驱动的管理方式上发生了变化：Selenium 4 尝试自动检测系统中安装的浏览器版本，并下载相应的驱动程序，这意味着用户不再需要手动下载和设置驱动程序路径，除非他们需要特定版本的驱动程序。
from selenium import webdriver

driver = webdriver.Chrome()  # 如果使用其他浏览器，如 Firefox，需要相应修改
# 当国内的网络环境，自动检测下载驱动需要不一样的网络环境，所以建议手动下载驱动，然后指定驱动路径。
# 在 Selenium 4 中，不再直接在 webdriver.Chrome 中设置驱动程序路径，而是通过引入 Service 对象来设置。这样可以避免弃用警告，并确保驱动程序的正确加载。例如：
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path="PATH_TO_DRIVER")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 以下代码指定驱动文件路径来获取网页标题：
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# 设置正确的驱动路径
service = ChromeService(executable_path="/RUNOOB/Downloads/chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 打开一个网站
driver.get("https://cn.bing.com")

# 获取页面标题
print(driver.title)

# 关闭浏览器
driver.quit()

# 基本用法
# 初始化 WebDriver
# 选择浏览器并初始化 WebDriver：
from selenium import webdriver

# 使用 Chrome 浏览器
driver = webdriver.Chrome()

# 或者使用 Firefox 浏览器
# driver = webdriver.Firefox()

# 或者使用 Edge 浏览器
# driver = webdriver.Edge()

# 打开网页
# 使用 get() 方法打开网页：

driver.get("https://www.baidu.com")

# 查找页面元素
# 可以通过多种方式查找页面元素，例如使用 ID、类名、标签名等：
# 通过 ID 查找元素
search_box = driver.find_element("id", "kw")

# 通过类名查找元素
search_button = driver.find_element("class name", "s_ipt")

# 通过标签名查找元素
links = driver.find_elements("tag name", "a")

# 模拟用户操作
# Selenium 可以模拟用户在浏览器中的操作，例如点击、输入文本等：
# 在搜索框中输入文本
search_box.send_keys("Selenium Python")

# 点击搜索按钮
search_button.click()

# 获取元素属性和文本
# 可以获取页面元素的属性值或文本内容：
# 获取元素的文本
element_text = search_box.text

# 获取元素的属性值
element_attribute = search_box.get_attribute("placeholder")

# 等待
# 有时页面加载需要时间，可以使用显式等待或隐式等待来确保元素可操作：
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 显式等待
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "kw"))
)

# 隐式等待
driver.implicitly_wait(10)

# 关闭浏览器
# 操作完成后，记得关闭浏览器：
driver.quit()

# 简单的网页自动化
# 下面是一个简单的 Selenium 项目示例，用于自动化搜索关键词，并获取结果页面的标题。
from selenium import webdriver
from selenium.webdriver.common.by import By  # 导入 By 模块
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置驱动的路径，启动浏览器
service = ChromeService(executable_path="/RUNOOB/Downloads/chromedriver-mac-arm64/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    # 打开百度首页
    driver.get("https://www.baidu.com")

    # 查找搜索框元素
    search_box = driver.find_element(By.ID, "kw")

    # 输入搜索内容
    search_box.send_keys("Selenium Python")

    # 提交搜索表单
    search_box.send_keys(Keys.RETURN)

    # 等待搜索结果加载
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content_left"))
    )

    # 打印页面标题
    print("页面标题是:", driver.title)

finally:
    # 关闭浏览器
    driver.quit()

# selenium 常用方法
# 下表列出了 selenium 库的常用方法：
# 方法	                                    说明	                            示例代码
# webdriver.Chrome()	                    初始化 Chrome 浏览器实例。	        driver = webdriver.Chrome()
# driver.get(url)	                        访问指定的 URL 地址。	                driver.get("https://example.com")
# driver.find_element(By, value)	        查找第一个匹配的元素。             	element = driver.find_element(By.ID, "id")
# driver.find_elements(By, value)	        查找所有匹配的元素。	                elements = driver.find_elements(By.CLASS_NAME, "class")
# element.click()	                        点击元素。	e                       lement.click()
# element.send_keys(value)	                向输入框中发送键盘输入。	            element.send_keys("text")
# element.text	                            获取元素的文本内容。	                text = element.text
# driver.back()	                            浏览器后退。	                        driver.back()
# driver.forward()	                        浏览器前进。	                        driver.forward()
# driver.refresh()	                        刷新当前页面。	                    driver.refresh()
# driver.execute_script(script, *args)	    执行 JavaScript 脚本。	            driver.execute_script("alert('Hello!')")
# driver.switch_to.frame(frame_reference)	切换到指定的 iframe。	                driver.switch_to.frame("frame_id")
# driver.switch_to.default_content()	    切换回主文档。	                    driver.switch_to.default_content()
# driver.quit()	                            关闭浏览器并退出驱动。	                driver.quit()
# driver.close()	                        关闭当前窗口。	                    driver.close()
