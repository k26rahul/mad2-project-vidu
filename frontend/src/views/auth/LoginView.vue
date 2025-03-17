<script>
import router from '@/router';
import store from '@/store';
import { post } from '@/utils';

export default {
  setup() {
    return { store };
  },
  data() {
    return {
      email: '',
      password: '',
      error: null,
    };
  },
  methods: {
    async submitForm() {
      let data = await post('/api/login', {
        email: this.email,
        password: this.password,
      });

      if (data.success) {
        store.isLoggedIn = true;
        store.userRole = data.role;
        router.push('/');
      } else {
        this.error = data.message;
      }
    },
  },
};
</script>

<template>
  <h1 style="text-align: center; margin-top: 1rem">Login</h1>

  <form @submit.prevent="submitForm">
    <p v-show="error" class="alert alert-danger">
      <span v-if="error === 'Email or password incorrect'"
        >Email or password incorrect, please try again.</span
      >
      <span v-else-if="error === 'User is blocked'">You are blocked, please contact admins.</span>
    </p>

    <div>
      <label class="form-label">
        Email:
        <input type="email" v-model="email" class="form-control" />
      </label>
    </div>

    <div>
      <label class="form-label">
        Password:
        <input type="password" v-model="password" class="form-control" />
      </label>
    </div>

    <button>Login</button>
  </form>
</template>
