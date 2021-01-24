<template>
  <div>
    <Alert show-icon banner closable>
      每日17：30定时执行用例并更新，可根据需要
      <Button type="primary" :to="jenkinsJobUrl" target="_blank">手动构建</Button>
    </Alert>
    <iframe :src='reportUrl' frameborder="0" style="width:100%;height:800px;" id="iframeBox"></iframe>
  </div>
</template>

<script>
export default {
    name: "InterfaceReport",
    data() {
      return {
        reportUrl: "http://10.2.1.32:8088/job/px-interface-test/allure/",
        jenkinsJobUrl:"http://10.2.1.32:8088/job/px-interface-test/"
      }
    }
}
</script>

<style scoped>
  .info-style{
    text-align: right;
  }
</style>
