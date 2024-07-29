<template>

  <div id="highlight2">
    History
  </div>
  <div class="box">
  <el-table :data="tableData.slice((currentPage - 1) * pageSize, currentPage * pageSize)" stripe border class="table" :header-cell-style="{ background: '#f4f6f8', color: '#000000' } ">
    <el-table-column  prop='id' label="id" width="60px" align="center"  >
      </el-table-column>
    <el-table-column prop="title" label="title" align="center"/>
    <el-table-column prop="type" label="type" align="center"/>
    <el-table-column prop="status" label="status" align="center">
    <template v-slot="{ row }">
      <el-tag type="success">{{ row.status}}</el-tag>
    </template>
      </el-table-column>
    <el-table-column prop="created_on" label="created_on" align="center"/>
    <el-table-column  label="action" align="center">
      <template v-slot="{ row }">
        <a :href="row.link" target="_blank" @click="showDialog(row, $event)" style="color: #409EFF">{{row.action}}</a>
        &nbsp;&nbsp;
        <a :href="row.link"  @click="deleteItem(row)" style="color: #F56C6C">delete</a>
        <el-dialog v-model="row.dialogVisible" title="Task detail" center :append-to-body="true" class="dialog">
          <el-collapse>
            <el-collapse-item v-model="row.collapseAnalysis">
              <template #title>
                <span>Analysis Result</span> <!-- 标题文本 -->
                <el-button  class="audio-button" circle @click.stop="playAudio" > <el-icon size="20"><Microphone /></el-icon></el-button> <!-- 标题旁的按钮 -->
              </template>

              <div>{{ tableData.find(item => item.id === row.id).analysis }}
              </div>

            </el-collapse-item>
            <el-collapse-item title="Content" v-model="row.collapseContent">
              <div>{{ tableData.find(item => item.id === row.id).content }}</div>
            </el-collapse-item>
          </el-collapse>
          <div v-if="row.audio">
              <audio id='audio' ref='audioElement' class="audio" controls="controls">
                <source :src="row.audio" type="audio/mpeg">
              </audio>
          </div>
        </el-dialog>
      </template>
    </el-table-column>
  </el-table>
    <div>
      <el-switch v-model="value" />
      <hr class="my-4" />
      <el-pagination
          :hide-on-single-page="value"
          layout="prev, pager, next,jumper, ->, total"
          background
          default-page-size
          :total="tableData.length"
          :page-size="pageSize"
          :current-page="currentPage"
          @current-change="handleCurrentChange"
      />
    </div>
  </div>

</template>

<script lang="js" setup>

import {ElMessage} from "element-plus";
import { useRouter } from 'vue-router'
const router = useRouter()
const pageSize = ref(10); // 每页展示的数据条数
const tableData = ref([]);
const currentPage=ref(1); //当前页 刷新后默认显示第一页
import { ref,onMounted } from 'vue'
const value = ref(false)
const open2 = () => {
  ElMessage({
    showClose: true,
    message: 'Congrats,Success get data.',
    type: 'success',
  })
}

const open4 = () => {
  ElMessage({
    showClose: true,
    message: 'Please login.',
    type: 'error',
  })
}
const open5 = () => {
  ElMessage({
    showClose: true,
    message: 'Something error.',
    type: 'error',
  })
}
const showDialog = async(row, event) => {
  event.preventDefault(); // 阻止默认行为，使超链接可以点击
  // row.dialogVisible = true; // 打开对应行的弹窗
  // 在这里可以根据需要执行其他操作，获取点击行的数据
  row.dialogVisible = true; // 打开对应行的弹窗
  const formdata=new FormData()
  formdata.append('analysis',row.analysis)
  const response = await axios.post('http://localhost:5000/getaudio', formdata, {
    responseType: 'blob' // 指定响应数据的类型为blob
  },{
    headers:{
      "content-type":'audio/mpeg' ,
    }
  });
  const blobData = new Blob([response.data],{type:"audio/mpeg"}); // 创建Blob对象，并指定MIME类型
  row.audio = URL.createObjectURL(blobData); // 将Blob对象转换为可直接播放的URL格式
  console.log(row.audio)

  console.log('点击行的数据:', row);
};
import axios from '@/main';
onMounted(async () => {
    const response=await axios.post('http://localhost:5000/history');
    const jsonData=response.data;
    console.log(jsonData)
    if(jsonData.state=='error'){
      open4();
      router.push('/loginPage');
    }
    else {
      open2()
      let idCounter = 0; // 初始计数器变量
      jsonData.forEach(item => {
        const saveTime = new Date(item.save_time);
        const formattedSaveTime = saveTime.toLocaleString();
        const newdata = {
          id:++idCounter,
          title: item.title,
          type: item.task,
          created_on: formattedSaveTime,
          analysis: item.result,
          content: item.content,
          dialogVisible: false,
          status:'success',
          action:'check',
        }
        tableData.value.push(newdata);
      })
    }
});
const handleCurrentChange = (page) => {
  currentPage.value = page; // 更新当前页的值
};
const deleteItem=async(row)=> {
  const formData = new FormData();
  formData.append('id', row.id);
  const response = await axios.post('http://localhost:5000/delete', formData);
  const jsonData=response.data;
  if (jsonData.state == 'error') {
    open5();
  } else {
    location.reload();
  }
}
const audioElement = ref(null)
const playAudio=()=> {
  const targetElement = document.getElementById('audio');
  if (audioElement.value) {
    audioElement.value.play().catch(e => {
      console.error("播放音频时发生错误:", e);
      // 处理用户看不到的错误
    });
    if (targetElement) {
      targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }
}
</script>
<style scoped>
#highlight2 {
  font-family: 'Times New Roman', Times, serif;
  text-align: left;
  margin-top: 50px;
  padding-bottom: 1rem;
  color: black;
  margin-bottom: 50px;
  font-size: 45px;
  font-weight: 700;
  line-height: 1;
  left:50px;
  margin-left: 350px;
}
/*.table{*/
/*  width:150px;*/
/*  font-family: 'Times New Roman', Times, serif;*/
/*  text-align: center;*/
/*}*/
.box{
  width:1200px;
  height:720px;
  text-align: center;
  margin:auto;
  font-family: 'Times New Roman', Times, serif;
}

.dialog{
  font-family: 'Times New Roman', Times, serif;
  font-size: 20px;
}
.audio{
  padding-top: 20px;
  text-align: center;
}
.audio-button{
  border: none; /* 移除边框 */
  outline: none; /* 在聚焦时移除轮廓，有助于保持样式的一致性 */
  background-color: transparent;
}
.audio-button:active {
  background-color: transparent;
}
</style>