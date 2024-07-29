<template>
    <head>
      <meta charset="utf-8">
      <title> Smart Transcript</title>
    </head>
    <body>
    <div class="container">
      <div class="box1">
        <form  action="http://localhost:5000/login" name="form" id="form" method="post" @submit="handleFormSubmit">
          <h1>
            login
          </h1>
          <label>Username<input class="acc" type="text" placeholder="Please enter your username" name="username" ></label>
          <label>Password<input class="acc" type="password" placeholder="Please enter your password" name="password" ></label>
          <input class="submit" type="submit" name="submit" value="submit" >
          <!-- //nbsp提供空格用来对其齐 -->
        </form>
        <div class="box2">
            <form action="" name="form2">
                &nbsp;&nbsp;&nbsp;
                <input  type="checkbox" name="rememberMe" value="true">Remember
                <!-- checbox提供一种小框 -->
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <a href="http://localhost:8080/registerPage">Register</a>
            </form>
        </div>
      </div>
      </div>
    </body>
  </template>

<script>
import {ref} from 'vue';
import {ElMessage} from "element-plus";
import axios from '@/main';
import {useRouter} from 'vue-router';

export default {
  setup() {
    const formData = ref({
      username: '',
      password: '',
    });
    const router = useRouter();

    const handleFormSubmit = (event) => {
      event.preventDefault();

      const formDataValue = new FormData(event.target);
      axios.post('http://localhost:5000/login', formDataValue)
          .then(response => {
            console.log(response.data);
            if (response.data.state === 'success') {
              open2();
              router.push('/');
            }
            else if(response.data.state ==='password error'){
              open5();
              return;
            }
            else if(response.data.state ==='unexist user'){
              open6();
              return;
            }
            else {
              open4();
              return;
            }
          })
          .catch(error => {
            console.error(error);
            open4();
          });
    };

    const open4 = () => {
      ElMessage({
        showClose: true,
        message: 'An error occurred. Please try again.',
        type: 'error',
      });
    };

    const open5 = () => {
      ElMessage({
        showClose: true,
        message: 'Passwords error.',
        type: 'error',
      });
    };

    const open2 = () => {
      ElMessage({
        showClose: true,
        message: 'Login Successful!',
        type: 'success',
      });
    };
    const open6 = () => {
      ElMessage({
        showClose: true,
        message: 'Unexist User.',
        type: 'error',
      });
    };
    return {
      formData,
      handleFormSubmit,
      open4,
      open5,
      open2
    };
  }
};
</script>
<style scoped>
body{
  height:700px;
}

.container{
    width: 600px;
    height: 370px;
    margin-top: 15vh;
    /* 百分比 */
    margin-left:auto;
    margin-right:auto;
    background:white;
    border-radius:1.5rem;
    font-size:20px;
    border:2px solid black;
    font-family: 'Times New Roman', Times, serif;
}

.box1{
    text-align: center;
    width:70%;
    margin:auto;
    padding-top:5px;
    align-items:center;
}
.box2{
    margin-top: 10px;

}
.acc{
    height: 40px;
    width:55%;
    margin-left:20px;
    margin-top:10px;
    margin-bottom:10px ;
    border:2px solid black;
    background:rgba(255,255,255,0.4);
    border-radius:25px;
    font-size:18px;
    /*background-image:url("");*/
    background-size:25px;
    background-repeat:no-repeat;
    padding-left:40px;
}

a{
    text-decoration:none ;
    color:#666666;

}
.submit{
    text-align: center;
    margin-top:20px;
    font-size:20px;
    width:130px;
    height:50px;
    border:2px solid black;
    background-color: rgba(255,255,255,0.4);
    color:#666666;
    border-radius:30px;
    font-family: 'Times New Roman', Times, serif;
}
.submit:hover {
    transform: scale(0.95); /* 缩小按钮 */
    background-color: #409EFF; /* 改变背景颜色 */
    color: #333333; /* 改变文字颜色 */
}
.submit:active {
    transform: scale(0.95); /* 缩小按钮 */
    background-color: #409EFF; /* 改变背景颜色 */
    color: #333333; /* 改变文字颜色 */
}
::placeholder{
  font-family: 'Times New Roman', Times, serif;
}
a:hover{
    color: #409EFF;
}
</style>