<template>
    <div>
        <h4>快速生成测试用户</h4>
      <br>
        <Input v-model="email" prefix="ios-contact" placeholder="请输入邮箱" style="width: auto" />
        <Button type="primary" @click="genUser">提交</Button>
    </div>
</template>

<script>
    import {apiGenUser} from "../request/api";

    export default {
        name: "genUser",
        data(){
          return{
            email: ''
          }
        },
        methods:{
          genUser(){
              apiGenUser({
                email:this.email
              }).then(res => {
                if (res.code === 200){
                  this.$Message.info({
                    content:"用户添加成功，并且已完成部分币种充值，请前往用户列表查看",
                    duration:5,
                    closable:true

                  })
                }else{
                  this.$Message.error({
                    content:res.msg,
                    duration:5,
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
