import Vue from 'vue/dist/vue.js'
import VueMathPlugin from './VueMatchPlugin.js'

Vue.use(VueMathPlugin)
new Vue({
    el:'#app',
    data:{
        item:20
    }
})