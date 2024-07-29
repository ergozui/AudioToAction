<template>
  <div class="box1">
    <div class="mini_box">
      <div id="highlight1">
        Ready to use<br><br>
        Audio To Action <br><br>
        Application
      </div>
      <div style="color:#A8ABB2">  Explore Smart Transcript for sentiment analysis and content
        summarization. Upload text and audio files to gain insightful analysis
        and creative responses using OpenAI api and advanced technologies.
      </div>
      <div class="flex">
        <el-button type="primary" class="el-button" @click="handleButtonClick">
          Try it out !<el-icon class="el-icon--right"><Right /></el-icon>
        </el-button>
      </div>
    </div>

  </div>

  <el-divider />

  <div class="box2">
    <div id="highlight2">
      create your task
    </div>
    <div class="form-container">
    <el-form
        ref="ruleFormRef"
        :model="ruleForm"
        :rules="rules"
        label-width="60px"
        class="demo-ruleForm"
        :size="formSize"
        status-icon
    >
      <el-form-item label="Title" prop="title" class="title">
        <el-input v-model="ruleForm.title" autosize type='textarea' show-word-limit maxlength='50' placeholder='Please input task name' class="custom-input"/>
      </el-form-item>
      <el-form-item label="Type" prop="type" class="type">
        <el-select v-model="ruleForm.type" class="custom-select">
          <el-option label="Key points identification" value="Key points identification" />
          <el-option label="Action item extraction" value="Action item extraction" />
          <el-option label="summary_extraction" value="summary" />
          <el-option label="sentiment_analysis" value="sentiment" />
        </el-select>
      </el-form-item>
      <el-form-item label="Content" prop="content" class="content">
        <el-input v-model="ruleForm.content" class="custom-input" placeholder="Please enter the content but if you want to submit it by file please make sure this place is empty!" type="textarea"/>
      </el-form-item>
      <el-form-item label="Upload" prop="upload" class="upload">
      <el-upload action="" v-model="ruleForm.file" class="upload-demo" drag :http-request="uploadSectionFile" >
        <el-icon class="el-icon--upload"><upload-filled /></el-icon>
        <div class="el-upload__text">
          Drop file here or <em>click to upload</em>
        </div>
        <template #tip>
          <div class="el-upload__tip">
            mp3/mp4/doc/docx/pdf is OK
          </div>
        </template>
      </el-upload>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm()">
          Submit
        </el-button>
        <el-button @click="resetForm(ruleFormRef)">Reset</el-button>
      </el-form-item>
    </el-form>
    </div>
    </div>
</template>

<script lang="js" setup>
import { ElMessage } from 'element-plus'
import { reactive, ref } from 'vue'
import axios from '@/main';
import { useRouter } from 'vue-router'
const router = useRouter()
const formSize = ref('default')
const ruleFormRef = ref()
const ruleForm = reactive({
  title: '',
  type: '',
  content: '',
})
const uploadSectionFile=(param)=>{
  const file = param.file;
  ruleForm.file=file;
}
const rules = reactive({
  title: [
    { required: true, message: 'Please input task name', trigger: 'blur' },
    { min: 3, max: 20, message: 'Length should be 3 to 20', trigger: 'blur' },
  ],
  type: [
    {
      type: 'string',
      required: true,
      message: 'Please select at least one activity type',
      trigger: 'change',
    },
  ],
  content: [
    {
      required: false,
      message: 'Please enter the content but if you want to submit it by file please make sure this place is empty! ',
      trigger: 'blur',
    }
  ],
})

const open2 = () => {
  ElMessage({
    showClose: true,
    message: 'Congrats, Submit success.',
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
    message: 'something error!',
    type: 'error',
  })
}
const submitForm = async () => {
  try {
  //   const valid = await ruleForm.validate();
  //   if (valid) {
      // 构造请求体
      const formData = new FormData();
      formData.append('title', ruleForm.title);
      formData.append('type', ruleForm.type);
      formData.append('content', ruleForm.content);

      // 处理文件上传
      // const files = formEl.files;
      // for (let i = 0; i < files.length; i++) {
      //   formData.append('files', files[i].raw);
      // }
      formData.append('file', ruleForm.file);
      console.log(formData.keys())
      // 发送 POST 请求
      const response = await axios.postForm('http://localhost:5000/openai', formData);
      const responseData = response.data; // 获取后端返回的字符串数据
      if(responseData.state=='success'){
        open2();
        router.push('/historyPage');
      }
      else if(responseData.state=='logerror'){
        open4();
        router.push('/loginPage');
      }
      else{
        open5();
      }

      // 根据后端接口返回的响应做相应处理
      console.log(response);
    // } else {
    //   // 表单验证不通过
    //   console.log('Validation failed');
      // 可以添加更多的逻辑来处理验证不通过的情况，例如显示错误提示信息
    // }
  } catch (error) {
    // 处理请求错误
    console.error(error);
  }
}

const resetForm = (formEl) => {
  if (!formEl) return
  formEl.resetFields()
}

