<template>
  <div id="app">
    <Header></Header>
    <router-view></router-view>
    <!--<Footer></Footer>-->
  </div>
</template>

<script>
import Header from "./components/common/Header";
import Footer from "./components/common/Footer"
export default {
  name: 'App',
  components: {
    Header,
    Footer,

  },
};
</script>

<style>
#app {
  margin: 10px 0px 10px 0px;
  padding:10px
}
</style>
