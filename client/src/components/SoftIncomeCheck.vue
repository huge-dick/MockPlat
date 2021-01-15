<template>
  <div>
    <div>
      <DatePicker type="date" @on-change="changeTime" format="yyyy-MM-dd" :options=dateOptions placeholder="选择需要检测的日期" style="width: 200px"></DatePicker>
      <Button id="startCheck" type="primary" @click="async_check">开始检测</Button>
    </div>
    <div id="income_check_list">
      <div id="softincome">
        <h5>持仓收益检测</h5>
        <Progress :percent="percent1" :status="status1"/>
        <div class="warning_font" v-if ="status1=='wrong'">预期本币收益{{exp_income1}}，实际本币收益{{income1}}</div>
        <br/><br/>
      </div>

      <div id="softlower">
        <h5>小于最小持仓收益检测</h5>
        <Progress :percent="percent2" :status="status2"/>
        <div class="warning_font" v-if ="status2=='wrong'">预期本币收益{{exp_income2}}，实际本币收益{{income2}}</div>
        <br/><br/>
      </div>

    </div>

    <div>
      <h5 class="notice_font">以上数据检测基于快照数据正确进行检测，17:30后可检测昨日收益，17:30前仅能检测更早以前的收益记录</h5>
    </div>

  </div>
</template>

<script>
  import {
    apiSoftIncomeCheck, apiSoftLowerCheck
  } from "../request/api";

    export default {
        name: "SoftIncomeCheck",
        data(){
            return{
              percent1:0,
              percent2:0,

              status1:"active",
              status2:"active",

              income1:"",
              income2:"",

              exp_income1:"",
              exp_income2:"",

              dateOptions:{
                shortcuts: [
                        {
                            text: '昨日',
                            value () {
                                const date = new Date();
                                date.setTime(date.getTime() - 3600 * 1000 * 24);
                                return date;
                            },
                            onClick: (picker) => {
                                // this.$Message.info("开始检测昨日收益");
                                // this.async_check()


                            }
                        },
                        {
                            text: '前天',
                            value () {
                                const date = new Date();
                                date.setTime(date.getTime() - 7200 * 1000 * 24);
                                return date;
                            },
                            onClick: (picker) => {
                                // this.$Message.info('开始检测前天收益');
                            }
                        }
                        ]


              }
            }
        },
        methods:{
          changeTime(e){
            this.checkDate=e
          },
          async_check(){

            apiSoftIncomeCheck({date:this.checkDate}).then(res => {
                if (res.code === 200){
                  if(res.result=="success"){
                      this.percent1=100,
                    this.status1="success"
                  }else{
                    this.percent1=75,
                    this.status1="wrong",
                      this.exp_income1=res.exp_income,
                      this.income1=res.income
                  }

                }else{
                  this.percent1=10,
                    this.status1="wrong"
                  this.$Message.error({
                    content:res.msg,
                    duration:5,
                    closable:true
                  })
                }
              })

              apiSoftLowerCheck({date:this.checkDate}).then(res => {
                if (res.code === 200){
                  if(res.result=="success"){
                      this.percent2=100,
                    this.status2="success"
                  }else{
                    this.percent2=75,
                    this.status2="wrong",
                      this.exp_income2=res.exp_income,
                      this.income2=res.income
                  }

                }else{
                  this.percent8=10,
                    this.status8="wrong"
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
  #income_check_list {
    margin-top: 20px;
    padding:10px 10px 50px 10px;

}
  .warning_font{
    font-size: xx-small;
    color: darkred;
  }

  .notice_font{
    font-size: xx-small;
    color: gray;
  }
</style>
