<template>
    <div class="navbar">
        <div class="navbar__logo">
            <img src="https://www.atombank.co.uk/_astro/atom-logo.CV42YAKh.svg" alt="">
        </div>
        <ul class="navbar__list">
            <RouterLink class="navbar__item" to="/">Home</RouterLink>
            <RouterLink class="navbar__item" to="/about">About</RouterLink>
        </ul class="navbar__list">
        <div class="navbar__buttons">
            <button class="navbar__button"><RouterLink to="/login">Logout</RouterLink></button>
            <button class="navbar__button"><RouterLink to="/login">Login</RouterLink></button>
        </div>
    </div>
</template>
<script setup>
    
</script>