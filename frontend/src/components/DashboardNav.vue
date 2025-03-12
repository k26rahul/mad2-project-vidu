<script>
import router from '@/router';
import store from '@/store';

export default {
  methods: {
    async logout() {
      let res = await fetch('http://127.0.0.1:5000/api/logout');
      let data = await res.json();
      if (data.success) {
        store.isLoggedIn = false;
        store.userRole = null;
        router.push('/');
      }
    },
  },
};
</script>

<template>
  <nav>
    <router-link to="home">Home</router-link>
    <router-link to="search">Search</router-link>
    <router-link to="summary">Summary</router-link>
    <slot></slot>
    <a href="#" @click.prevent="logout">Logout</a>
  </nav>
</template>
