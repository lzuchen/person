from pyecharts.charts import *
from pyecharts import options as opts
cate = ['变道',
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
data = [8925, 2543, 1913, 1003, 430, 284, 281, 262, 53, 7, 6, 1]

pie = (Pie()
       .add('', [list(z) for z in zip(cate, data)])
       )
pie.set_series_opts(
    # 自定义数据标签
    label_opts=opts.LabelOpts(position='top',
                              formatter='{d}%'
                              )
)
pie.set_global_opts(legend_opts=opts.LegendOpts(is_show=True,
                                                 pos_left='5%',
                                                 pos_bottom='30%',
                                                orient='vertical'),
                    title_opts=opts.TitleOpts(title="分类后场景占比"))
pie.render("各个场景的占比.html")