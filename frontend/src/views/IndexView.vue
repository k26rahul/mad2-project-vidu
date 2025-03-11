<template>
  <nav>
    <router-link to="/login">Login</router-link>
    <router-link to="/register/customer">Register as Customer</router-link>
    <router-link to="/register/professionals">Register as Professionals</router-link>
  </nav>
  <h1>Household Services v2</h1>
</template>

<style scoped>
nav {
  display: flex;
  gap: 1rem;
  margin: 1rem 0;
}
</style>
