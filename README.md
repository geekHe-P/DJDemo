# DJDemo
为面试准备的前端+数据分析小demo

爬取东方财富网的深市A股个人资金流向中的数据，并对其数据进行分析，封装后端接口，前端请求数据并展示

数据来源：https://data.eastmoney.com/zjlx/detail.html

### 技术栈

+ 前端：vue3+vite
+ 后端：python+flask

+ 爬虫：requests，json
+ 数据分析：numpy，pandas
+ 前端ui：element-plus，Echarts

### 运行环境

+ 前端

  node：20.13.1

  vue：3.4.29

  echarts:   5.5.1
  element-plus：2.7.8

+ 后端

  python：3.9.19

  flask：2.23

  numpy：1.26.4

  pandas：2.2.2

### 目录树

```tree
//   前端文件
├── DJDemo
│   ├── index.html
│   ├── public
│   ├── src
│   │   ├── App.vue
│   │   ├── assets
│   │   ├── components
│   │   │   ├── DataAnalysis.vue // 数据分析板块
│   │   │   └── DataOverview.vue // 数据总览板块
│   │   ├── main.js
│   │   ├── router
│   │   │   └── index.js // 路由配置
│   │   ├── stores
│   │   ├── utils
│   │   │   ├── axios.js // 封装axios，请求响应拦截
│   │   │   └── toEchartsFormat.js // 将json数据转成echarts需要的格式
│   │   └── views
│   │       └── index.vue 
│   └── vite.config.js
//  后端文件
├── DataAnalysis
│   ├── __pycache__
│   │   ├── dataAnalysis.cpython-39.pyc
│   │   └── dataScraping.cpython-39.pyc
│   ├── data.csv  //输出的数据，以便观察
│   ├── data.json // 爬取的数据
│   ├── data.xlsx //输出的数据，以便观察
│   ├── dataAnalysis.py  // 数据分析
│   ├── dataScraping.py  // 爬虫
│   └── main.py
├── LICENSE
└── README.md

```

### 运行

+ 前端

  1. `pnpm install`

  2. `pnpm dev`或`vite`或到`package.json`文件点击执行

+ 后端` python main.py`

### 运行时图

+  数据总览

![](https://cdn.jsdelivr.net/gh/geekHe-P/picGo_0403/202407291324775.png)



+ 数据分析

![](https://cdn.jsdelivr.net/gh/geekHe-P/picGo_0403/202407291331945.png)



+ 饼图展示

![](https://cdn.jsdelivr.net/gh/geekHe-P/picGo_0403/202407291332124.png)
