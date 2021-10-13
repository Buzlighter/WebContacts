import Vue from 'vue';
import Router from 'vue-router';
import Users from "../components/Users";

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/users',
      name: 'Users',
      component: Users,
    },
  ],
});
