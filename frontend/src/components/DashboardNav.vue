<script>
import router from '@/router';
import store from '@/store';
import { get } from '@/utils';

export default {
  methods: {
    async logout() {
      let data = await get('/api/logout');
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
