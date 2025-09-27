import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import '@/assets/style.css';
import { get } from './utils';

const app = createApp(App);
app.use(router);
app.mount('#app');

window.whoami = async () => {
  console.log(await get('/api/whoami'));
};
