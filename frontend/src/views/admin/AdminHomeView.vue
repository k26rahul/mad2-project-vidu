<script>
import { get } from '@/utils';

export default {
  data() {
    return {
      customers: [],
    };
  },
  async mounted() {
    this.customers = await get('/api/admin/customers');
  },
  methods: {
    async block(customer) {
      await get(`/api/admin/block/${customer.user_id}`);
      customer.active = false;
    },
    async unblock(customer) {
      await get(`/api/admin/unblock/${customer.user_id}`);
      customer.active = true;
    },
  },
};
</script>

<template>
  <h1>This is admin home</h1>
  <div class="table-responsive">
    <table class="table table-striped table-hover">
      <thead>
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Email</th>
          <th>Location</th>
          <th>Pincode</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="c in customers">
          <td>{{ c.id }}</td>
          <td>{{ c.name }}</td>
          <td>{{ c.email }}</td>
          <td>{{ c.location }}</td>
          <td>{{ c.pincode }}</td>
          <td>
            <button v-if="c.active" @click="block(c)">Block</button>
            <button v-else @click="unblock(c)">Unblock</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
