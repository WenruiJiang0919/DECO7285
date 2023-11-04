<template>
    <div class="container" style="background-color: #fff8ed;">

      <!-- 渲染不同Cuisine的菜谱信息 -->
      <CuisineRecipeGroup
      v-for="(group, cuisine) in this.recipeGroups"
      :key="cuisine"
      :cuisineName="cuisine"
      :recipes="group"
    />
    </div>
  </template>
  
  <script>
  import {fetchRecipesBycuision} from '../api/meal'
  import CuisineRecipeGroup from '../components/CuisineRecipeGroup.vue';
  export default {
    components: {
    CuisineRecipeGroup,
  },
    name:'communty',
    data() {
      return {
        recipeGroups: {}, // 用于存储不同Cuisine的菜谱信息
        username: localStorage.getItem('username'), // 当前用户的用户名，可以根据需要修改
      };
    },
    created() {
      // 在页面创建时发送POST请求获取菜谱信息
      this.fetchRecipes();
    },
    methods: {
      fetchRecipes() {
        // 发送POST请求获取菜谱信息
        const data = { username: this.username };
        fetchRecipesBycuision(data).then(response => {
            console.log(response)
            this.recipeGroups=response.data
        }).catch(error => {
            // this.$Message.error(error.status)
            console.log(error)
        })
        // 请在此处添加POST请求的代码，使用Axios或其他HTTP库发送请求
        // 将获取到的菜谱信息存储在this.recipeGroups中
      },
      toggleLike(recipe) {
        // 点赞/取消点赞操作，根据实际情况实现
        // 请发送POST请求来更新服务器上的点赞信息
        recipe.isLiked = !recipe.isLiked;
      },
      toggleFavorite(recipe) {
        // 收藏/取消收藏操作，根据实际情况实现
        // 请发送POST请求来更新服务器上的收藏信息
        recipe.userFavorited = !recipe.userFavorited;
      },
    },
  };
  </script>
  
  <style>
  /* 在此添加自定义样式 */
  </style>
  