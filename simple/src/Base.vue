<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <div class="app-header">
        <Header/>
    </div>
    <div class="app-content">
        <Content/>
    </div>
    <div class="app-footer">
        <Footer/>
    </div>
  </div>
</template>

<script>
// 引入组件
// import HelloComponent from './HelloComponent' //文件已删除
import Header from './commponents/Header'
import Content from './commponents/Content'
import Footer from './commponents/Footer'
export default{
  data() {
    return {
      msg:'基础模板'
    };
  },
  // 调用
  components:{
    // HelloComponent,
    Header,
    Content,
    Footer
  }
}
</script>

// scoped只在当前模板起作用
<style scoped>
h1{
  color:red;
}
</style>
