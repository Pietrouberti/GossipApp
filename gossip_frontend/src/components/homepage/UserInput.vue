<template>
    <div class="userinput">
        <input type="text" class="userinput__input" v-model="userInput">
        <button class="userinput__submit">Submit</button>
    </div>
</template>
<script setup>
import { ref } from 'vue';
const userInput = ref(null);


</script>