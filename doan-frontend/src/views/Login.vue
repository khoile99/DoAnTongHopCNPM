<template>
  <main>
    <div class="login-form">
      <form @submit.prevent v-on:keyup.enter="signIn">
        <h1>Login</h1>
        <div class="content">
          <div class="input-field">
            <input type="email" placeholder="Email" name="email" v-model="form.email">
          </div>
          <div class="input-field">
            <input type="password" placeholder="Password" name="password" v-model="form.password">
          </div>
          <a href="#" class="link">Forgot Your Password?</a>
        </div>
        <div class="action">
          <button>Register</button>
          <button @click="signIn">Sign in</button>
        </div>
      </form>
    </div>
  </main>
</template>

<script setup>
import { reactive } from "vue"
import HTTPService from "@/common/HTTP"
import LocalStorageWorker from "@/common/storageHelper"
import router from "@/router/index"
let form = reactive({ email: "", password: "" })

async function signIn() {
  let response = await HTTPService.login(form)
  if (response.status === 200) {
    LocalStorageWorker.setToken(response.data.token)
    router.push('/dashboard')
  } else {
    alert(response.data.message)
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
}

.login-form {
  background: #fff;
  width: 500px;
  margin: 0 auto;
  display: -webkit-box;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  flex-direction: column;
  border-radius: 4px;
  box-shadow: 0 2px 25px rgba(0, 0, 0, 0.2);
}

.login-form h1 {
  padding: 35px 35px 0 35px;
  font-weight: 300;
}

.login-form .content {
  padding: 35px;
  text-align: center;
}

.login-form .input-field {
  padding: 12px 5px;
}

.login-form .input-field input {
  font-size: 16px;
  display: block;
  font-family: 'Rubik', sans-serif;
  width: 100%;
  padding: 10px 1px;
  border: 0;
  border-bottom: 1px solid #747474;
  outline: none;
  -webkit-transition: all .2s;
  transition: all .2s;
}

.login-form .input-field {
  padding: 12px 5px;
}

.login-form a.link {
  text-decoration: none;
  color: #747474;
  letter-spacing: 0.2px;
  text-transform: uppercase;
  display: inline-block;
  margin-top: 20px;
}

.login-form .input-field input {
  font-size: 16px;
  display: block;
  font-family: 'Rubik', sans-serif;
  width: 100%;
  padding: 10px 1px;
  border: 0;
  border-bottom: 1px solid #747474;
  outline: none;
  -webkit-transition: all .2s;
  transition: all .2s;
}

.login-form .action {
  display: -webkit-box;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
  flex-direction: row;
}

.login-form .action button {
  width: 100%;
  border: none;
  padding: 18px;
  font-family: 'Rubik', sans-serif;
  cursor: pointer;
  text-transform: uppercase;
  background: #e8e9ec;
  color: #777;
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 0;
  letter-spacing: 0.2px;
  outline: 0;
  -webkit-transition: all .3s;
  transition: all .3s;
}

.login-form .action button:nth-child(2) {
  background: #2d3b55;
  color: #fff;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 4px;
}
</style>

<style>
body {
  background: url('@/assets/bg-img.jpg');
  background-repeat: round;
}

#app {
  padding-top: 65px;
}
</style>
