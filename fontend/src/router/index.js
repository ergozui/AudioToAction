import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/homePage' // 引入首页组件
import History from '@/components/historyPage' // 引入历史页组件
import Login from '@/components/loginPage' // 引入历史页组件
import Register from "@/components/RegisterPage"
import UserInfo from "@/components/UserInfo"
// 创建路由器实例
const router = createRouter({
  history: createWebHistory(),  // 在调用 createWebHistory() 即可
  routes:[
    {
      path: '/', // 路由路径为根路径
      name: 'Home', // 路由名称为 home
      component: Home // 对应的组件为 HomePage
    },
    {
      path: '/historyPage', // 路由路径为 /history
      name: 'History', // 路由名称为 history
      component: History // 对应的组件为 HistoryPage
    },
    {
      path: '/UserInfo', // 路由路径为 /history
      name: 'User', // 路由名称为 history
      component: UserInfo, // 对应的组件为 HistoryPage
    },
    {
      path:'/loginPage',
      name:'login',
      component:Login,
    },
    {
      path:'/registerPage',
      name:'register',
      component:Register,
    },

  ]
})

export default router

