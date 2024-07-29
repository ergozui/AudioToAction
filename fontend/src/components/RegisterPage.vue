<template>
  <div className="home">
    <div className="container">
      <h1>register</h1>
      <div className="box">
        <form action="" name="form1" method="post" ref="myForm" @submit="handleFormSubmit">
          <div className="form-group">
            <label>Username</label>
            <input className="acc" type="text" placeholder="Please enter your username" name="username"
                   v-model="formData.username">
          </div>
          <div className="form-group">
            <label>Password</label>
            <input className="acc" type="password" placeholder="Please enter your password" name="password"
                   v-model="formData.password">
          </div>
          <div className="form-group">
            <label>Confirm</label>
            <input className="acc" type="password" placeholder="Please confirm your password" name="confirmPassword"
                   v-model="formData.confirmPassword">
          </div>
          <input className="submit" type="submit" name="submit" value="Submit">
        </form>
        <a href="http://localhost:8080/loginPage">Already have an account? Click to redirect to the login page.</a>
      </div>
    </div>
  </div>
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
      confirmPassword: ''
    });
    const router = useRouter();

    const handleFormSubmit = (event) => {
      event.preventDefault();

      const password = formData.value.password;
      const confirmPassword = formData.value.confirmPassword;

      if (password !== confirmPassword) {
        open5();
        return;
      }

      const formDataValue = new FormData(event.target);
      axios.post('http://localhost:5000/register', formDataValue)
          .then(response => {
            console.log(response.data);
            if (response.data.state === 'success') {
              open2();
              router.push('/loginPage');
            }
            else if(response.data.state === 'Username already registered'){
              open6();
              return;

            }
            else{
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
        message: 'Passwords do not match. Please try again.',
        type: 'error',
      });
    };

    const open2 = () => {
      ElMessage({
        showClose: true,
        message: 'Registration successful!',
        type: 'success',
      });
    };
    const open6 = () => {
      ElMessage({
        showClose: true,
        message: 'Username already registered',
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
.home {
  height: 700px;
}

.container {
  width: 600px;
  height: 400px;
  margin-top: 15vh;
  margin-left: auto;
  margin-right: auto;
  background: white;
  border-radius: 1.5rem;
  font-size: 20px;
  border: 2px solid black;
  text-align: center;
  font-family: 'Times New Roman', Times, serif;
}

.box {
  text-align: center;
  width: 70%;
  margin: auto;
  padding-top: 5px;
  align-items: center;
}

.box2 {
  margin-top: 10px;
}

.acc {
  height: 40px;
  width: 55%;
  margin-left: 20px;
  margin-top: 10px;
  margin-bottom: 10px;
  border: 2px solid black;
  background: rgba(255, 255, 255, 0.4);
  border-radius: 25px;
  font-size: 18px;
  background-size: 25px;
  background-repeat: no-repeat;
  padding-left: 40px;
}

a {
  text-decoration: none;
  color: #666666;
  font-size: 16px;
}

a:hover {
  color: #409EFF;
}

.submit {
  text-align: center;
  margin-top: 20px;
  font-size: 20px;
  width: 130px;
  height: 50px;
  border: 2px solid black;
  background-color: rgba(255, 255, 255, 0.4);
  color: #666666;
  border-radius: 30px;
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

::placeholder {
  font-family: 'Times New Roman', Times, serif;
}
</style>