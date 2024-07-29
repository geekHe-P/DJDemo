import { createRouter, createWebHistory } from 'vue-router'
import DataOverview from "@/components/DataOverview.vue";
import DataAnalysis from "@/components/DataAnalysis.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/data_overview'
    },
    {
      path: '/data_overview',
      name: 'data_overview',
      component: DataOverview
    },
    {
      path: '/data_analysis',
      name: 'data_analysis',
      component: DataAnalysis
    },
  ]
})

export default router
