# !/usr/local/bin/python3.12
# Python pyecharts 模块
# pyecharts 是一个基于 ECharts 的 Python 数据可视化库，它允许用户使用 Python 语言生成各种类型的交互式图表和数据可视化。
# ECharts 是由百度开发的一款强大的开源数据可视化库，而 Pyecharts 则是 ECharts 的 Python 封装，使得在 Python 中使用 ECharts 变得更加方便。
# pyecharts 提供了一组简单而灵活的 API，使用户能够轻松地创建各种图表，包括但不限于折线图、柱状图、散点图、饼图、地图等。
# 通过 pyecharts，用户可以使用 Python 语言处理和准备数据，然后使用简洁的代码生成交互式的图表，这些图表可以嵌入到 Web 应用程序中或保存为静态文件。

# pyecharts 特点与功能：
# 简单易用： Pyecharts 提供了直观而友好的 API，使得用户能够快速上手，轻松生成各种图表。
# 丰富的图表类型： 支持多种常见的图表类型，包括线图、柱状图、散点图、饼图、地图等，满足不同场景的需求。
# 支持主流数据格式： 能够处理常见的数据格式，如列表、字典、Pandas DataFrame 等。
# 交互性： 生成的图表可以具有交互性，用户可以通过鼠标悬停、缩放等方式与图表进行互动。
# 丰富的配置选项： 提供了丰富的配置选项，允许用户自定义图表的样式、布局等属性。
# 支持主题： 提供多种主题，用户可以根据需要选择合适的主题，使图表更符合应用的整体风格。

# pyecharts 安装
# pip 安装：
# pip install pyecharts
# 安装成功后可以查看 pyecharts 版本：
import pyecharts

print(pyecharts.__version__)

# pyecharts 图表类型
# pyecharts 支持以下图表类型图表：
# 图表类型	        pyecharts 类	包引入
# 折线图	            Line	        from pyecharts.charts import Line
# 柱状图	            Bar	            from pyecharts.charts import Bar
# 散点图	            Scatter	        from pyecharts.charts import Scatter
# 饼图	            Pie	            from pyecharts.charts import Pie
# 雷达图	            Radar	        from pyecharts.charts import Radar
# 热力图	            HeatMap	        from pyecharts.charts import HeatMap
# K 线图	        Kline	        from pyecharts.charts import Kline
# 箱线图	            Boxplot	        from pyecharts.charts import Boxplot
# 地图	            Map	            from pyecharts.charts import Map
# 词云图	            WordCloud	    from pyecharts.charts import WordCloud
# 仪表盘	            Gauge	        from pyecharts.charts import Gauge
# 漏斗图	            Funnel	        from pyecharts.charts import Funnel
# 树图	            Tree	        from pyecharts.charts import Tree
# 平行坐标系图	    Parallel	    from pyecharts.charts import Parallel
# 桑基图	            Sankey	        from pyecharts.charts import Sankey
# 地理坐标系图	    Geo	            from pyecharts.charts import Geo
# 时间线图	        Timeline	    from pyecharts.charts import Timeline
# 3D 散点图	        Scatter3D	    from pyecharts.charts import Scatter3D
# 3D 柱状图	        Bar3D	        from pyecharts.charts import Bar3D
# 3D 曲面图	        Surface3D	    from pyecharts.charts import Surface3D

# 创建第一个图表
# 接下来我们使用 Pyecharts 创建了一个简单的柱状图，展示了五个月份的销售额:
from pyecharts.charts import Bar

# 准备数据
x_data = ['一月', '二月', '三月', '四月', '五月']
y_data = [10, 20, 15, 25, 30]

# 创建柱状图
bar_chart = Bar()
bar_chart.add_xaxis(x_data)
bar_chart.add_yaxis("销售额", y_data)

# 也可以传入路径参数，如 bar_chart.render("bar_chart.html")
bar_chart.render()
# 如果在 bar_chart.render() 中不指定文件路径，Pyecharts 默认会在当前工作目录下生成一个名为 "render.html" 的文件，即生成的图表将保存在 "render.html" 文件中。

# 如果你希望图表的文件名有一定的规范，或者想要指定保存的路径，可以在 render() 方法中提供文件路径参数。例如：
# bar_chart.render("my_bar_chart.html")
# 这样，生成的图表就会保存在当前工作目录下的 "my_bar_chart.html" 文件中。
# 设置图表配置选项
# 实例中图表的标题是 "月度销售额柱状图"，横轴是月份，纵轴是销售额，可以根据实际需求调整数据和图表配置：
from pyecharts import options as opts
from pyecharts.charts import Bar

# 准备数据
x_data = ['一月', '二月', '三月', '四月', '五月']
y_data = [10, 20, 15, 25, 30]

