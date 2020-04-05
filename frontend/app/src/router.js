import Vue from "vue"
import VueRouter from "vue-router"

import Home from "./components/Home.vue"

Vue.use(VueRouter)

var router =  new VueRouter({
    routes: [
        {
            path:"/home",
            component: Home
        }
    ]
})

export default router
