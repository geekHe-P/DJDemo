<script setup>
import {ref, watch} from 'vue'
import { useRoute } from 'vue-router'

// 获取当前路由
const route = useRoute()

const activeIndex = ref(route.path)

// 监听路由变化，更新 activeIndex
watch(() => route.path, (newPath) => {
  activeIndex.value = newPath
})
</script>

<template>
  <header>
    <el-menu
        :default-active="activeIndex"
        mode="horizontal"
        router
    >
      <el-menu-item index="/data_overview">数据总览</el-menu-item>
      <el-menu-item index="/data_analysis">数据分析</el-menu-item>
      <el-menu-item index="0" disabled>
        深市a股的个股资金流（2024.7.28下午爬取）
      </el-menu-item>
    </el-menu>
    <div class="h-6" />
  </header>
  <router-view />
</template>

<style scoped>

</style>
