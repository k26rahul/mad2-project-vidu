<script>
import router from '@/router';
import store from '@/store';

export default {
  setup() {
    return { store };
  },
  data() {
    return {
      email: '',
      password: '',
      errorFlag: false,
    };
  },
  methods: {
    async submitForm() {
      let formData = new FormData();
      formData.append('email', this.email);
      formData.append('password', this.password);

      let res = await fetch('http://127.0.0.1:5000/api/login', {
        method: 'POST',
        body: formData,
      });
      let data = await res.json();

      if (data.success) {
        store.isLoggedIn = true;
        store.userRole = data.role;
        router.push('/');
      } else {
        this.errorFlag = true;
      }
    },
  },
};
</script>

<template>
  <h1 style="text-align: center; margin-top: 1rem">Login</h1>

  <form @submit.prevent="submitForm">
    <p v-show="errorFlag" class="alert alert-danger">
      Email or password incorrect, please try again.
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
