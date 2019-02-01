import Vue from 'vue';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;

// import 3rd Party apps
import UUID from 'vue-uuid';

// install 3rd Party apps
Vue.use(UUID);

new Vue({
    router,
    render: h => h(App),
}).$mount('#app');