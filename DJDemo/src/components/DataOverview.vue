<script setup>
import axios from '@/utils/axios.js'
import {ref} from "vue";

// 获取数据
const tableData = ref()
const getData = () => {
  loading.value = true
  axios.get('/data', {
    params: {
      page: currentPage.value,
      per_page: pageSize.value,
      company: form.value.company,
      change_period: form.value.change_period,
      change: form.value.change,
      sort_period: form.value.sort_period,
      sort: form.value.sort,
      ascending: form.value.ascending,
    }
  })
    .then((res) => {
      tableData.value = res
      console.log(res.data)
      loading.value = false
    })
}

// 表格列数据
const columns = ref([
  { key: '股票代码', dataKey: '股票代码', title: '股票代码', width: 150, fixed: 'left' },
  { key: '公司名称', dataKey: '公司名称', title: '公司名称', width: 150, fixed: 'left' },
  { key: '所属模块', dataKey: '所属模块', title: '所属模块', width: 150 },
  { key: '最新价', dataKey: '最新价', title: '最新价', width: 150 },
  { key: '涨跌_今日', dataKey: '涨跌_今日', title: '今日涨跌', width: 150 },
  { key: '涨跌_5日', dataKey: '涨跌_5日', title: '5日涨跌', width: 150 },
  { key: '涨跌_10日', dataKey: '涨跌_10日', title: '10日涨跌', width: 150 },
  { key: '今日主力流入_元', dataKey: '今日主力流入_元', title: '今日主力流入', width: 150 },
  { key: '主力净占比_今日', dataKey: '主力净占比_今日', title: '今日主力净占比', width: 150 },
  { key: '主力净占比_5日', dataKey: '主力净占比_5日', title: '5日主力净占比', width: 150 },
  { key: '主力净占比_10日', dataKey: '主力净占比_10日', title: '10日主力净占比', width: 150 },
  { key: '排名_今日', dataKey: '排名_今日', title: '今日排名', width: 150 },
  { key: '排名_5日', dataKey: '排名_5日', title: '5日排名', width: 150 },
  { key: '排名_10日', dataKey: '排名_10日', title: '10日排名', width: 150 },
]);

// 页码监听
const currentPage = ref(1)
const pageSize = ref(10)
const handleSizeChange = () => {
  getData()
}
const handleCurrentChange = () => {
  getData()
}

// 条件筛选
const form = ref({
  company: 'default',
  change_period: '今日',
  change: '9',
  sort_period: '今日',
  sort: 'ranking',
  ascending: 'True'
})

// 加载状态
const loading = ref(false);

// 按钮查询
const query = () => {
  getData()
}

// 数据初始化
getData()

</script>

<template>
<!--  表单-->
  <el-form class="search-form">
<!--    公司类型表单-->
    <el-form-item label="公司类型">
      <el-select v-model="form.company" >
        <el-option label="全部" value="default" />
        <el-option label="st" value="st" />
        <el-option label="停牌" value="suspend" />
      </el-select>
    </el-form-item>
<!--    涨跌查询表单-->
    <el-form-item label="按涨跌与时间查询">
      <el-select v-model="form.change_period" >
        <el-option label="今日涨跌" value="今日" />
        <el-option label="5日涨跌" value="5日" />
        <el-option label="10日涨跌" value="10日" />
      </el-select>
      <el-select v-model="form.change">
        <el-option label="全部" value=9 />
        <el-option label="涨" value=1 />
        <el-option label="无涨跌" value=0 />
        <el-option label="跌" value=-1 />
      </el-select>
<!--    排序表单-->
    </el-form-item>
    <el-form-item label="按类型与时间排序">
      <el-select v-model="form.sort_period">
        <el-option label="今日" value="今日" />
        <el-option label="5日" value="5日" />
        <el-option label="10日" value="10日" />
      </el-select>
      <el-select v-model="form.sort">
        <el-option label="名次排序" value="ranking" />
        <el-option label="涨跌幅排序" value="change" />
        <el-option label="主力净流入排序" value="main_inflow" />
      </el-select>
      <el-select v-model="form.ascending">
        <el-option label="正序" value='True' />
        <el-option label="逆序" value='False' />
      </el-select>
    </el-form-item>
  </el-form>
<!--  查询按钮-->
  <el-button type="success" @click="query">
    查询
  </el-button>
<!--  表格-->
  <el-auto-resizer>
    <template #default="{ height, width }">
      <el-table-v2
          :width="width"
          :height="400"
          class="table"
          v-loading="loading"
          :columns="columns"
          :data="tableData.data"
          :fixed="150"
      >
      </el-table-v2>
    </template>
  </el-auto-resizer>

<!--  分页器-->
  <el-pagination
      class="pagination"
      v-model:current-page="currentPage"
      v-model:page-size="pageSize"
      :page-sizes="[10, 20, 500, 1000]"
      layout="total, sizes, prev, pager, next, jumper"
      :total="tableData['now_total']"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
  />
</template>

<style scoped>
.search-form {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.search-form .el-form-item {
  width: 300px;
  margin: 10px 20px;
}

.pagination {
  margin: 20px;
}

</style>
