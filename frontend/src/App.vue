<script>
import store from './store';

export default {
  setup() {
    return { store };
  },
};
</script>

<template>
  <h1 v-show="store.errorFlag" class="alert alert-danger">
    Something went wrong, please refresh the page. 🙏
  </h1>
  <main>
    <router-view></router-view>
  </main>
</template>
