import Vue from 'vue'
import Router from 'vue-router'
import Index from '../views/index'
import Login from '../views/login'
import Register from '../views/register'
import Recipe from '../views/recipe'
import Community from '../views/community'
import Home from '../views/home'
import Newmeal from '../views/newmeal'
import ShowRecipe from '../views/showRecipe'
import Profile from '../views/Profile'
import editRecipe from '../views/editRecipe'
Vue.use(Router)

export default new Router({
    routes: [
    {
        path: '/home',
        name: 'home',
        component: Home,
        meta: {
            requiredAuth: false,
        }
    }, 
    {
        path: '/recipe',
        name: 'recipe',
        component: Recipe,
        meta: {
            requiredAuth: true,
        }
    }, 
    {
        path: '/community',
        name: 'community',
        component: Community,
        meta: {
            requiredAuth: true,
        }
    }, 
    {
        path: '/newmeal',
        name: 'newmeal',
        component: Newmeal,
        meta: {
            requiredAuth: true,
        }
    }, 
    {
        path: '/login',
        name: 'login',
        component: Login,
    },
    {
        path: '/register',
        name: 'register',
        component: Register,
    },
    {
        path: '/showRecipe',
        name: 'ShowRecipe',
        component: ShowRecipe,
    },
    {
        path: '/editRecipe',
        name: 'editRecipe',
        component: editRecipe,
    },
    {
        path: '/Profile',
        name: 'Profile',
        component: Profile,
    },
]
})