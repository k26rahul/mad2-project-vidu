<script>
import DashboardNav from '@/components/DashboardNav.vue';

export default {
  components: {
    DashboardNav,
  },
};
</script>

<template>
  <DashboardNav>
    <router-link to="profile">Profile</router-link>
  </DashboardNav>
  <router-view></router-view>
</template>
