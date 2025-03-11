import { createRouter, createWebHashHistory } from 'vue-router';
import IndexView from './views/IndexView.vue';
import LoginView from './views/auth/LoginView.vue';
import CustomerRegisterView from './views/auth/CustomerRegisterView.vue';
import ProfessionalsRegisterView from './views/auth/ProfessionalsRegisterView.vue';

const routes = [
  { path: '/', component: IndexView },
  { path: '/login', component: LoginView },
  { path: '/register/customer', component: CustomerRegisterView },
  { path: '/register/professionals', component: ProfessionalsRegisterView },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
