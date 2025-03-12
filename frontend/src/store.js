import { reactive, watch } from 'vue';

const initialState = {
  isLoggedIn: false,
  userRole: null,
};

const appState = JSON.parse(localStorage.getItem('appState')) || initialState;

const store = reactive(appState);

watch(
  store,
  appState => {
    localStorage.setItem('appState', JSON.stringify(appState));
  },
  { deep: true }
);

export default store;
