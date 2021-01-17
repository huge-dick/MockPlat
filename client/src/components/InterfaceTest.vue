<template>
  <div>
    <div>
      <Button type="primary" @click="addInterface">新增接口</Button>
      <br>
      <br>
      <Table stripe border :columns="columns" :data="data"></Table>
      <Page  class="page-style" :total="page.total" show-sizer show-elevator @on-change="pIndexChange" @on-page-size-change="pSizeChange"/>
    </div>
  </div>
</template>

<script>
    export default {
        name: "InterfaceTest",
        data () {
          return {
            columns:[
              {
                title: '接口路径',
                key: 'interfacePath'
              },{
                title: '请求方法',
                key: 'interfaceName'
              },{
                title: '接口内容',
                key: 'interfaceData'
              },{
                title: '接口描述',
                key: 'interfaceDes'
              }
            ],
            data:[],
            page:{
                  index:1,
                  size:10,
                  total:0
              }
          }
        },
      methods:{
        pIndexChange(i){
          this.page.index=i;
          this.query()

        },

        pSizeChange(i){
          this.page.size=i;
          this.query()

        },
        addInterface (){

        }
      }
    }
</script>

<style scoped>
  .page-style{
    text-align: right;
  }

</style>
