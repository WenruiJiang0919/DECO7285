<template>
    <div id="app" style="background-color: #fef7ec;">
        <Header ></Header>
        <router-view></router-view>
    </div>
</template>

<script>
import Header from './components/header3'
export default {
    name: 'app',
    components: { Header },
    data() {
        return {
            
        }
    },
    methods: {

    }
}
</script>

<style lang="less" scoped>
#app {
    min-height: 100vh; /* 设置最小高度为视口高度的100% */
}
</style>

