<template>
    <div class="header">
        <div class="header-inner">
            <router-link :to="{ path: '/' }" class="logo"></router-link>
            
            <div class="menu-items">
                <a href="#" class="btn btn-default btn-sm menu-item">@awesomeuser</a>

                <a href="#" class="btn btn-secondary btn-sm menu-item">Logout</a>
            </div>
        </div>
    </div>
</template>