<template>
    <div class="container h-100"  style="margin-top: 100px;">
      <div class="row h-100 justify-content-center align-items-center">
        <div class="col-md-6">
          <h2 class="text-center">Register</h2>
          <form >
            <div class="form-group">
              <label for="username">username:</label>
              <input type="text" class="form-control" id="username" v-model="formData.username" required>
            </div>
            <div class="form-group">
              <label for="password">password:</label>
              <input type="password" class="form-control" id="password" v-model="formData.password" required>
            </div>
            <div style="text-align: center;margin-top: 30px;">
            <button type="submit" class="btn btn-primary btn-block" @click="register">Register</button>
          </div>
          </form>
          <div class="text-center mt-2">
            Already have an Account?<router-link to="/login">Login</router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  
  <script>
  import {RegisterRequest} from '../api/user'
  export default {
    data() {
      return {
        formData: {
          username: '',
          password: '',
        },
      };
    },
    methods: {
      register() {
        console.log('aaaa')
        RegisterRequest(this.formData.username, this.formData.password).then(response => {
            console.log(response)
            this.$router.push({path: '/login'});
            this.$vs.notification({
                          color:'warn',
                          title: 'Message',
                          text: `Register Success!`
                        })
        }).catch(error => {
            // this.$Message.error(error.status)
            console.log(error)
            this.$vs.notification({
                          color:'danger',
                          title: 'Message',
                          text: `Username already exists!`
                        })
        })
      },
    },
  };
  </script>

<style>
.btn-primary {
    background-color: #f09a39;
    border: none;
    outline: none;
}

.btn-primary:hover {
    background-color: #f39120;
    /* 鼠标悬停时改变背景颜色 */
    border: #f2cca0;
}
.form-control:focus {
    border-color: #cc7d25;
    box-shadow: 0 0 0 0.2rem rgba(204, 125, 37, 0.25);
}

</style>
  