import { createRouter, createWebHashHistory } from 'vue-router';
import store from './store';

import IndexView from './views/IndexView.vue';
import LoginView from './views/auth/LoginView.vue';
import CustomerRegisterView from './views/auth/CustomerRegisterView.vue';
import ProfessionalsRegisterView from './views/auth/ProfessionalsRegisterView.vue';

import AdminDashboardView from './views/admin/AdminDashboardView.vue';
import AdminHomeView from './views/admin/AdminHomeView.vue';
import AdminSearchView from './views/admin/AdminSearchView.vue';
import AdminSummaryView from './views/admin/AdminSummaryView.vue';
import AdminAddServiceView from './views/admin/AdminAddServiceView.vue';

import CustomerDashboardView from './views/customer/CustomerDashboardView.vue';
import CustomerHomeView from './views/customer/CustomerHomeView.vue';
import CustomerSearchView from './views/customer/CustomerSearchView.vue';
import CustomerSummaryView from './views/customer/CustomerSummaryView.vue';
import CustomerProfileView from './views/customer/CustomerProfileView.vue';

import ProfessionalsDashboardView from './views/professionals/ProfessionalsDashboardView.vue';
import ProfessionalsHomeView from './views/professionals/ProfessionalsHomeView.vue';
import ProfessionalsSearchView from './views/professionals/ProfessionalsSearchView.vue';
import ProfessionalsSummaryView from './views/professionals/ProfessionalsSummaryView.vue';
import ProfessionalsProfileView from './views/professionals/ProfessionalsProfileView.vue';

const routes = [
  { path: '/', component: IndexView },
  { path: '/login', component: LoginView },
  { path: '/register/customer', component: CustomerRegisterView },
  { path: '/register/professionals', component: ProfessionalsRegisterView },

  {
    path: '/admin',
    component: AdminDashboardView,
    children: [
      { path: '', redirect: '/admin/home' },
      { path: 'home', component: AdminHomeView },
      { path: 'add-service', component: AdminAddServiceView },
      { path: 'search', component: AdminSearchView },
      { path: 'summary', component: AdminSummaryView },
    ],
  },

  {
    path: '/customer',
    component: CustomerDashboardView,
    children: [
      { path: '', redirect: '/customer/home' },
      { path: 'home', component: CustomerHomeView },
      { path: 'search', component: CustomerSearchView },
      { path: 'summary', component: CustomerSummaryView },
      { path: 'profile', component: CustomerProfileView },
    ],
  },

  {
    path: '/professionals',
    component: ProfessionalsDashboardView,
    children: [
      { path: '', redirect: '/professionals/home' },
      { path: 'home', component: ProfessionalsHomeView },
      { path: 'search', component: ProfessionalsSearchView },
      { path: 'summary', component: ProfessionalsSummaryView },
      { path: 'profile', component: ProfessionalsProfileView },
    ],
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (store.isLoggedIn) {
    if (to.path === '/') {
      if (store.userRole === 'admin') return next('/admin/home');
      else if (store.userRole === 'customer') return next('/customer/home');
      else return next('/professionals/home');
    }
  } else if (
    to.path.startsWith('/admin') ||
    to.path.startsWith('/customer') ||
    to.path.startsWith('/professionals')
  ) {
    return next('/login');
  }

  next();
});

export default router;
