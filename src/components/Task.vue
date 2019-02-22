<template>
    <div class="task-view">
        <div class="checklist">
            <span v-if="!task.complete" @click="$emit('complete-task', task.id)" class="check-not-complete"></span>
            
            <span v-else @click="$emit('complete-task', task.id)" class="check-complete"></span>
        </div>

        <div class="task-details">
            <span v-bind:class="{ 'task-completed' : taskDetailsLineThrough }">{{ task.content }}</span>
        </div>

        <div class="task-controls"><span class="icon-rubbish-bin-delete-button delete-task" @click="$emit('delete-task', task.id)"></span></div>
    </div>
</template>

<script>
export default {
    props: [
        "task"
    ],
    computed: {
        taskDetailsLineThrough() {
            return this.task.complete;
        }
    }
}
</script>

