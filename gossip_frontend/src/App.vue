<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/global/Navbar.vue'
import {ref, onMounted } from 'vue';
import {useUserStore} from '@/stores/user.js'

const userStore = useUserStore();


onMounted(() => {
  userStore.initStore();
});
</script>

<template>
  <header>
    <div class="wrapper">
      <Navbar></Navbar>
    </div>
  </header>
  <RouterView />
</template>
