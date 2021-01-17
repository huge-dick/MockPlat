<template>
  <div>
    <div>
      <DatePicker type="date" @on-change="changeTime" format="yyyy-MM-dd" :options=dateOptions placeholder="选择需要检测的日期" style="width: 200px"></DatePicker>
      <Button id="startCheck" type="primary" @click="async_check">开始检测</Button>
      <Timing :incomeType="incomeType"></Timing>
    </div>
    <div id="income_check_list">
      <div id="subscribe">
        <h5>申购期收益检测</h5>
        <Progress :percent="percent1" :status="status1"/>
        <div class="warning_font" v-if ="status1=='wrong'">预期本币收益{{exp_currency_income1}}，实际本币收益{{acc_currency_income1}}，预期POL收益{{exp_pol_income1}}，实际POL收益{{acc_pol_income1}}</div>
        <br/><br/>
      </div>

      <div id="time">
        <h5>定期产品质押期间收益检测</h5>
        <Progress :percent="percent2" :status="status2"/>
        <div class="warning_font" v-if ="status2=='wrong'">预期本币收益{{exp_currency_income2}}，实际本币收益{{acc_currency_income2}}，预期POL收益{{exp_pol_income2}}，实际POL收益{{acc_pol_income2}}</div>
        <br/><br/>
      </div>

      <div id="demand">
        <h5>活期产品收益检测</h5>
        <Progress :percent="percent3" :status="status3"/>
        <div class="warning_font" v-if ="status3=='wrong'">预期本币收益{{exp_currency_income3}}，实际本币收益{{acc_currency_income3}}，预期POL收益{{exp_pol_income3}}，实际POL收益{{acc_pol_income3}}</div>
        <br/><br/>
      </div>

      <div id="black">
        <h5>本币收益黑名单检测</h5>
        <Progress :percent="percent4" :status="status4"/>
        <div class="warning_font" v-if ="status4=='wrong'">预期本币收益{{exp_currency_income4}}，实际本币收益{{acc_currency_income4}}，预期POL收益{{exp_pol_income4}}，实际POL收益{{acc_pol_income4}}</div>
        <br/><br/>
      </div>

      <div id="fake">
        <h5>fake锁仓收益检测</h5>
        <Progress :percent="percent5" :status="status5"/>
        <div class="warning_font" v-if ="status5=='wrong'">预期本币收益{{exp_currency_income5}}，实际本币收益{{acc_currency_income5}}，预期POL收益{{exp_pol_income5}}，实际POL收益{{acc_pol_income5}}</div>
        <br/><br/>
      </div>

      <div id="vote">
        <h5>投票收益检测</h5>
        <Progress :percent="percent6" :status="status6"/>
        <div class="warning_font" v-if ="status6=='wrong'">预期本币收益{{exp_currency_income6}}，实际本币收益{{acc_currency_income6}}，预期POL收益{{exp_pol_income6}}，实际POL收益{{acc_pol_income6}}</div>
        <br/><br/>
      </div>

      <div id="liquidity">
        <h5>赎回期系数检测</h5>
        <Progress :percent="percent7" :status="status7"/>
        <div class="warning_font" v-if ="status7=='wrong'">预期调整系数{{exp_liquidity}}，实际调整系数{{liquidity}}</div>
        <br/><br/>
      </div>

      <div id="total">
        <h5>平台挖矿总产出检测</h5>
        <Progress :percent="percent8" :status="status8"/>
        <div class="warning_font" v-if ="status8=='wrong'">预期总产出{{expect_total}}，实际总产出{{acc_total}}</div>
        <br/><br/>
      </div>

    </div>

    <div>
      <h5 class="notice_font">以上数据检测基于快照数据正确进行检测，16:00后可检测昨日收益，16:00前仅能检测更早以前的收益记录</h5>
    </div>

  </div>
</template>

