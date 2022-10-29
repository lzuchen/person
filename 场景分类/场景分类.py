from pyecharts.charts import *
data = [
    {"name": "判断",
     "children": [
             {"name": "普通场景",
              "children": [
                  {"name": "车道不变", "children": [{
                      "name":"直行","children":[{"name":"车道内加速直行"},{"name":"车道内匀速直行"},{"name":"车道内减速直行"}]
                  },
                  {
                      "name":"转弯","children":[{"name":"沿弯道加速直行"},{"name":"沿弯道匀速直行"},{"name":"沿弯道减速直行"}]
                  }
                  ]},
                  {"name": "车道变化", "children": [{
                      "name":"道路不变","children":[{"name":"变道"}]
                  },
                  {
                      "name":"道路变化","children":[{"name":"匝道"},{"name":"路口转弯"}]
                  }
                  ]},
              ]},
             {"name": "特殊场景",
              "children": [
                  {"name": "车道不变", "children": [{
                      "name":"直行","children":[{"name":"特殊场景下车道内加速直行"},{"name":"特殊场景下车道内匀速直行"},{"name":"特殊场景下车道内减速直行"}]
                  },
                  {
                      "name":"转弯","children":[{"name":"特殊场景下沿弯道加速直行"},{"name":"特殊场景下沿弯道匀速直行"},{"name":"特殊场景下沿弯道减速直行"}]
                  }
                  ]},
                  {"name": "车道变化", "children": [{
                      "name":"道路不变","children":[{"name":"特殊场景下变道"}]
                  },
                  {
                       "name":"道路变化","children":[{"name":"特殊场景下匝道"},{"name":"特殊场景下路口转弯"}]
                  }
                  ]},
              ]},
     ],
     }
]
tree = (
    Tree()
    .add("", data)
)

tree.render("场景分类")