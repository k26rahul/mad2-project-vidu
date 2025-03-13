import { reactive, watch } from 'vue';

const saved = JSON.parse(localStorage.getItem('appState')) || {};
const appState = {
  isLoggedIn: false,
  userRole: null,
  ...saved,
  errorFlag: false,
};

const store = reactive(appState);

watch(
  store,
  appState => {
    localStorage.setItem('appState', JSON.stringify(appState));
  },
  { deep: true }
);

export default store;
