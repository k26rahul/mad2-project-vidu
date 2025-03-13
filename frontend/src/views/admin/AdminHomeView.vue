<script>
import { get } from '@/utils';

export default {
  async mounted() {
    console.log(await get('/api/admin/customers'));
    console.log(await get('/api/whoami'));
  },
};
</script>

<template>
  <h1>This is admin home</h1>
</template>
