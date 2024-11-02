<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/global/Navbar.vue'
</script>

<template>
  <header>
    <div class="wrapper">
      <Navbar></Navbar>
    </div>
  </header>
  <RouterView />
</template>
