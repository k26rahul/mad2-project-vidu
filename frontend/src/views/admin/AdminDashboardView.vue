<script>
import DashboardNav from '@/components/DashboardNav.vue';

export default {
  components: {
    DashboardNav,
  },
};
</script>

<template>
  <DashboardNav />
  <router-view></router-view>
</template>
