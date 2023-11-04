
<template>
    <div class="hidden" style="margin-top: 10px;">
        <div>
            <vs-sidebar v-model="active" open>
                <vs-sidebar-item id="MyPost">
                    <template #icon>
                        <i class='bx bx-home'></i>
                    </template>
                    My Post
                </vs-sidebar-item>
                <vs-sidebar-item id="collection">
                    <template #icon>
                        <i class='bx bx-grid-alt'></i>
                    </template>
                    My Collection
                </vs-sidebar-item>
                <vs-sidebar-item id="comment">
                    <template #icon>
                        <i class='bx bxs-music'></i>
                    </template>
                    My Comment
                </vs-sidebar-item>
                <vs-sidebar-item id="userlike">
                    <template #icon>
                        <i class='bx bxs-donate-heart'></i>
                    </template>
                    My Like
                </vs-sidebar-item>

            </vs-sidebar>
        </div>

        <div style="margin-left: 300px;width: 70%;">
            <div style="text-align: center;margin-bottom: 20px;">
                <img class="ml-5" src="http://127.0.0.1:5000/get-image?image_filename=img_user.jpg" alt="user"
                    style="width: 80px;height: 80px;">
                <h4>username: {{ this.username }}</h4>
                <vs-button warn border @click="logOut" style="margin-left: 45%;">
                    Logout
                </vs-button>
            </div>
            <MyPost v-if="this.active === 'MyPost'"></MyPost>
            <UserLike v-if="this.active === 'userlike'"></UserLike>
            <UserCollection v-if="this.active === 'collection'"></UserCollection>
            <MyComment v-if="this.active === 'comment'"></MyComment>
        </div>


    </div>
</template>
<script>
import MyPost from '../components/myPost.vue'
import UserLike from '../components/userLikeRecipe.vue'
import UserCollection from '../components/collection.vue'
import MyComment from '../components/Mycomment.vue'
export default {
    components: {
        MyPost, UserLike, UserCollection, MyComment
    },
    data() {
        return {
            username: localStorage.getItem('username'),
            active: 'MyPost',
        };
    },
    methods: {
        log_c() {
            console.log(this.active);
        },
        logOut(){
            localStorage.removeItem('username')
            this.$router.push({path: '/login'});
            location.reload();
        }
    }
}
</script>
<style>
.vs-sidebar-content {
    top: 120px;

}

.vs-sidebar__item.active.hasIcon {
    color: #cc7d25;
    /* 设置字体颜色为黑色 */
}

.vs-sidebar__item:after {
    background-color: #cc7d25;
    /* 设置 ::after 伪元素的颜色为黑色 */
}
</style>


        