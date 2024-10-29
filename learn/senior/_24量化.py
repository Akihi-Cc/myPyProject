# !/usr/local/bin/python3.12
# Python 量化
# Python 量化是指利用 Python 编程语言以及相关的库和工具来进行金融市场数据分析、策略开发和交易执行的过程。
# Python 由于其简洁、易学、强大的生态系统和丰富的金融库而成为量化交易的首选编程语言之一。
# 量化交易在金融领域得到广泛应用，它允许交易者通过系统性的方法来制定和执行交易策略，提高交易效率和决策的科学性。
# 量化主要是通过数学和统计学的方法，利用计算机技术对金融市场进行量化分析，从而制定和执行交易策略。
# 实例应用
# 接下来我们先看一个 Python 量化简单的应用实例，可以使用移动平均策略，使用雅虎金融数据来实现。
# 该策略的基本思想是通过比较短期和长期移动平均线来生成买入和卖出信号。
# 在进行这个简单实例前，需要先安装三个包：
# pip install pandas yfinance matplotlib

# 包说明：
# Pandas 是一个功能强大的开源数据处理和分析库，专门设计用于高效地进行数据分析和操作。
# yfinance 是一个用于获取金融数据的库，支持从 Yahoo Finance 获取股票、指数和其他金融市场数据。
# Matplotlib 是一个二维绘图库，用于创建静态、动态和交互式的数据可视化图表。

# 获取历史股票数据
# 使用 yfinance 获取历史股票数据，以下是一个简单的实例：
import yfinance as yf

# 获取股票数据
symbol = "600519.SS"
start_date = "2022-01-01"
end_date = "2023-01-01"

data = yf.download(symbol, start=start_date, end=end_date)
print(data.head())

# 简单的数据分析和可视化
# 使用 pandas 进行数据分析和 matplotlib 进行可视化：
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 获取股票数据
symbol = "600519.SS"
start_date = "2022-01-01"
end_date = "2023-01-01"

data = yf.download(symbol, start=start_date, end=end_date)
# 简单的数据分析
print(data.describe())

# 绘制股价走势图
data['Close'].plot(figsize=(10, 6), label=symbol)
plt.title(f"{symbol} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

# 移动平均交叉策略回测
# 回测是在历史市场数据上模拟和评估一个交易策略的过程。
# 以下是一个简单的移动平均交叉策略回测的实例代码，策略是在 50 日均线上穿越 200 日均线时买入，下穿越时卖出，策略的表现输出了总收益、年化收益和最大回撤等指标。
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 获取股票数据
symbol = "600519.SS"
start_date = "2021-01-01"
end_date = "2023-01-01"

data = yf.download(symbol, start=start_date, end=end_date)

# 计算移动平均
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

# 初始化交叉信号列
data['Signal'] = 0

# 计算交叉信号
data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1
data.loc[data['SMA_50'] < data['SMA_200'], 'Signal'] = -1

# 计算每日收益率
data['Daily_Return'] = data['Close'].pct_change()

# 计算策略信号的收益率（shift(1) 是为了避免未来数据的偏差）
data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']

# 计算累计收益
data['Cumulative_Return'] = (1 + data['Strategy_Return']).cumprod()

# 输出策略表现
strategy_performance = {
    'Total Return': data['Cumulative_Return'].iloc[-1] - 1,
    'Annualized Return': (data['Cumulative_Return'].iloc[-1] ** (252 / len(data))) - 1,
    'Max Drawdown': (data['Cumulative_Return'] / data['Cumulative_Return'].cummax() - 1).min(),
}

print("策略表现:")
for key, value in strategy_performance.items():
    print(f"{key}: {value:.4f}")

# 绘制累计收益曲线
plt.figure(figsize=(10, 6))
plt.plot(data['Cumulative_Return'], label='Strategy Cumulative Return', color='b')
plt.plot(data['Close'] / data['Close'].iloc[0], label='Stock Cumulative Return', color='g')
plt.title("Cumulative Return of Strategy vs. Stock")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()
plt.show()

# 请注意，这只是一个简单的实例，实际应用中需要更复杂的策略和更多的考虑因素。
