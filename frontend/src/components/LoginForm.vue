<template>
	<v-dialog content-class="login-form">
		<template v-slot:activator="{ on, attrs }">
			<v-btn
			dark
			color="secondary"
			elevation="2"
			v-bind="attrs"
			v-on="on"
			>Login</v-btn>
		</template>
		<v-card class="mt-5 mx-a">
			<v-card-title>
				<h1>Login</h1>
			</v-card-title>
			<v-card-text>
				<v-form>
					<v-text-field
						label="Username"
						prepend-icon="mdi-account-circle"
					/>
					<v-text-field
						:type="showPassword ? 'text' : 'password'"
						label="Password"
						prepend-icon="mdi-lock"
						:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
						@click:append="showPassword = !showPassword"
					/>
				</v-form>
			</v-card-text>
			<v-divider></v-divider>
			<v-card-actions>
				<v-btn color="success">Register</v-btn>
				<v-spacer></v-spacer>
				<v-btn color="info" @click="login()">Login</v-btn>
			</v-card-actions>
		</v-card>
	</v-dialog>
</template>

<style lang="scss">
.login-form {
	width: 25rem !important;
}
</style>

<script lang="ts">
	import Vue from 'vue'

	export default Vue.extend({
		name: 'LoginForm',

		data: () => {
			return {
				showPassword: false,
				loggedIn: false
			}
		},
		methods: {
			async login() {
				console.log('Logging In');
				const { data } = await this.$http.post(
					'/api/login/',
					{ username: 'test', password: 'password' }
				);
				console.log(data);
			}
		}
	});
</script>
