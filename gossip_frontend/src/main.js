import './assets/main.scss';
import { library } from '@fortawesome/fontawesome-svg-core';

// Import specific icons
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';

// Add Font Awesome icons to the library
import { faUser, faCoffee } from '@fortawesome/free-solid-svg-icons';
library.add(faUser, faCoffee);

const app = createApp(App);

// Register FontAwesomeIcon component globally
app.component('font-awesome-icon', FontAwesomeIcon);

app.use(createPinia());
app.use(router);

app.mount('#app');
