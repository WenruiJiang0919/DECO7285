<template>
    <div class="container h-100" style="margin-top: 100px;">
      <div class="row h-100 justify-content-center align-items-center">
        <div class="col-md-6">
          <h2 class="text-center">Login</h2>
          <form >
            <div class="form-group">
              <label for="username">username:</label>
              <input type="text" class="form-control" id="username" v-model="formData.username" required>
            </div>
            <div class="form-group">
              <label for="password">password:</label>
              <input type="password" class="form-control" id="password" v-model="formData.password" required>
            </div>
            <div style="text-align: center;margin-top: 10px;">
              <button type="submit" class="btn btn-primary" @click="handleSubmit" style="background-color:#f39120 ;">Login</button>
            </div>
            
          </form>
          <div class="text-center mt-2">
            Don't have account<router-link to="/register">Register</router-link>
          </div>
        </div>
      </div>
    </div>
</template>
<script>
import {LoginRequest} from '../api/user'
export default {
    name: 'login',
    data() {
        return {
            formData: {
          username: '',
          password: '',
        },
        }
    },
    methods: {
        handleSubmit() {
            LoginRequest(this.formData.username, this.formData.password).then(response => {
                        console.log(response.data.access_token,response)
                        localStorage.setItem('token',response.data.access_token)
                        localStorage.setItem('username',this.formData.username)
                        
                        this.$vs.notification({
                          color:'warn',
                          title: 'Message',
                          text: `Login Success`
                        })
                        this.$router.push({path: '/recipe'});
                        location.reload();
                    }).catch(error => {
                        // this.$Message.error(error.status)
                        console.log(error)
                        this.$vs.notification({
                          color:'danger',
                          title: 'Message',
                          text: `Login Error! Check username and password!`
                        })
                    })
        }
    }
}
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