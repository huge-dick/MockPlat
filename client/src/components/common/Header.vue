<template>
  <div>
    <Menu mode="horizontal" :theme="theme1" active-name="1">
        <MenuItem name="1" to="/">
            <Icon type="md-apps" />
            功能导航
        </MenuItem>

        <Submenu name="2">
            <template slot="title">
                <Icon type="ios-build-outline" />
                Pool-X工具
            </template>
            <MenuGroup title="测试数据">
                <MenuItem name="2-1" to="/testusers">用户列表</MenuItem>
                <MenuItem name="2-2" to="/createuser">生成用户</MenuItem>
                <MenuItem name="2-3" to="/deposite">充值</MenuItem>
              <MenuItem name="2-3-1" to="/others">其他功能列表</MenuItem>
            </MenuGroup>

            <MenuGroup title="数据检查工具">
                <MenuItem name="2-4" to="incomecheck">一键锁仓收益检测</MenuItem>
                <MenuItem name="2-5" to="soft_income_check">持仓收益检测</MenuItem>
                <MenuItem name="2-6">lockDrop收益检测</MenuItem>
            </MenuGroup>
        </Submenu>

        <Submenu name="3">
            <template slot="title">
                <Icon type="ios-stats" />
                Mock平台
            </template>
            <MenuGroup title="">
                <MenuItem name="3-1" to="http://10.2.1.73:5000" target="_blank" >moco数据文件配置</MenuItem>
                <MenuItem name="3-2" to="https://nac.kucoin.com:1063/?p=1610" target="_blank">使用手册</MenuItem>
                <MenuItem name="3-3" to="http://10.2.1.73:5000/restart" target="_blank">重启Mock Server</MenuItem>
            </MenuGroup>

        </Submenu>
        <MenuItem name="4">
            更多
          <Icon type="ios-arrow-down" />
        </MenuItem>
    </Menu>
    <br>
    <!--<p>Change theme</p>-->
    <!--<RadioGroup v-model="theme1">-->
        <!--<Radio label="light"></Radio>-->
        <!--<Radio label="dark"></Radio>-->
        <!--<Radio label="primary"></Radio>-->
    <!--</RadioGroup>-->
    </div>
</template>
<script>
    export default {
        name: 'Header',
        data () {
            return {
                theme1: 'light'
            }
        }
    }
</script>

<style scoped>

</style>
