<template>
  <div class="home">
    <div class="box1">
      <div id="highlight2">
      User Info
      </div>
    </div>
    <div class="box2">
      <div class="box3">
      <div class="line1">
        <div class="tag">
        <span><el-icon><User /></el-icon> Username</span>
          <span class="right">{{Username}}</span>
        </div>
        <el-divider />
      </div>
        <div class="line2">
          <div class="tag">
            <span><el-icon><Calendar /></el-icon> Register_Time</span>
            <span class="right">{{Register_Time}}</span>
          </div>
          <el-divider />
        </div>
        <div class="line2">
          <div class="tag">
            <span><el-icon><Memo /></el-icon> Transcript_Time</span>
            <span class="right">{{Transcript_Time}}</span>
          </div>
        </div>
      </div>

    </div>
    <div class="box4">
    <el-button type="primary" @click="logout()" class='el-button' size="large">
      logout
    </el-button>
    </div>
  </div>

</template>

<script setup>
import {ref,onMounted} from "vue";
import axios from '@/main';
import {ElMessage} from "element-plus";
const Username=ref();
const Register_Time=ref();
const Transcript_Time=ref();
import { useRouter } from 'vue-router'
const router = useRouter()

const open4 = () => {
  ElMessage({
    showClose: true,
    message: 'Please login.',
    type: 'error',
  })
}
onMounted(async () => {
  const response=await axios.post('http://localhost:5000/userinfo');
  const jsondata=response.data;
  if(jsondata.state=='error'){
    open4();
    router.push('/loginPage');
  }
  else{
    Username.value=jsondata.username;
    Register_Time.value=jsondata.register_time;
    Transcript_Time.value=jsondata.usetimes;
  }
})
const logout=async()=>{
  const response=await axios.post('http://localhost:5000/logout');
  const jsondata=response.data
  if(jsondata.state=='success'){
    open2();
    router.push('/loginPage');
  }
  else{
    open5();
  }

}
const open2 = () => {
  ElMessage({
    showClose: true,
    message: 'logout success!',
    type: 'success',
  })
}

const open5 = () => {
  ElMessage({
    showClose: true,
    message: 'somehing srror.',
    type: 'error',
  })
}
</script>
<style scoped>
.home{
  height:820px;
}

#highlight2 {
  font-family: 'Times New Roman', Times, serif;
  margin-top: 50px;
  padding-bottom: 1rem;
  color: black;
  margin-bottom: 50px;
  font-size: 45px;
  font-weight: 700;
  line-height: 1;
  text-align: center;
}
.box1{
  margin: 0 auto; /* 水平居中 */
  height:100px;
}
.box2{
  width:600px;
  height:259px;
  margin: 0 auto; /* 水平居中 */
  background-color: white;
  text-align: center;
  font-size:20px;
  font-family: 'Times New Roman', Times, serif;
}
.box3{
  width:500px;
  height:259px;
  margin: 0 auto; /* 水平居中 */
  background-color: white;
  text-align: center;
  font-size:20px;
  font-family: 'Times New Roman', Times, serif;
}
.tag{
  padding-top: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.right{
  text-align: right;
}
.box4{
  padding-top: 50px;
  margin: 0 auto; /* 水平居中 */
  text-align: center;
  font-family: 'Times New Roman', Times, serif;
  font-size: 30px;
}
.el-button{
  font-family: 'Times New Roman', Times, serif;
  font-size: 20px;
}
</style>