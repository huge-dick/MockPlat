import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '../components/HelloWorld';
import UserList from '../components/UserList'
import genUser from '../components/genUser'
import Deposite from '../components/Deposite'
import IncomeCheck from '../components/IncomeCheck'
import SoftIncomeCheck from '../components/SoftIncomeCheck'
import Sharding from '../components/Sharding'
import ClearCache from '../components/ClearCache'
import InterfaceTest from '../components/InterfaceTest'
import TaskList from '../components/TaskList'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld,
    },
    {
      path: '/testusers',
      name: 'UserList',
      component: UserList,
    },
    {
      path: '/pool',
      redirect: '/testusers'
    },
    {
      path: '/createuser',
      name: 'genUser',
      component: genUser
    },
    {
      path: '/deposite',
      name: 'Deposite',
      component: Deposite
    },
    {
      path: '/incomecheck',
      name: 'IncomeCheck',
      component: IncomeCheck
    },
    {
      path: '/soft_income_check',
      name: 'SoftIncomeCheck',
      component: SoftIncomeCheck
    },
    {
      path:'/clearcache',
      name:'ClearCache',
      component: ClearCache
    },
    {
      path:'/sharding',
      name:'Sharding',
      component: Sharding
    },
    {
      path:'/interfaceTest',
      name:'InterfaceTest',
      component: InterfaceTest
    },
    {
      path:'/task_list',
      name:'TaskList',
      component: TaskList
    }
  ],
  mode: 'history',
});
