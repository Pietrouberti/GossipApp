<template>
    <div class="login__container">
        <h2 class="login__title">Login to your account</h2>
        <form v-on:submit.prevent="submitForm()" class="login__form">
            <input type="text" placeholder="Username" class="login__input" v-model="email">
            <input type="password" placeholder="Password" class="login__input" v-model="password">
            <button type="submit">Login</button>
        </form>
    </div>
</template>
<script setup>
    import axios from 'axios';
    import {ref } from 'vue';
    import {useRouter} from 'vue-router';
    import {useUserStore} from '@/stores/user.js';

    const email = ref("");
    const userStore = useUserStore();
    const password = ref("");
    const router = useRouter();
    const submitForm = async() => {
        try {
            const response = await axios.post('http://localhost:8000/api/login/', {
                username: email.value,
                password: password.value,
            });
    
            // Assuming response.data contains an 'auth_token' field
            const auth_token = response.data.token;
        
            // Use auth_token with userStore
            router.push({path : '/dashboard'})
            userStore.setToken(auth_token, email.value);
            
        } catch (error) {
            console.error('Error logging in:', error);
        }
    }
</script>