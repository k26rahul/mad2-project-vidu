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
          <th>Location</th>
          <th>Pincode</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="c in customers">
          <td>{{ c.id }}</td>
          <td>{{ c.name }}</td>
          <td>{{ c.location }}</td>
          <td>{{ c.pincode }}</td>
          <td>
            <button>Block</button>
            <button>Unblock</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
