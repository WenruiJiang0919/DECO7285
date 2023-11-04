<template>
    <div style="text-align: center;">
      <h3>{{ cuisineName }}</h3>
      
      <vs-card-group>
    <vs-card v-for="(recipe, index) in pagedRecipes" :key="recipe.recipeName" @click="jump(recipe.recipe_id)">
      <template #title>
        <h3>{{ recipe.recipeName }}</h3>
      </template>
      <template #img>
        <img :src="recipe.imgPath" alt="">
      </template>
      <template #text>
        <p>
          Lorem ipsum dolor sit amet consectetur, adipisicing elit.
        </p>
      </template>
      <template #interactions>

        <vs-button class="btn-chat" shadow primary>
          <i
                class="heart-icon"
                :class="{'fas fa-heart': recipe.isLiked, 'far fa-heart': !recipe.isLiked}"
                style="color: #e84133;"
                @click="toggleLike(recipe)"
              ></i>
        </vs-button>

              <vs-button class="btn-chat" shadow primary>
                <i
                :class="{'fas fa-star': recipe.userFavorited, 'far fa-star': !recipe.userFavorited}"
                style="color: #e84133;"
                @click="toggleFavorite(recipe)"
              ></i>
        </vs-button>
        <!-- <vs-button class="btn-chat" shadow primary>
          <i class="fa-regular fa-comment"></i>
          <span class="span">
            {{ recipe.commentCount }}
          </span>
        </vs-button> -->
      </template>
    </vs-card>
  </vs-card-group>

    </div>
  </template>
  
  <script>
  import {likeRecipeApi,unlikeRecipeApi,favoriteRecipeApi,unfavoriteRecipeApi} from '../api/meal'
  export default {
    props: {
      cuisineName: String,
      recipes: Array,
    },
    data() {
      return {
        username:localStorage.getItem('username'),
        currentPage: 1,
        itemsPerPage: 5,
      };
    },
    computed: {
      pagedRecipes() {
        const start = (this.currentPage - 1) * this.itemsPerPage;
        const end = start + this.itemsPerPage;
        return this.recipes.slice(start, end);
      },
      totalPages() {
        return Math.ceil(this.recipes.length / this.itemsPerPage);
      },
    },
    methods: {
      jump(recipeId){
        localStorage.setItem('current_id', recipeId)
            console.log(recipeId)
            this.$router.push({ path: "/showRecipe" });
      },
      toggleLike(recipe) {
        // 处理点赞操作
        // 发送请求更新服务器上的点赞信息
        console.log(this.username,recipe.recipe_id)
        recipe.isLiked = !recipe.isLiked;
        if (recipe.isLiked){
          likeRecipeApi(recipe.recipe_id,this.username).then(response => {
                        console.log(response)
                    }).catch(error => {
                        // this.$Message.error(error.status)
                        console.log(error)
                    })
        }else{
          unlikeRecipeApi(recipe.recipe_id,this.username).then(response => {
                        console.log(response)
                    }).catch(error => {
                        // this.$Message.error(error.status)
                        console.log(error)
                    })

        }
        
      },
      toggleFavorite(recipe) {
        // 处理收藏操作
        // 发送请求更新服务器上的收藏信息
        console.log(this.username,recipe.recipe_id)
        recipe.userFavorited = !recipe.userFavorited;
        if(recipe.userFavorited){
          favoriteRecipeApi(recipe.recipe_id,this.username).then(response => {
                        console.log(response)
                    }).catch(error => {
                        // this.$Message.error(error.status)
                        console.log(error)
                    })
        }else{
          unfavoriteRecipeApi(recipe.recipe_id,this.username).then(response => {
                        console.log(response)
                    }).catch(error => {
                        // this.$Message.error(error.status)
                        console.log(error)
                    })
        }

      },
      goToPage(page) {
        if (page >= 1 && page <= this.totalPages) {
          this.currentPage = page;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* 在此添加自定义样式 */
  /* .heart-icon,
  .star-icon {
    font-size: 24px;
    cursor: pointer;
    margin: 5px;
  } */
  </style>
  