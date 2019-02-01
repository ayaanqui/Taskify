<template>
    <div class="new-task-board">
        <form @submit.prevent="addTask()" class="new-task-board-container">
            <div class="task">
                <input v-model="content" class="task-input-controller" name="task" type="text" placeholder="Add a task..." required autofocus autocomplete="off">
            </div>

            <div class="create-task">
                <button class="add-task-btn" v-bind:class="{ 'active' : contentNotEmpty }" type="submit"><span class="icon-add-plus-button"></span></button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    props: [
        "latestTask"
    ],    
    data() {
        return {
            id: 1,
            content: '',
            complete: false,
            date: null
        }
    },
    computed: {
        contentNotEmpty() {
            if (this.content !== "" || this.content) {
                return true;
            }
            return false;
        }
    },
    methods: {
        addTask() {
            if (this.content) {
                if (this.latestTask) {
                    this.id = this.latestTask.id + 1;
                }

                const myTask = {
                    id: this.id,
                    content: this.content,
                    date: new Date(),
                    complete: this.complete
                };
                
                this.$emit('add-task', myTask);
                this.content = '';
            }
        }
    }
}
</script>
