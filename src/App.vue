<template>
    <div class="content">
        <Navbar />

        <div class="main-content content-body">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import Navbar from './components/layout/Navbar';

// CSS
import './assets/css/bootstrap.min.css';
import './assets/css/styles.css';
import './assets/fonts/material-design-icons/font/flaticon.min.css';

export default {
    name: 'App',
    components: {
        Navbar
    }
}
</script>

<style>
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
</style>