const handleButtonClick=()=>{
  // 获取目标元素
  const targetElement = document.getElementById('highlight2');
  if (targetElement) {
    targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}
</script>

<style scoped>
.container{
  height:600px;
  /*margin: 0 auto; !* 水平居中 *!*/
  /*text-align: center; !* 水平居中 *!*/
  font-family: 'Times New Roman', Times, serif;
}

.box1{
  width:800px;
  height: 400px;
  margin: 0 auto; /* 水平居中 */
  /*text-align: center; !* 水平居中 *!*/
  font-family: 'Times New Roman', Times, serif;
  left: 50px;
}
.mini_box{
  margin-top: 50px;
}

#highlight1 {
  text-align: left;
  margin-top: 1rem;
  padding-bottom: 1rem;
  color: black;
  margin-bottom: 0.4rem;
  font-size: 30px;
  font-weight: 700;
  line-height: 1;
  left:50px;
}
#highlight2 {
  margin: 0 auto; /* 水平居中 */
  text-align: center;
  font-family: 'Times New Roman', Times, serif;
  text-align: left;
  margin-top: 1rem;
  padding-bottom: 1rem;
  color: black;
  margin-bottom: 0.4rem;
  font-size: 30px;
  font-weight: 700;
  line-height: 1;
  left:50px;
}
/* 设置了底部内边距为 1rem,等于16px;
给元素设置底部外边距为 0.4rem;
这样可以在元素下方留出一定的空白。
设置文本的字体大小为 50 像素。
将文本的字重设置为粗体（700） */
.box2 {
  width: 700px;
  height:600px;
  text-align: center;
  margin:auto;
  padding-top:5px;
  align-items:center;
  font-family: 'Times New Roman', Times, serif;
}
label {
  display: inline-block;
  width: 50px; /* 设置 label 元素的宽度 */
  text-align: right; /* 可选：将 label 文本右对齐 */
  align-items: center;
}
/*form {*/
/*  !* display: flex; *!*/
/*  !* 上述方法设计元素自适应排列 *!*/
/*  border: 1px solid black;*/
/*  flex-direction: column;*/
/*  background: white;*/
/*}*/
.acc1{
  height: 35px;
  width:50%;
  margin-left:20px;
  margin-top:20px;
  margin-bottom:10px ;
  background:rgba(255,255,255,0.4);
  border-radius:25px;
  font-size:18px;
  /*background-image:url("");*/
  background-size:25px;
  background-repeat:no-repeat;
  padding-left:40px;
  border: 1px solid black;
}
.acc2{
  height: 35px;
  width:50%;
  margin-left:20px;
  margin-top:10px;
  margin-bottom:10px ;
  background:rgba(255,255,255,0.4);
  border-radius:25px;
  font-size:18px;
  /*background-image:url("");*/
  background-size:25px;
  background-repeat:no-repeat;
  padding-left:40px;
  border: 1px solid black;
  font-family: 'Times New Roman', Times, serif;
}

.acc3{
  height: auto;
  width:50%;
  margin-left:20px;
  margin-top:10px;
  margin-bottom:10px ;
  background:rgba(255,255,255,0.4);
  border-radius:25px;
  font-size:18px;
  /*background-image:url("");*/
  background-size:25px;
  background-repeat:no-repeat;
  padding-left:40px;
  border: 1px solid black;

}
.submit{
  text-align: center;
  align-items:center;
  margin-top:20px;
  margin-left:20px;
  font-size:20px;
  width:150px;
  height:50px;
  border:2px solid black;
  background-color: rgba(255,255,255,0.4);
  color:#666666;
  border-radius:30px;
  margin-right: 20px;
  margin-bottom: 20px;
  font-family: 'Times New Roman', Times, serif;
}
.submit:hover {
  transform: scale(0.95); /* 缩小按钮 */
  background-color: green; /* 改变背景颜色 */
  color: #333333; /* 改变文字颜色 */
}
.submit:active {
  transform: scale(0.95); /* 缩小按钮 */
  background-color: rgba(255, 255, 255, 0.6); /* 改变背景颜色 */
  color: #333333; /* 改变文字颜色 */
}
::placeholder{
  font-family:'Times New Roman', Times, serif ;
}
label, textarea {
  vertical-align: middle;
}
label, a {
  vertical-align: middle;
}
/* 隐藏原生文本框 */
/* .file[type="file"] {
    display: none;
  } */
.upload_file {
  position: relative;
  display: inline-block;
  width: 40%;
  height: 40px;
  background: white;
  border: 1px solid black;
  border-radius: 4px;
  padding: 4px 12px;
  overflow: hidden;
  color: black;
  text-decoration: none;
  text-indent: 0;
  line-height: 20px;
  margin-left: 20px;
  padding-left: 20px;
}
.upload_file input {
  position: absolute;
  font-size: 100px;
  right: 0;
  top: 0;
  opacity: 0;
}
.upload_file:hover {
  background: #AADFFD;
  border-color: #78C3F3;
  color: #004974;
  text-decoration: none;
}
.flex{
  margin-top: 50px;
}

.el-button{
  font-family: 'Times New Roman', Times, serif;
  font-size: 18px;
}
.el-icon--right{
  size:20px;
}
.custom-input{
  font-family: 'Times New Roman', Times, serif;
  width:400px;
}
.custom-select{
  font-family: 'Times New Roman', Times, serif;
  width:400px;
}
.title{
  text-align: center;
  margin:auto;
  margin-top: 50px;
}
.type{
  text-align: center;
  margin:auto;
  margin-top: 20px;
}
.content{
  text-align: center;
  margin:auto;
  margin-top: 20px;
}
.demo-ruleForm{
  /*text-align: center;*/
  margin:auto;
}
.form-container {
  width:700px;
  display: flex;
  justify-content: center;
  background-color: white;
/*  align-items: center;*/
/*  height: 100vh;*/
}
.upload{
  text-align: center;
  margin:auto;
  margin-top: 20px;
}
.upload-demo{
  width:400px;
  height:auto;
}
/*::placeholder{*/
/*  font-family:'Times New Roman', Times, serif ;*/
/*}*/
</style>