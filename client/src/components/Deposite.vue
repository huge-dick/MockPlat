<template>

    <div>
        <h4>给用户Pool-X帐户充值</h4>
        <br>
        <Input v-model="userId" placeholder="请输入用户userId" style="width: 240px" />
        <!--<br><br>-->
        <Input v-model="amount" placeholder="请输入充值数量" style="width: 200px" />
        <!--<br><br>-->
        <Input v-model="currency" placeholder="请输入充值币种" style="width: 200px" />
        <!--<br><br>-->
        <Button type="primary" @click="deposite">充值</Button>

        <br><br>
        <br>

        <h4>给用户充值NFT资产</h4>
        <br>
        <Input v-model="nftuserid" placeholder="请输入用户userId" style="width: 240px" />

        <Select v-model="nftcurrency" @on-change="fefreshtokens" style="width:200px">
        <Option v-for="item in currencyList" :value="item.value" :key="item.value">{{ item.label }}</Option>
        </Select>

      <Select v-model="nfttokenId" filterable style="width:200px">
        <Option v-for="item in tokenList" :value="item" :key="item">{{ item }}</Option>
        </Select>
        <Button type="primary" @click="nftdeposite">充值NFT</Button>

    </div>
</template>

<script>


  import {apiDeposite, apiGetNftTokens, apiNftReceipt} from "../request/api";

    export default {
        name: "Deposite",
        data(){
          return{
            userId: '',
            currency: 'KCS',
            amount: '10000',
            currencyList:[
              {
                        value: 'GEGO_V2',
                        label: 'GEGO_V2'
                    },
                    {
                        value: 'GEGO',
                        label: 'GEGO'
                    },
                    {
                        value: 'VELO_X',
                        label: 'VELO_X'
                    },
            ],
            tokenList:[],
            nftcurrency:'GEGO_V2',
            nfttokenId:'',
            nftuserid:''

          }
        },
      created(){
          this.fefreshtokens()
      },
        methods:{
          fefreshtokens(){
            apiGetNftTokens({
              currency:this.nftcurrency
            }).then(res => {
              if (res.code==200 || res.code=='200'){
                this.tokenList=res.tokenList
              }else{
                this.$Message.error({
                    content:res.msg,
                    duration:5,
                    closable:true
                  })
              }
            })
          },
          nftdeposite(){
            apiNftReceipt({
              userId:this.nftuserid,
              currency:this.nftcurrency,
              tokenId:this.nfttokenId
            }).then(res =>{
              if (res.code == 200 || res.code=='200'){
                  this.$Message.info({
                    content:"充值NFT成功",
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
          },
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
