<template>
    <div class="userinput">
        <form class="userinput__form">
            <input type="text" class="userinput__input" v-model="userInput">
            <button class="userinput__submit">+</button>
        </form>
    </div>
</template>
<script setup>
import { ref } from 'vue';
const userInput = ref(null);


</script>