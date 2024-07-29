<script setup>
import * as echarts from 'echarts';
import {onMounted, ref} from "vue";
import axios from "@/utils/axios.js";
import echartsFormat from "@/utils/toEchartsFormat.js";

// 拿到dom
const company_class_dom_top = ref()
const company_class_dom_low = ref()

// 加载状态
const loading = ref(false)

// 请求数据
const get_company_class_info = () => {
  loading.value = true
  axios.get(`/company_class_index`, {
    params: {
      'start': 0,
      'end': 15
    }
  })
      .then(res => {
        company_class_more.value = res.data
        let formattedData = echartsFormat(res.data)
        // 配置表格
        myChart_class_top.setOption(company_class_option.value);
        myChart_class_top.setOption({
          series: [{
            data: formattedData
          }]
        })
      })

  axios.get(`/company_class_index`, {
    params: {
      'start': -16,
      'end': -1
    }
  })
      .then(res => {
        company_class_low.value = res.data

        let formattedData = echartsFormat(res.data)
        // 配置表格
        myChart_class_low.setOption(company_class_option.value);
        myChart_class_low.setOption({
          title: {
            text: '公司数量最少的板块（后15名）',
          },
          series: [{
            data: formattedData
          }]
        })
      })

  axios.get('/company_class_info')
      .then((res) => {
        company_class_info.value = res
        // let formattedData = echartsFormat(res.above_mean)
        // 配置表格
        // myChart_class_top.setOption(company_class_option.value);
        // myChart_class_top.setOption({
        //   series: [{
        //     data: formattedData
        //   }]
        // })

        loading.value = false
      })
}

// 拿数据
const company_class_info = ref()
const company_class_more = ref()
const company_class_low = ref()
get_company_class_info()

// 设置配置项
const company_class_option = ref({
  title: {
    text: '公司数量最多的板块（前15名）',
    top: 'top',
    left: 'center',
  },
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'horizontal',
    bottom: 'bottom',
    left: 'center'
  },
  series: [
    {
      name: '所属板块',
      type: 'pie',
      radius: '50%',
      data: [],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
})

let myChart_class_top = null
let myChart_class_low = null

onMounted(() => {
  // 初始化表格
  myChart_class_top = echarts.init(company_class_dom_top.value);
  myChart_class_low = echarts.init(company_class_dom_low.value);
})
</script>

<template>
  <div v-if="company_class_info">
    <h3>板块总数量：</h3>
    <span>
      {{ company_class_info.total }}
    </span>
  </div>
  <div v-if="company_class_info">
    <h3>
      板块下公司数量平均值：
    </h3>
    <span>
      {{ company_class_info.info.mean }}
    </span>
  </div>
  <div v-if="company_class_info">
    <h3>
      公司数量前15名的板块：
    </h3>
    <ul v-if="company_class_more">
      <li v-for='(index, item) in company_class_more' :key='index'>
        {{ item }}
      </li>
    </ul>
  </div>
  <div v-if="company_class_info">
    <h3>
      公司数量后15名的板块：
    </h3>
    <ul v-if="company_class_low">
      <li v-for='(index, item) in company_class_low' :key='index'>
        {{ item }}
      </li>
    </ul>
  </div>
  <h3>板块种类：</h3>
  <ul v-if="company_class_info">
    <li v-for='(item, index) in company_class_info.info.class' :key='index'>
      {{ item }}
    </li>
  </ul>
  <div class="pie_container" >
    <div v-loading="loading" ref="company_class_dom_top" class="company_class"></div>
    <div v-loading="loading" ref="company_class_dom_low" class="company_class"></div>
  </div>
</template>

<style scoped>
.company_class {
  width: 500px;
  height: 500px;
  margin: 20px;
}

ul {
  display: flex;
  flex-wrap: wrap;
}

li {
  width: 120px;
}

h3 {
  display: inline-block;
}

.pie_container {
  display: flex;
}
</style>
