<template>
  <div >

    <h4>清除币服务缓存</h4>
    <br>
    <Button type="primary" @click="clearCache">清除币服缓存</Button>
    <!--<h4>设置交易对价格(当币种价格不存在，无法挖矿，无法计算收益等情况下可使用)</h4>-->

  </div>

</template>

<script>
    import {apiClearCurrencyCache} from "../request/api";

    export default {
        name: "OtherFunction",
        methods:{
          clearCache(){
            apiClearCurrencyCache().then(res => {
                if (res.code === "200"){
                  this.$Message.info({
                    content:"清除币服缓存成功",
                    duration:2,
                    closable:true

                  })
                }else{
                  this.$Message.error({
                    content:res.msg,
                    duration:2,
                    closable:true
                  })
                }
              })
          }
        }
    }
</script>

<style scoped>


</style>
