import Vue from 'vue'
import VueRouter from 'vue-router'

import Base from './Base.vue'
import IndexPage from './commponents/index.vue'

Vue.use(VueRouter)
let router = new VueRouter({
  // 开启浏览器保存历史
  mode:'history',
  routes:[{
    path:'/',
    component:IndexPage
  }]
})

new Vue({
  el: '#app',
  // 注册
  router,
  components:{
    Base,
  },
  template:'<Base>'
})