# 创建柱状图
bar_chart = Bar()
bar_chart.add_xaxis(x_data)
bar_chart.add_yaxis("销售额", y_data)

# 配置图表
bar_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="月度销售额柱状图"),
    xaxis_opts=opts.AxisOpts(name="月份"),
    yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
)

# 渲染图表
bar_chart.render("bar_chart.html")
# 说明：
# Bar()：创建一个柱状图对象。
# add_xaxis 和 add_yaxis：分别用于添加横轴和纵轴的数据。
# set_global_opts：配置全局选项，包括标题、坐标轴的名称等。
# 生成的图表将保存为 "bar_chart.html" 文件，你可以在浏览器中打开该文件，查看生成的柱状图。

# 使用主题
# pyecharts 支持主题切换，用户可以根据自己的需求选择合适的主题来改变图表的样式。
# pyecharts 提供了 10+ 种内置主题，开发者也可以定制自己喜欢的主题。
# 以下是一个简单的例子，演示了如何使用 pyecharts 切换主题：
from pyecharts import options as opts
from pyecharts.charts import Bar
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

# 准备数据
x_data = ['一月', '二月', '三月', '四月', '五月']
y_data = [10, 20, 15, 25, 30]

# 创建柱状图
bar_chart = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # 初始主题为亮色系
bar_chart.add_xaxis(x_data)
bar_chart.add_yaxis("销售额", y_data)

# 配置图表
bar_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="月度销售额柱状图"),
    xaxis_opts=opts.AxisOpts(name="月份"),
    yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
)

# 切换到暗色系主题
bar_chart.set_global_opts(theme=ThemeType.DARK)

# 渲染图表
bar_chart.render("themed_bar_chart.html")
# 以上例子演示了如何在 pyecharts 中使用 ThemeType 来切换主题，pyecharts 支持的主题类型包括 LIGHT（亮色系）、DARK（暗色系）等，你可以根据需求选择合适的主题。
# init_opts=opts.InitOpts(theme=ThemeType.LIGHT)：在创建图表对象时，通过 init_opts 参数指定图表的初始主题，这里设置为亮色系。

# 以下是 pyecharts 支持的主题列表：
#
# Light Themes（亮色系主题）:
#
# "LIGHT": 亮色系默认主题
# "WESTEROS": 经典的暖色调主题
# "CHALK": 粉笔风格主题
# "ESSOS": 温和的绿色调主题
# "INFOGRAPHIC": 信息图形主题
# "MACARONS": 美味糖果色主题
# Dark Themes（暗色系主题）:
#
# "DARK": 暗色系默认主题
# "PURPLE-PASSION": 深紫色调主题
# "SHINE": 简洁的黑色调主题
# "VINTAGE": 复古风格主题
# "ROMA": 古罗马风格主题
# "WALDEN": 森林深色系主题
# 用户可以通过设置自定义的颜色和样式来创建自定义主题。

# 设置全局配置项
# set_global_opts 是 pyecharts 中用于设置全局配置项的方法，该方法允许你配置整个图表的一些全局属性，如标题、坐标轴、图例等。
# 以下是一些常用的全局配置项：
bar_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="月度销售额柱状图", subtitle="副标题"),
    xaxis_opts=opts.AxisOpts(name="月份"),
    yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
    legend_opts=opts.LegendOpts(pos_left="center", pos_top="top"),
    toolbox_opts=opts.ToolboxOpts(),
    tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
)
# 说明：
# title_opts:                   标题配置项，可以设置主标题和副标题，以及相关的样式设置。
# xaxis_opts 和 yaxis_opts:      x 轴和 y 轴的配置项，可以设置轴的名称、轴线样式等。
# legend_opts:                  图例配置项，可以设置图例的位置、样式等。
# toolbox_opts:                 工具箱配置项，用于添加一些交互工具，如保存为图片、数据视图等。
# tooltip_opts:                 提示框配置项，可以设置提示框的触发方式、样式等。

from pyecharts import options as opts
from pyecharts.charts import Bar

# 准备数据
x_data = ['一月', '二月', '三月', '四月', '五月']
y_data = [10, 20, 15, 25, 30]

# 创建柱状图
bar_chart = Bar()
bar_chart.add_xaxis(x_data)
bar_chart.add_yaxis("销售额", y_data)

# 配置全局属性
bar_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="月度销售额柱状图", subtitle="副标题"),
    xaxis_opts=opts.AxisOpts(name="月份"),
    yaxis_opts=opts.AxisOpts(name="销售额（万元）"),
    legend_opts=opts.LegendOpts(pos_left="center", pos_top="top"),
    toolbox_opts=opts.ToolboxOpts(),
    tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
)

# 渲染图表
bar_chart.render("global_options_bar_chart.html")
