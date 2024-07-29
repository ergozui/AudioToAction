import { createApp } from 'vue'
import App from './App.vue'
import routes from './router/index';
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import axios from "axios";
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
//创建一个新的请求实例instance,instance.的用法和axios.的用法一致，可以使用instance({})、instance.get（）、instance.post()
const instance = axios.create({
  baseURL: 'http://localhost:5000/',
  timeout: 60000,
  withCredentials: true,   //配置此处,允许携带cookie发送请求
});
export default instance;
const app=createApp(App)
app.use(routes)
app.use(ElementPlus);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
app.mount('#app')