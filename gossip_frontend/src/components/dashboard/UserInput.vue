<template>
    <div class="userinput">
        <div class="userinput__title-container">
            <h1 class="userinput__title">Stuck? ask our AI to find you help</h1>
        </div>
        <form class="userinput__form" v-on:submit.prevent="submitForm()">
            <div class="userinput__form-search">
                <input type="text" class="userinput__input" v-model="userInput">
                <button class="userinput__submit" @click.prevent="showToolbar()">+</button>
            </div>
            <div class="userinput__form-tooltip" v-if="toggletooltip">
                <div class="userinput__entry">
                    <label for="checkbox">Discussion: </label>
                    <input type="checkbox" class="userinput__checkbox">
                </div>
                <div class="userinput__entry">
                    <label for="">Priority</label>
                    <select name="" id="" v-model="priority">Priority
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                    </select>
                </div>
                <div class="userinput__entry">
                    <label for="">@collaborators</label>
                    <textarea v-model="collaborators"></textarea>
                </div>
            </div>
            <button class="submit">Search</button>
        </form>
    </div>
</template>
<script setup>
import { ref } from 'vue';
import {useUserStore} from '@/stores/user.js';
import axios from 'axios';
const userStore = useUserStore()

const userInput = ref(null);
const priority = ref(null);
const collaborators = ref(null);
const toggletooltip = ref(false)

const showToolbar = () => {
    toggletooltip.value = !toggletooltip.value
}
function splitStringBySpaces(inputString) {
    return inputString.trim().split(/\s+/);
}

const sendRequest  = async() => {
    let response = axios.post('http://localhost:8000/api/create_message/', {
        headers: {
            'Authorization' : 'token ' + userStore.user.token,
            'Content-Type' : 'application/json'
        },
        text: userInput.value,
        priority: priority.value,
        collaborators: splitStringBySpaces(collaborators.value),
    } )

    return response;
}

const submitForm = async() => {
    let response = await sendRequest();

    console.log("Fire Search", userInput.value, priority.value, collaborators.value, response)
}
</script>