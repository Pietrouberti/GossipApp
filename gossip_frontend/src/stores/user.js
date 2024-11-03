import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore({
  id: 'user',
  state: () => ({
      user: {
          isAuthenticated: false,
          name: null,
          token: null
      }
  }),

  actions: {
      initStore() {
          this.user.token = localStorage.getItem('user.token');
          this.user.name = localStorage.getItem('user.name')
          if(this.user.token != null) {
              this.user.isAuthenticated = true
          }
          console.log("Initialised User", this.user)
      },
      setToken(token, name) {
          console.log("Set Token")
          this.user.token = token;
          this.user.name =name;
          this.user.isAuthenticated = true;
          localStorage.setItem('user.token', token)
          localStorage.setItem('user.name', name)
      },
      removeToken() {
          console.log('remove Token')
          this.user.token = null;
          this.user.name = null;
          this.user.isAuthenticated = false;
          localStorage.setItem('user.name', null);
          localStorage.setItem('user.token', null)
      }
  }
})