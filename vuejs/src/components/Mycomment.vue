<template>
    <div class="container">
        <div>
            <vs-alert color="warn" v-if="recipes.length === 0">
                <template #title>
                    Empty
                </template>
                There is no Post. 
            </vs-alert>
            <div v-for="recipe in recipes" :key="recipe.id">
                <div class="recipe-item row mt-4">
                    <div class="recipe-image col-md-3">
                        <img :src="recipe.imgPath" alt="Recipe Image" class="img-fluid" style="width: 80%;" />
                    </div>
                    <div class="recipe-details col-md-9">
                        <h4>{{ recipe.recipeName }}</h4>
                        <p>{{ recipe.Steps }}</p>
                        <div class="time-icon">
                            <i class="fa fa-clock-o"></i>
                            {{ recipe.LengthOfTime }}
                        </div>
                        <div class="interactions row">
                            <vs-button class="btn-chat col-md-1" shadow primary>
                                <i class="heart-icon"
                                    :class="{ 'fas fa-heart': recipe.isLiked, 'far fa-heart': !recipe.isLiked }"
                                    style="color: #e84133;" @click="toggleLike(recipe)"></i>{{ recipe.likeCount }}
                            </vs-button>

                            <vs-button class="btn-chat col-md-1" shadow primary>
                                <i :class="{ 'fas fa-star': recipe.isFavorite, 'far fa-star': !recipe.isFavorite }"
                                    style="color: #e84133;" @click="toggleFavorite(recipe)"></i>{{ recipe.favoriteCount }}
                            </vs-button>
                            <vs-button class="btn-chat col-md-1" shadow primary>
                                <i class="fa-regular fa-comment"></i>
                                <span class="span">
                                    {{ recipe.commentCount }}
                                </span>
                            </vs-button>
                        </div>
                        <button class="btn btn-primary" @click="showRecipeDetail(recipe.recipe_id)">Show Details</button>
                    </div>
                    <div class="row mt-2">
                    <h2>My Comments</h2>
                    <ul>
                        <div v-for="(comment, index) in recipe.comments" :key="index">
                            {{ comment.user_id }}: {{ comment.comment }}
                        </div>
                        <hr>
                    </ul>
                </div>
                </div>
                
            </div>
        </div>
    </div>
</template>
  
<script>
import { likeRecipeApi, unlikeRecipeApi, favoriteRecipeApi, unfavoriteRecipeApi, usercommentRecipeApi } from '../api/meal'
// import { getAdminRecipe } from '../api/meal'
export default {
    data() {
        return {
            username: localStorage.getItem('username'),
            recipes: [], // 存放菜谱数据的数组
        };
    },
    mounted() {
        // 使用POST请求从后端获取菜谱数据，你可以使用axios或其他HTTP库
        this.fetchRecipes();
    },
    methods: {
        toggleLike(recipe) {
            // 处理点赞操作
            // 发送请求更新服务器上的点赞信息
            console.log(this.username, recipe.recipe_id)
            recipe.isLiked = !recipe.isLiked;
            if (recipe.isLiked) {
                likeRecipeApi(recipe.recipe_id, this.username).then(response => {
                    console.log(response)
                    recipe.likeCount += 1
                }).catch(error => {
                    // this.$Message.error(error.status)
                    console.log(error)
                })
            } else {
                unlikeRecipeApi(recipe.recipe_id, this.username).then(response => {
                    console.log(response)
                    recipe.likeCount -= 1
                }).catch(error => {
                    // this.$Message.error(error.status)
                    console.log(error)
                })

            }

        },
        toggleFavorite(recipe) {
            // 处理收藏操作
            // 发送请求更新服务器上的收藏信息
            console.log(this.username, recipe.recipe_id)
            recipe.isFavorite = !recipe.isFavorite;
            if (recipe.isFavorite) {
                favoriteRecipeApi(recipe.recipe_id, this.username).then(response => {
                    console.log(response)
                    recipe.favoriteCount += 1
                }).catch(error => {
                    // this.$Message.error(error.status)
                    console.log(error)
                })
            } else {
                unfavoriteRecipeApi(recipe.recipe_id, this.username).then(response => {
                    console.log(response)
                    recipe.favoriteCount -= 1
                }).catch(error => {
                    // this.$Message.error(error.status)
                    console.log(error)
                })
            }

        },
        fetchRecipes() {
            // 发送POST请求，获取菜谱数据
            // 请根据你的后端接口配置进行调整

            usercommentRecipeApi(this.username).then(response => {
                console.log(response.data)
                this.recipes = response.data
            }).catch(error => {
                // this.$Message.error(error.status)
                console.log(error)
            })
        },
        showRecipeDetail(recipeId) {
            // 导航到菜谱详情页面，你可以使用Vue Router
            localStorage.setItem('current_id', recipeId)
            console.log(recipeId)
            this.$router.push({ path: "/showRecipe" });
        },
    },
};
</script>
  
<style scoped>
.recipe-item {
    border: 1px solid #716641;
    margin: 10px;
    padding: 10px;
    border-radius: 10px;
}

.recipe-image img {
    max-width: 100%;
}

.time-icon {
    display: flex;
    align-items: center;
}

.btn-primary {
    float: right;
    background-color: #f39120;
    border: none;
}

.btn-primary:hover {
    background-color: #f39120;
    /* 鼠标悬停时改变背景颜色 */
    border: #f2cca0;
}
</style>
  </template>
  