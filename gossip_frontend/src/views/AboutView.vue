<template>
  <div class="about">
    <h1>This is an about page</h1>
    <h2>{{counter}}</h2>
    <button @click="jumpCounter()">Increment</button>
  </div>
</template>

<script setup>
  import {ref, reactive } from 'vue';
  const counter = ref(0)

  const jumpCounter = () => {
    counter.value += 1;
  }
</script>
