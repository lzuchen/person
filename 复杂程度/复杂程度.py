from pyecharts.charts import *
from pyecharts import options as opts
x_data = ['变道',
 '车道内加速直行',
 '车道内减速直行',
 '车道内匀速直行',
 '沿弯道加速行驶',
 '特殊场景下变道',
 '路口转弯',
 '沿弯道减速行驶',
 '沿弯道匀速行驶',
 '特殊场景下路口转弯',
 '特殊场景下车道内减速直行',
 '特殊场景下车道内加速直行']
y_data = [12.44862745, 11.17734959, 11.42550967, 12.09072782, 11.31162791,
        8.22887324, 12.5088968 , 10.79389313,  9.05660377,  8.14285714,
        7.        ,  7.        ]

bar = (Bar(init_opts=opts.InitOpts(width='1000px', height='600px'))
       .add_xaxis(x_data)
       .add_yaxis('', y_data)
      )
bar.set_global_opts(legend_opts=opts.LegendOpts(is_show=True,
                                                 pos_left='5%',
                                                 pos_bottom='30%',
                                                orient='vertical'),
                    title_opts=opts.TitleOpts(title="复杂程度"),
                    tooltip_opts=opts.TooltipOpts(is_show=False),
                    xaxis_opts=opts.AxisOpts(
                        axislabel_opts={"interval": "0","rotate":20},
                    ),
                    yaxis_opts=opts.AxisOpts(
                        # 分割线配置，显示 y 轴每个刻度的分割线
                        splitline_opts=opts.SplitLineOpts(is_show=True),
                    )
                    )
bar.render("复杂程度.html")