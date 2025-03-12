import { reactive, watch } from 'vue';

const initialState = {
  isLoggedIn: false,
  userRole: null,
  errorFlag: false,
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

store.errorFlag = false;

export default store;
