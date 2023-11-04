<template>
    <div class="container ml-4" style="width: 80%;margin-top: 20px;">
        <div class="">
            <div class="">
                <div>
                    <div style="text-align: center;margin-top: 20px;padding: 10px;">
                        <h2>{{ recipe.recipeName }}</h2>
                        <div class="recipe-image mt-4">
                            <img :src="recipe.imgPath" alt="Recipe Image" class="img-fluid" style="height: 300px;" />
                        </div>



                        <div class="">
                            <h4 class="mt-2 ml-2">
                                <i class="fa fa-clock-o"> </i>
                                {{ recipe.LengthOfTime }}
                            </h4>
                        </div>
                    </div>
                    <h4>Description</h4>
                    <p>{{ recipe.Description }}</p>
                    <h4>Ingredients</h4>
                    <p>{{ recipe.Ingredients }}</p>
                    <h4>Steps</h4>
                    <p>{{ recipe.Steps }}</p>
                    <div class="interactions">
                        <vs-button class="btn-chat" shadow primary>
                            <i class="heart-icon"
                                :class="{ 'fas fa-heart': recipe.isLiked, 'far fa-heart': !recipe.isLiked }"
                                style="color: #e84133;" @click="toggleLike(recipe)"></i>
                                <span class="span">
                                {{ recipe.likeCount }}
                            </span>
                        </vs-button>
                        <vs-button class="btn-chat" shadow primary>
                            <i :class="{ 'fas fa-star': recipe.isFavorite, 'far fa-star': !recipe.isFavorite }"
                                style="color: #e84133;" @click="toggleFavorite(recipe)"></i>
                                <span class="span">
                                    {{ recipe.favoriteCount }}
                            </span>
                        </vs-button>
                        <!-- <div class="interaction">
                            <i class="fa" :class="{ 'fa-heart': !recipe.isFavorite, 'fa-heart liked': recipe.isFavorite }"
                                @click="toggleFavorite"></i>
                            
                        </div> -->

                    </div>
                    <div class="comments">
                        <h3>Comments</h3>
                        <ul>
                            <div v-for="(comment, index) in recipe.comments" :key="index" class="comment-item">
                                <h5>username:{{ comment.user_id }}</h5>
                                {{ comment.comment }}
                            </div>
                        </ul>
                    </div>
                    <div class="comment-input" style="text-align: center;">
                        <div class="form-group">
                            <textarea v-model="newComment" rows="4" class="form-control"
                                placeholder="Add your comment"></textarea>
                        </div>
                        <button @click="addComment" class="btn btn-primary custom-button ">Submit</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import { getShowRecipeApi, commentRecipeApi, likeRecipeApi, unlikeRecipeApi,favoriteRecipeApi,unfavoriteRecipeApi } from '../api/meal'
