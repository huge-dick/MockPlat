<template>
    <!--<div align="center">-->
    <div>
        <h4>给用户Pool-X帐户充值</h4>
        <br>
        <Input v-model="userId" placeholder="请输入用户userId" style="width: 240px" />
        <!--<br><br>-->
        <Input v-model="amount" placeholder="请输入充值数量" style="width: auto" />
        <!--<br><br>-->
        <Input v-model="currency" placeholder="请输入充值币种" style="width: auto" />
        <!--<br><br>-->
        <Button type="primary" @click="deposite">充值</Button>
    </div>
</template>

<script>


    import {apiDeposite} from "../request/api";

    export default {
        name: "Deposite",
        data(){
          return{
            userId: '',
            currency: 'KCS',
            amount: '10000'

          }
        },
        methods:{
          deposite(){
              apiDeposite({
                userId: this.userId,
                currency: this.currency,
                amount: this.amount
              }).then(res => {
                if (res.code == 200){
                  this.$Message.info({
                    content:"充值成功",
                    duration:3,
                    closable:false

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
