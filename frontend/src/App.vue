<template>
  <v-app>
    <v-navigation-drawer app>
      <!-- -->
    </v-navigation-drawer>

    <v-app-bar
      app
      color="primary"
      dark
    >
      <v-switch
        label="Toggle Dark Theme"
        @change="toggleDarkTheme()"
        class="switch-theme"
      ></v-switch>

      <div class="d-flex align-center">
      </div>

      <v-spacer></v-spacer>


      <Login v-if="!loggedIn" />
      <User v-else />
    </v-app-bar>

    <v-main>
      <HelloWorld/>
    </v-main>

    <v-footer app>
      Footer goes here
    </v-footer>
  </v-app>
</template>

<style lang="scss">
.switch-theme {
	margin-top: 1rem !important;
}
</style>

<script lang="ts">
import Vue from 'vue';
import HelloWorld from './components/HelloWorld.vue';
import Login from './components/LoginForm.vue';
import User from './components/User.vue';

export default Vue.extend({
  name: 'App',

  components: {
    HelloWorld,
    Login,
    User
  },

  data: () => ({
    loggedIn: false
  }),

  methods: {
    toggleDarkTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    }
  }
});
</script>
