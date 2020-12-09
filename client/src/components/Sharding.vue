<template>

    <div >
      <div>
          <h4>account分库分表查询</h4>
        <br>
        <Input v-model="userIdkc" placeholder="请输入用户userId" style="width: auto" />
          <Button type="primary" @click="shardingAccount">查询</Button>
        <br>
        <div class="notice_font" v-if="accountDbIndex!=''" >
          用户账务余额保存在<span class="light_font">{{accountDbIndex}}</span>库<span class="light_font">{{accountTableIndex}}</span>表
        </div>
      </div>

      <br>
      <br>
      <div >
          <h4>Pool-X分表查询</h4>
        <br>
        <Input v-model="userIdpx" placeholder="请输入用户userId" style="width: auto" />
          <Button type="primary" @click="shardingPool">查询</Button>
        <br>
        <div class="notice_font" v-if="poolTableIndex!=''" >
          用户数据保存在<span class="light_font">{{poolTableIndex}}</span>表
        </div>

      </div>

    </div>
</template>

<script>
  import {apiShardingAccount, apiShardingPoolTable} from "../request/api";

    export default {
        name: "Sharding",
        data(){
          return {
            userIdkc:'',
            userIdpx:'',
            accountDbIndex:'',
            accountTableIndex:'',
            poolTableIndex:'',
          }
        },
        methods:{
          shardingAccount(){
            apiShardingAccount({
              userId:this.userIdkc
            }).then(res => {
                if (res.code === "200"){
                  this.accountDbIndex= res.data.dataSourceIndex
                  this.accountTableIndex=res.data.tableIndex
                }else{
                  this.$Message.error({
                    content:res.msg,
                    duration:2,
                    closable:true
                  })
                }
              })
          },
          shardingPool(){
            apiShardingPoolTable({
              userId:this.userIdpx
            }).then(res => {
                if (res.code === "200" || res.code===200){
                  this.poolTableIndex= res.data.table_index
                }else{
                  this.$Message.error({
                    content:res.msg,
                    duration:2,
                    closable:true
                  })
                }
              })
          },
        }
    }
</script>

<style scoped>
     .light_font{
    font-size: small;
    color:lightcoral ;
       font-weight:bold;
  }
     .notice_font{
       font-size: xx-small;
    color:gray ;
       font-weight:bold;
     }

  .div-spacing{
    margin-top: 10px;

  }
</style>
