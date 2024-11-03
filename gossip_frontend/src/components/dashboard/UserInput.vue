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
                    <select name="" id="">Priority
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                    </select>
                </div>
                <div class="userinput__entry">
                    <label for="">@ collaborators</label>
                    <textarea></textarea>
                </div>
            </div>
            <button class="submit">Search</button>
        </form>
    </div>
</template>
<script setup>
import { ref } from 'vue';

const userInput = ref(null);
const toggletooltip = ref(false)

const showToolbar = () => {
    toggletooltip.value = !toggletooltip.value
}


const submitForm = () => {
    console.log("Fire Search")
}
</script>