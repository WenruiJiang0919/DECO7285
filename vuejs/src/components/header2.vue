
<template>
    <div class="center examplex">
      <vs-navbar center-collapsed v-model="active">
        <template #left>
          <img src="/logo2.png" alt="">
        </template>
        <vs-navbar-item :active="$route.name === 'home'" id="License">
            <router-link to="/home" class="nav-link">Home</router-link>
        </vs-navbar-item>
        <vs-navbar-item :active="$route.name === 'recipe'" id="License">
            <router-link to="/recipe" class="nav-link">Recipe</router-link>
        </vs-navbar-item>
        <vs-navbar-item :active=" $route.name === 'community'" id="License">
            <router-link to="/community" class="nav-link">Community</router-link>
        </vs-navbar-item>
        <vs-navbar-item :active="$route.name === 'newmeal'" id="License">
            <router-link to="/newmeal" class="nav-link">New Meal</router-link>
        </vs-navbar-item>

        <template #right>
          <vs-button flat >Login</vs-button>
          <vs-button>Get Started</vs-button>
        </template>
      </vs-navbar>
      <div class="square">
        <div class="child">
          child 1
        </div>
        <div class="child">
          child 2
        </div>
        <div class="child">
          child 3
        </div>
      </div>
    </div>
  </template>
<script>
  export default {
    data:() => ({
      active: 'guide'
    })
  }
  </script>
  <style>
.vs-navbar-content{
    background-color: #fff8ed;
}
</style>

        