export default {
    data() {
        return {
            username: localStorage.getItem('username'),
            recipe_id: localStorage.getItem('current_id'),
            newComment:'',
            recipe: {}
            // recipe: {
            //     "recipe_id": 10,
            //     "Cuisine": "亚洲菜",
            //     "Description": "no Description",
            //     "Ingredients": "(8 rolls)\n8 sheets of Vietnamese rice paper\n1 egg\nSausage and prawns\nLettuce, purple kale, colorful peppers\n(Southeast Asian peanut flavor sauce)\n2 tablespoons of peanut butter\n1 tablespoon of soy sauce\n1 tbsp rice vinegar\n4 tbsp water\n½ tbsp honey or 1 tbsp\nWhite sesame seeds",
            //     "LengthOfTime": "25 minutes",
            //     "Steps": "1. Prepare vegetables by washing and cutting into small strips or shreds\n2. Egg meat fried or boiled\n3. Prepare a bowl of water, take a piece of rice paper dipped in water, lay flat on the plate,\nin order to code on the favorite ingredients\n4. Bottom turn up and roll the ingredients, fold the sides inward a little, and then\nRoll up from bottom to top\n5. Dip all the ingredients into the mixture, mix well to mix",
            //     "commentCount": 0,
            //     "comments": [],
            //     "favoriteCount": 0,
            //     "imgPath": "./uploads/图片0.jpg",
            //     "isFavorite": false,
            //     "isLiked": false,
            //     "likeCount": 0,
            //     "recipeName": "Vietnamese Spring Roll"
            // },
        };
    },
    created() {
        getShowRecipeApi(this.username, this.recipe_id).then(response => {
            console.log(response.data)
            this.recipe = response.data
        }).catch(error => {
            // this.$Message.error(error.status)
            console.log(error)
        })
    },
    methods: {
        addComment() {
            // 将新评论提交给后端保存
            // 这里你需要实现向后端发送评论数据的逻辑
            // 成功后将评论添加到 recipe.comments 数组中
            const commentText = this.newComment.trim();
            if (commentText) {
                // 创建评论对象
                const newComment = {
                    text: commentText,
                };
                console.log(commentText)
                commentRecipeApi(this.recipe_id, this.username, commentText).then(response => {
                    console.log(response)
                }).catch(error => {
                    // this.$Message.error(error.status)
                    console.log(error)
                })
                let new_record={
                    'user_id':this.username,
                    'comment':newComment.text
                }
                this.recipe.comments.push(new_record);
                // 清空输入框
                this.newComment = '';
            }
        },
        toggleLike() {
            // 处理点赞操作
            // 发送请求更新服务器上的点赞信息
            console.log(this.username, this.recipe_id)
            this.recipe.isLiked = !this.recipe.isLiked;
            if (this.recipe.isLiked) {
                likeRecipeApi(this.recipe.recipe_id, this.username).then(response => {
                    console.log(response)
                    this.recipe.likeCount+=1
                }).catch(error => {
                    // this.$Message.error(error.status)
                    console.log(error)
                })
            } else {
                unlikeRecipeApi(this.recipe.recipe_id, this.username).then(response => {
                    console.log(response)
                    this.recipe.likeCount-=1
                }).catch(error => {
                    // this.$Message.error(error.status)
                    console.log(error)
                })

            }

        },
        toggleFavorite() {
            // 处理收藏操作
            // 发送请求更新服务器上的收藏信息
            console.log(this.username, this.recipe_id)
            this.recipe.isFavorite = !this.recipe.isFavorite;
            if (this.recipe.isFavorite) {
                favoriteRecipeApi(this.recipe_id, this.username).then(response => {
                    console.log(response)
                    this.recipe.favoriteCount+=1
                }).catch(error => {
                    // this.$Message.error(error.status)
                    console.log(error)
                })
            } else {
                unfavoriteRecipeApi(this.recipe_id, this.username).then(response => {
                    console.log(response)
                    this.recipe.favoriteCount-=1
                }).catch(error => {
                    // this.$Message.error(error.status)
                    console.log(error)
                })
            }

        },
    },
};
</script>
  
<style scoped>
.recipe-image img {
    max-width: 100%;
}

.time-icon {
    display: flex;
    align-items: center;
}

.interactions {
    display: flex;
    justify-content: left;
    margin-top: 10px;
}

.interaction {
    display: flex;
    align-items: center;
}

.fa {
    font-size: 24px;
    cursor: pointer;
    transition: color 0.3s;
}

.fa.liked {
    color: red;
    /* 设置点赞和收藏的高亮颜色 */
}

.comments {
    margin-top: 20px;
}

.comment-item {
    margin-bottom: 10px;
    padding: 10px;
    border-bottom: 1px solid #ccc;
}

.comment-input {
    margin-top: 20px;
}

textarea {
    width: 100%;
}

.btn-primary {
    margin-top: 10px;
}

/* 自定义输入框的点击高亮颜色 */
.form-control:focus {
    border-color: #cc7d25;
    box-shadow: 0 0 0 0.2rem rgba(204, 125, 37, 0.25);
}

/* 去除按钮的边框 */
.custom-button {
    background-color: #f09a39;
    border: none;
    outline: none;
}

.custom-button:hover {
    background-color: #f39120;
    /* 鼠标悬停时改变背景颜色 */
    border: #f2cca0;
}
</style>
  </template>
  