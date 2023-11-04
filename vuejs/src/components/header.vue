<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">
        <i class="fas fa-icon-name"></i> <!-- 替换为你的图标 -->
      </a>
  
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item" :class="{ active: $route.name === 'home' }">
            <router-link to="/home" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item" :class="{ active: $route.name === 'recipe' }" v-if="hasToken">
            <router-link to="/recipe" class="nav-link">Recipe</router-link>
          </li>
          <li class="nav-item" :class="{ active: $route.name === 'community' }" v-if="hasToken">
            <router-link to="/community" class="nav-link">Community</router-link>
          </li>
          <li class="nav-item" :class="{ active: $route.name === 'newmeal' }" v-if="hasToken">
            <router-link to="/new-meal" class="nav-link">New Meal</router-link>
          </li>
        </ul>
      </div>
  
      <div class="navbar-text" v-if="!hasToken">
        <button @click="login" class="btn btn-primary">Login</button>
      </div>
  
      <div class="navbar-text" v-else>
        <img src="user-avatar.png" alt="User Avatar" class="user-avatar">
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    data() {
      return {
        hasToken: true // 根据 localStorage 中的 token 设置此变量
      };
    },
    methods: {
      login() {
        // 处理登录逻辑
      }
    }
  };
  </script>

<style lang="less" scoped>
#active{
    background-color: aqua;
}
</style>
  