<script>
  import {
    apiIncomeCheckBlack,
    apiIncomeCheckDemand,
    apiIncomeCheckFake, apiIncomeCheckLiquidity,
    apiIncomeCheckSubscribe,
    apiIncomeCheckTime, apiIncomeCheckTotal, apiIncomeCheckVote
  } from "../request/api";
  import Timing from './common/Timing.vue'

    export default {
        name: "IncomeCheck",
        components:{
          'Timing': Timing
        },
        data(){
            return{
              percent1:0,
              percent2:0,
              percent3:0,
              percent4:0,
              percent5:0,
              percent6:0,
              percent7:0,
              percent8:0,
              status1:"active",
              status2:"active",
              status3:"active",
              status4:"active",
              status5:"active",
              status6:"active",
              status7:"active",
              status8:"active",
              exp_currency_income1:"",
              exp_currency_income2:"",
              exp_currency_income3:"",
              exp_currency_income4:"",
              exp_currency_income5:"",
              exp_currency_income6:"",
              exp_currency_income7:"",
              exp_currency_income8:"",

              acc_currency_income1:"",
              acc_currency_income2:"",
              acc_currency_income3:"",
              acc_currency_income4:"",
              acc_currency_income5:"",
              acc_currency_income6:"",
              acc_currency_income7:"",
              acc_currency_income8:"",




              exp_pol_income1:"",
              exp_pol_income2:"",
              exp_pol_income3:"",
              exp_pol_income4:"",
              exp_pol_income5:"",
              exp_pol_income6:"",
              exp_pol_income7:"",
              exp_pol_income8:"",

              acc_pol_income1:"",
              acc_pol_income2:"",
              acc_pol_income3:"",
              acc_pol_income4:"",
              acc_pol_income5:"",
              acc_pol_income6:"",
              acc_pol_income7:"",
              acc_pol_income8:"",


              expect_total:"",
              acc_total:"",
              exp_liquidity:"",
              liquidity:"",
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


              },
              incomeType:"incomeCheck",
              checkDate:null
            }
        },
        methods:{
          changeTime(e){
            this.checkDate=e
          },
          async_check(){
            if (this.checkDate === null){
              this.$Message.info('请填写需要检测的日期！')
              return
            }
            apiIncomeCheckSubscribe({date:this.checkDate}).then(res => {
                if (res.code === 200){
                  if(res.result=="success"){
                      this.percent1=100,
                    this.status1="success"
                  }else{
                    this.percent1=75,
                    this.status1="wrong",
                      this.exp_currency_income1=res.exp_currency_income,
                      this.acc_currency_income1=res.acc_currency_income,
                      this.exp_pol_income1=res.exp_pol_income,
                      this.acc_pol_income1=res.acc_pol_income
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
              });

            apiIncomeCheckTime({date:this.checkDate}).then(res => {
                if (res.code === 200){
                  if(res.result=="success"){
                      this.percent2=100,
                    this.status2="success"
                  }else{
                    this.percent2=75,
                    this.status2="wrong",
                      this.exp_currency_income2=res.exp_currency_income,
                      this.acc_currency_income2=res.acc_currency_income,
                      this.exp_pol_income2=res.exp_pol_income,
                      this.acc_pol_income2=res.acc_pol_income
                  }

                }else{
                  this.percent2=10,
                    this.status2="wrong"
                  this.$Message.error({
                    content:res.msg,
                    duration:5,
                    closable:true
                  })
                }
              });

            apiIncomeCheckDemand({date:this.checkDate}).then(res => {
                if (res.code === 200){
                  if(res.result=="success"){
                      this.percent3=100,
                    this.status3="success"
                  }else{
                    this.percent3=75,
                    this.status3="wrong",
                      this.exp_currency_income3=res.exp_currency_income,
                      this.acc_currency_income3=res.acc_currency_income,
                      this.exp_pol_income3=res.exp_pol_income,
                      this.acc_pol_income3=res.acc_pol_income
                  }

                }else{
                  this.percent3=10,
                    this.status3="wrong"
                  this.$Message.error({
                    content:res.msg,
                    duration:5,
                    closable:true
                  })
                }
              });

            apiIncomeCheckBlack({date:this.checkDate}).then(res => {
                if (res.code === 200){
                  if(res.result=="success"){
                      this.percent4=100,
                    this.status4="success"
                  }else{
                    this.percent4=75,
                    this.status4="wrong",
                      this.exp_currency_income4=res.exp_currency_income,
                      this.acc_currency_income4=res.acc_currency_income,
                      this.exp_pol_income4=res.exp_pol_income,
                      this.acc_pol_income4=res.acc_pol_income
                  }

                }else{
                  this.percent4=10,
                    this.status4="wrong"
                  this.$Message.error({
                    content:res.msg,
                    duration:5,
                    closable:true
                  })
                }
              });

            apiIncomeCheckFake({date:this.checkDate}).then(res => {
                if (res.code === 200){
                  if(res.result=="success"){
                      this.percent5=100,
                    this.status5="success"
                  }else{
                    this.percent5=75,
                    this.status5="wrong",
                      this.exp_currency_income5=res.exp_currency_income,
                      this.acc_currency_income5=res.acc_currency_income,
                      this.exp_pol_income5=res.exp_pol_income,
                      this.acc_pol_income5=res.acc_pol_income
                  }

                }else{
                  this.percent5=10,
                    this.status5="wrong"
                  this.$Message.error({
                    content:res.msg,
                    duration:5,
                    closable:true
                  })
                }
              });

            apiIncomeCheckVote({date:this.checkDate}).then(res => {
                if (res.code === 200){
                  if(res.result=="success"){
                      this.percent6=100,
                    this.status6="success"
                  }else{
                    this.percent6=75,
                    this.status6="wrong",
                      this.exp_currency_income6=res.exp_currency_income,
                      this.acc_currency_income6=res.acc_currency_income,
                      this.exp_pol_income6=res.exp_pol_income,
                      this.acc_pol_income6=res.acc_pol_income
                  }

                }else{
                  this.percent6=10,
                    this.status6="wrong"
                  this.$Message.error({
                    content:res.msg,
                    duration:5,
                    closable:true
                  })
                }
              });

            apiIncomeCheckLiquidity({date:this.checkDate}).then(res => {
                if (res.code === 200){
                  if(res.result=="success"){
                      this.percent7=100,
                    this.status7="success"
                  }else{
                    this.percent7=75,
                    this.status7="wrong",
                      this.exp_liquidity=res.exp_liquidity,
                      this.liquidity=res.liquidity

                  }

                }else{
                  this.percent7=10,
                    this.status7="wrong"
                  this.$Message.error({
                    content:res.msg,
                    duration:5,
                    closable:true
                  })
                }
              });

            apiIncomeCheckTotal({date:this.checkDate}).then(res => {
                if (res.code === 200){
                  if(res.result=="success"){
                      this.percent8=100,
                    this.status8="success"
                  }else{
                    this.percent8=75,
                    this.status8="wrong",
                      this.expect_total=res.expect_total,
                      this.acc_total=res.acc_total
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
