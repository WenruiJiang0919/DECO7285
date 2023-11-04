<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-custom">
            <div class="container ">
                <img class="ml-5" src="http://127.0.0.1:5000/get-image?image_filename=logo.png" alt="user" style="width: 100px;height: 100px;">
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="" id="navbarNav" style="width: 80%;height: 100%;margin-top: 30px;">
                    <div class="row justify-content-evenly" style="text-align: center;border-bottom: #cc7d25 2px solid;">
                        <div class="col-2 pt-1"  :class="{ active: $route.name === 'community' }" v-if="hasToken">
                            <h5><router-link to="/community" class="nav-link">Community</router-link></h5>
                        </div>
                        <div class="col-2  pt-1" :class="{ active: $route.name === 'home' }" v-if="!hasToken">
                            <h5><router-link to="/home" class="nav-link">Home</router-link></h5>
                        </div>
                        <div class="col-2  pt-1" :class="{ active: $route.name === 'recipe' }" v-if="hasToken">
                            <h5><router-link to="/recipe" class="nav-link">Recipe</router-link></h5>
                        </div>
                        <div class="col-2  pt-1" :class="{ active: $route.name === 'newmeal' }" v-if="hasToken">
                            <h5><router-link to="/newmeal" class="nav-link">New Meal</router-link></h5>
                        </div>
                    </div>
                    <!-- <ul class="navbar-nav ">
                    <li class="nav-item ml-5 mt-1">
                        <h5>Home</h5>
                    </li>
                    <li class="nav-item ml-5 mt-1">
                        <h5>Restaurant</h5>
                    </li>
                    <li class="nav-item ml-5  mt-1">
                        <h5>Community</h5>
                    </li>
                </ul> -->
                </div>
                <div v-if="hasToken">
                    <router-link to="/Profile" ><img class="ml-5" src="http://127.0.0.1:5000/get-image?image_filename=img_user.jpg" alt="user" style="width: 80px;height: 80px;"></router-link>
                </div>
                <div v-if="!hasToken">
                    <button @click="login" class="btn btn-primary custom-button ">Login</button>
                </div>

            </div>
        </nav>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            hasToken: localStorage.getItem('username') // 根据 localStorage 中的 token 设置此变量
        };
    },
    methods: {
        login() {
            this.$router.push({path: '/login'});
        }
    }
};
</script>

<style lang="less" scoped>
.custom-card {
    border-radius: 15px;
    /* 圆角 */
    margin: 10px;
    /* 图片间距 */
    text-align: center;
}

.custom-card img {
    border-radius: 15px 15px 15px 15px;
    /* 顶部圆角 */
}

.navbar-custom {
    background-color: #fef7ec;
    // color: #dc7f00;
}

.navbar-custom img {
    border-radius: 50%;
    /* 圆形图片 */
    width: 30px;
    height: 30px;
    margin-right: 10px;
    /* 图片右侧的间距 */
}

.center-div {
    display: flex;
    justify-content: center;
    align-items: center;
}

.center-div img {
    border-radius: 50%;
    /* 圆形图片 */
    width: 30px;
    height: 30px;
}

.custom-hr {
    border-top: 2px solid #805619;
    /* 线的颜色和粗细 */
    margin-top: 10px;
    /* 顶部间距 */
    margin-bottom: 20px;
    /* 底部间距 */
}

.radius-div {
    background-color: #fff1cb;
    /* 背景颜色 */
    padding: 20px;
    /* 内边距 */
    border-radius: 10px;
    /* 圆角半径 */
}

.linear-gradient-div {
    background: linear-gradient(to bottom, #fdebb8, #ffffff);
    /* 垂直渐变 */
    padding: 20px;
    /* 内边距 */
}

.custom-progress {
    border-radius: 10px;
    /* 圆角 */
}

.progress-bar {
    background-color: #f5d5b1;
    /* 进度条背景颜色 */
}

.progress-bar-striped {
    background-color: #f3a448;
    /* 进度条颜色 */
    color: black;
    /* 文字颜色 */
}

.collection-button {
    background-color: #f3b659;
    /* 背景颜色 */
    color: white;
    /* 字体颜色 */
    border: none;
    /* 移除边框 */
    border-radius: 10px;
    /* 圆角 */
    padding: 10px 20px;
    /* 内边距 */
}

.slider {
    width: 30px;
    height: 15px;
    background-color: #ffb03a;
    border-radius: 7px;
    position: relative;
}

.slider input[type="checkbox"] {
    opacity: 0;
    width: 0;
    height: 0;
}

.slider label {
    display: block;
    width: 15px;
    height: 15px;
    background-color: #fff;
    border-radius: 50%;
    position: absolute;
    top: 0;
    left: 0;
    transition: all 0.2s ease;
    cursor: pointer;
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

.active {
    border-bottom: #dc7f00 4px solid;
    background-color: #dc7f00;
    border-radius: 3px;
    color: #ffffff;
}</style>
  