<template>
    <div class="container" style="background-color: #fff8ed;">
      <div v-for="(group, cuisine) in pagedRecipeGroups" :key="cuisine">
        <h3>{{ cuisine }}</h3>
        <div class="row">
          <div class="col-3" v-for="recipe in group" :key="recipe.recipeName">

          </div>
        </div>

        <paginate :page-count="pageCount" :click-handler="changePage" :prev-text="'上一页'" :next-text="'下一页'"></paginate>
      </div>
    </div>
  </template>
  
  <script>
  import Paginate from 'vuejs-paginate';
  import {fetchRecipesBycuision} from '../api/meal'
  export default {
    name:'communty',
    components: {
      Paginate,
    },
    data() {
      return {
        recipeGroups: {}, // 所有菜谱信息
        username: "admin", // 当前用户的用户名，可以根据需要修改
        perPage: 5, // 每页显示的菜谱数量
        currentPage: 1, // 当前页数
      };
    },
    computed: {
      pagedRecipeGroups() {
        // 分页显示菜谱信息
        const start = (this.currentPage - 1) * this.perPage;
        const end = this.currentPage * this.perPage;
        const pagedGroups = {};
  
        for (const cuisine in this.recipeGroups) {
          pagedGroups[cuisine] = this.recipeGroups[cuisine].slice(start, end);
        }
  
        return pagedGroups;
      },
      pageCount() {
        // 计算总页数
        const totalRecipes = Object.values(this.recipeGroups).reduce((total, group) => total + group.length, 0);
        return Math.ceil(totalRecipes / this.perPage);
      },
    },
    methods: {
      // 获取菜谱信息并填充到this.recipeGroups中
      fetchRecipes() {
        // 发送POST请求来获取菜谱信息
        const data = { username: this.username };
        fetchRecipesBycuision(data).then(response => {
            console.log(response)
            this.recipeGroups=response.data
        }).catch(error => {
            // this.$Message.error(error.status)
            console.log(error)
        })
      },
      changePage(page) {
        this.currentPage = page;
      },
      // ...其它方法...
    },
  };
  </script>
  
  <style>
  /* 在此添加自定义样式 */
  </style>
  