import Vue from 'vue'
import Router from 'vue-router'
import About from '@/pages/About'
import Index from '@/pages/Index'
import Detail from '@/pages/Detail'
import Terminal from '@/pages/Terminal'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Welcome',
      component: Index
    },
    {
      path: '/index',
      name: 'Welcome',
      component: Index
    },
    {
      path: '/detail',
      name: 'Detail',
      component: Detail
    },
    {
      path: '/terminal/:id',
      name: 'Terminal',
      component: Terminal
    },
    {
      path: '/about',
      name: 'Aboutname',
      component: About
    }
  ]
})
