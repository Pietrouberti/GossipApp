<template>
    <div class="navbar">
        <div class="navbar__logo">
            <img src="https://www.atombank.co.uk/_astro/atom-logo.CV42YAKh.svg" alt="">
        </div>
        <ul class="navbar__list">
            <RouterLink class="navbar__item" to="/">Home</RouterLink>
            <RouterLink class="navbar__item" to="/dashboard">Dashboard</RouterLink>
            <RouterLink class="navbar__item" to="/about">About Us</RouterLink>
        </ul class="navbar__list">
        <div class="navbar__buttons">
            <button class="navbar__button" v-if="userStore.user.isAuthenticated"><RouterLink to="/login" @click="removeToken()">Logout</RouterLink></button>
            <button class="navbar__button" v-if="!userStore.user.isAuthenticated"><RouterLink to="/login">Login</RouterLink></button>
        </div>
    </div>
</template>
<script setup>
    import {useUserStore} from '@/stores/user.js';

    const userStore = useUserStore();

    const removeToken = () => {
        userStore.removeToken();
    }

</script>