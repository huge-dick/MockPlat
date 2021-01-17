<template>
  <div>
      <h4>定时任务列表</h4>
      <br>
      <Table border :context="self" :columns="columns" :data="data"></Table>
      <Page  class="page-style" :total="page.total" show-sizer show-elevator @on-change="pIndexChange" @on-page-size-change="pSizeChange"/>
    </div>
</template>

<script>
import {apiGetTask,apiTaskPause,apiTaskResume} from "../request/api";
export default {
    name: "TaskList",
    data () {
      return {
        self: this,
        columns:[
          {
            title: 'id',
            key: 'id',
            width: 150,
            align: 'center'
          },{
            title: '检测项',
            key: 'name'
          },
          {
            title: '状态',
            key: 'state',
            width: 200,
            align: 'center'
          },
          {
            title: '操作',
            key: 'action',
            width: 200,
            align: 'center',
            render: (h, params) => {
                return h('div', [
                    h('Button', {
                        props: {
                            type: 'primary',
                            size: 'small'
                        },
                        on: {
                            click: () => {
                                this.$Modal.confirm({
                                    title: '修改',
                                    content: '<p>确认修改定时任务状态吗?</p>',
                                    onOk: () => {
                                        console.log(params.row)
                                        // alert(params.row.id)
                                        if (params.row.state === this.openTask) {
                                          this.pause(params.row.id, params.row.name)
                                        }
                                        if (params.row.state === this.closeTask){
                                          this.resume(params.row.id, params.row.name)
                                        }
                                        this.setBottonDate()
                                    },
                                    onCancel: () => {}
                                });
                            }
                        }
                    }, '修改')
                ]);
            }
          },
        ],
        data:[],
        page:{
              index:1,
              size:10,
              total:0
          },
        openTask : '已开启',
        closeTask: '已暂停'
      }
    },
    created(){
      this.setBottonDate()
    },
    methods:{
      setBottonDate(){
        apiGetTask().then(res=> {
        this.data = res
        for (var i=0; i<this.data.length; i++){
          if (this.data[i].name === 'soft_income_check')  this.data[i].name = '持仓收益检测'
          if (this.data[i].name === 'staking_income_check')  this.data[i].name = '锁仓收益检测'
          if (this.data[i].state === '1')  this.data[i].state = this.openTask
          if (this.data[i].state === '0')  this.data[i].state = this.closeTask
          }
        })
      },
      pause (index, name){   // 暂停定时任务
        // alert('暂停定时任务')
        apiTaskPause({id: index})
          .then(res =>{
            if (res === 'Success!') {
              this.$Message.info(this.closeTask+" ["+name+"] 定时任务！")
            }
          })
      },
      resume (index, name){  // 启动定时任务
        // alert('启动定时任务')
        apiTaskResume({id: index})
          .then(res => {
            if (res === 'Success!') {
              this.$Message.info(this.openTask+" ["+name+"] 定时任务！")
            }
          })
      },
      pIndexChange(i){
        this.page.index=i;
        this.query()

      },
      pSizeChange(i){
        this.page.size=i;
        this.query()
      }
    }
}
</script>

<style scoped>
  .page-style{
    text-align: right;
  }
</style>
