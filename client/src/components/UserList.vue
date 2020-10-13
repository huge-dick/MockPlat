<template>
  <div>
    <h4>测试用户列表</h4>
    <br>
    <div>
      <div>
        <div>
          <Input v-model="email" placeholder="请输入邮箱" style="width: auto" />
          <Button type="primary" @click="search">搜索</Button>
           <h4 class="gcode-style">google验证码: {{googleCode}} </h4>
        </div>

      </div>

    </div>

    <Table stripe border :columns="columns1" :data="data1"></Table>
    <Page  class="page-style" :total="page.total" show-sizer show-elevator @on-change="pIndexChange" @on-page-size-change="pSizeChange"/>
  </div>

</template>
<script>
  import {apiGoogleCode, apiUserList} from "../request/api";


export default {
  name: 'Address',
  data () {
            return {

                starttimer:true,

                googleCode:'-',

                email:'',

                columns1: [
                    {
                        title: 'userid',
                        key: 'id'
                    },
                    {
                        title: 'UID',
                        key: 'uid'
                    },
                    {
                        title: '邮箱',
                        key: 'email'
                    },
                  {
                        title: '登录密码',
                        key: 'password'
                    },
                  {
                        title: '交易密码',
                        key: 'trade_pwd'
                    },
                  {
                        title: '两步验证密钥',
                        key: 'google_key'
                    },
                  {
                        title: '创建时间',
                        key: 'created_at'
                    },

                ],
                data1:[],
              page:{
                  index:1,
                  size:10,
                  total:100
              }
            }
        },
  created() {
    this.refreshCode();
    this.onLoad();
  },
  methods: {
    // 获取数据
    onLoad() {
      // 调用api接口，并且提供了两个参数
      apiUserList({
        page: 1,
        pageSize: 10
      }).then(res => {
        this.data1=res.data
        this.page.index=res.currentPage
        this.page.total=res.total

      })
    },

    query() {
      apiUserList({
        page: this.page.index,
        pageSize: this.page.size
      }).then(res => {
        this.data1 = res.data
        this.page.index = res.currentPage
        this.page.total = res.total

      })
    },

    search(){
      this.page.index=1
      apiUserList({
        page: this.page.index,
        pageSize: this.page.size,
        email: this.email
      }).then(res => {
        this.data1 = res.data
        this.page.index = res.currentPage
        this.page.total = res.total

      })
    },

    pIndexChange(i){
      this.page.index=i;
      this.query()

    },

    pSizeChange(i){
      this.page.size=i;
      this.query()

    },

    genCode(){
      apiGoogleCode().then(res => {
        this.googleCode=res.google_code

      })
    },

    refreshCode() {
      let _this=this
     async function timerFn() {
        if (!_this.starttimer) return
      await _this.genCode()
  
      setTimeout(timerFn, 2000)
     }
     timerFn();
    },

    stopTime(){
      this.starttimer=false
    }

  },
  //离开页面时停止轮询
  destroyed(){
    this.stopTime();
   }


}
</script>


<style scoped>
  .page-style{
    text-align: right;
  }
  .gcode-style{
    text-align: right;
    color:#2d8cf0;
    padding-right: 15px;
    padding-bottom: 5px;
  }
</style>
