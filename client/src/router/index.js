import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '../components/HelloWorld';
import UserList from '../components/UserList'
import genUser from '../components/genUser'
import Deposite from '../components/Deposite'
import IncomeCheck from '../components/IncomeCheck'
import SoftIncomeCheck from '../components/SoftIncomeCheck'
import OtherFunction from '../components/OtherFuction'

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
      path:'/others',
      name:'OtherFunction',
      component: OtherFunction
    }
  ],
  mode: 'history',
});
