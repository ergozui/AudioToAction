<template>
  <div class="common-layout">
    <img alt="Vue logo" src="@/assets/logo.png" class="logo">
    <el-container>
      <el-header height="100px" class="header">
        <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
          <el-tab-pane label="Home" name="Home" value="Home">
            <template #label>
              <span class="custom-tabs-label">
                <el-icon><House /></el-icon>
                <span>Home</span>
              </span>
            </template>
          </el-tab-pane>
          <el-tab-pane label="History" name="History" value="History">
            <template #label>
              <span class="custom-tabs-label">
                <el-icon><Timer /></el-icon>
                <span>History</span>
              </span>
            </template>
          </el-tab-pane>
          <el-tab-pane label="User" name="User" value="User">
            <template #label>
              <span class="custom-tabs-label">
                <el-icon><User /></el-icon>
                <span>User</span>
              </span>
            </template>
          </el-tab-pane>
        </el-tabs>
      </el-header>
      <el-main class="main">
        <router-view></router-view>
      </el-main>
      <el-footer class="footer">
        <div class="footer_font"> Copy right @Audio To Action <a href="#" @click="openGDPRPopup" class="GDPR">View our GDPR statement</a></div>
      </el-footer>
    </el-container>
    <el-dialog v-model="dialogVisible" title="GDPR Statement" center :append-to-body="true" class="dialog">
      In today's digital age, privacy is a paramount concern.  As you navigate our website, we want you to feel confident that your personal information is safeguarded.  Hence, we've developed a GDPR Privacy Policy to outline how we collect, use, and protect your data.<br><br>

      When you interact with our website, we may gather certain information, such as your name, email address, and technical details like IP addresses.  Rest assured, this data is collected with your explicit consent and solely for legitimate purposes.<br><br>

      Your privacy is our priority, and we take stringent measures to ensure the security of your personal data.  While we implement robust security protocols, including encryption and firewalls, it's important to note that no system is entirely immune to potential risks.<br><br>

      We are committed to transparency in our data practices.  We do not sell or trade your personal information to third parties without your explicit consent.  However, there may be instances where we need to share data with service providers or comply with legal obligations.<br><br>

      Your rights regarding your personal data are paramount.  You have the right to access, rectify, or delete your information.  Additionally, you can object to or restrict the processing of your data as necessary.<br><br>

      Our use of cookies enhances your browsing experience by customizing content and improving functionality.  You have the option to manage cookie settings in your browser according to your preferences.<br><br>

      As part of our commitment to transparency, this Privacy Policy may undergo updates periodically.  We encourage you to review it regularly for any changes.<br><br>

      Should you have any questions or concerns about our GDPR Privacy Policy, please don't hesitate to reach out to us.  Your trust is essential to us, and we're dedicated to ensuring the protection of your privacy every step of the way.<br><br>

      Thank you for entrusting us with your information.
    </el-dialog>
  </div>
</template>

<script setup>
import { ref,onBeforeMount,watch,onMounted} from 'vue'
import { useRouter } from 'vue-router'
const activeName = ref('Home')
const dialogVisible = ref(false)

const router = useRouter()
onBeforeMount(() => {
  router.beforeEach((to) => {
    activeName.value = to.name
  })
})

// 监听 activeName 的变化
watch(activeName, (newValue) => {
  switch (newValue) {
    case 'Home':
      router.push('/');
      break;
    case 'History':
      router.push('/historyPage');
      break;
    case 'User':
      router.push('/UserInfo');
      break;
      // default:
      //   router.push('/');
      //   break;
  }
});
// onMounted(() => {
//   console.log(activeName.value)
// })
const openGDPRPopup = () => {
  dialogVisible.value = true
}
onMounted(() => {
  document.body.style.setProperty('--el-color-primary', 'black');
  // document.body.style.setProperty('--el-color-primary-light-9', '#F5FBF0');
  // document.body.style.setProperty('--el-color-primary-light-3', '#95d475');
})
</script>

<style>
.demo-tabs > .el-tabs__content {
  --el--tabs--bg--color: black;

  padding: 0px;
  color: black;
  font-size: 50px;
  font-weight: 600;
}
.header {
  font-family: 'Times New Roman', Times, serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 60px;
  background: #f2f3f5;
}
.logo {
  width: 120px;
  height: 70px;
  position: absolute;
  top: 15px;
  left: 50px;
}
.footer {
  text-align: center;
  left: 0;
  width: 100%;
  background: #303133;
  color: white;
  font-family: 'Times New Roman', Times, serif;
}
.main {
  min-height: 750px;
  background: #f2f3f5;
}
.footer_font {
  padding: 20px;
}
.GDPR {
  margin-left: 30px;
  color: #409EFF;
}
.common-layout {
}
.dialog{
  width: auto;
  height:auto;
  font-family: 'Times New Roman', Times, serif;
  font-size: 30px;
}
</style>