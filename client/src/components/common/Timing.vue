<template>
  <Button @click="setTiming" :title="msg" type="primary">{{timing}}</Button>
</template>

<script>
import {apiTaskPause,apiTaskResume,apiGetTask} from "../../request/api"

export default {
    name: "Timing",
    props:['incomeType'],
    // inject:['reload'],
    data () {
      return{
        timing: '',
        id: '',
        timingFlag: '',
        msg:''
      }
    },
    created(){
        this.getID(this.incomeType)
        this.setBottonDate()
    },
    methods: {
      setTiming() {
        if (this.timingFlag === '0') {
          this.resume()
        } else {
          this.pause()
        }
        this.setBottonDate()
      },
      setBottonDate() {
        apiGetTask().then(res=> {
          for (var i=0; i<res.length; i++){
            if (res[i].id === this.id) {
                this.timingFlag = res[i].state
              if (this.timingFlag === '1') {
                  // alert('启动状态')
                  this.timing = '停止定时检测'
                  this.msg = '已开启定时任务，将在每日17：00：00检测'
                } else {
                  // alert('关闭状态')
                  this.timing = '启动定时检测'
                  this.msg = '已停止定时任务，点击"启动定时检测"开启'
                }
              }
            }
          })
      },
      getID(incomeType) {
        //一键锁仓收益检测
        if (incomeType == 'incomeCheck') {
          this.id = '2'
        }
        //持仓收益检测
        else if (incomeType == 'SoftIncomeCheck') {
          this.id = '1'
        }
      },
      pause (){   // 暂停定时任务
        apiTaskPause({id: this.id})
          .then(res =>{
            if (res === 'Success!') {
              this.$Message.info("已暂停定时任务！")
            }
          })
      },
      resume (){  // 启动定时任务
        apiTaskResume({id: this.id})
          .then(res => {
            if (res === 'Success!') {
              this.$Message.info("已启动时任务！")
            }
          })
      }
    }
}
</script>

<style scoped>

</style>
