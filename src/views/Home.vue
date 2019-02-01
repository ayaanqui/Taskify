<template>
    <div class="tasks-board">
        <div class="my-tasks">
            <div v-if="taskList.length !== 0">
                <Task 
                    v-for="task in taskList"
                    :key="task.id"
                    :task="task"
                    v-on:complete-task="completeTask"
                />
            </div>

            <div v-else class="empty-list">
                <h3>Empty List</h3>
                <p>Start adding stuff in here to get more productive!</p>
            </div>
        </div>

        <AddTask v-on:add-task="addTask" :latestTask="taskList[taskList.length-1]" />
    </div>
</template>

<script>
import AddTask from '../components/AddTask';
import Task from '../components/Task';

export default {
    components: {
        AddTask,
        Task
    },
    data() {
        return {
            taskList: []
        }
    },
    methods: {
        addTask(myTask) {
            this.taskList.push(myTask);
        },
        completeTask(id) {
            var task = {};

            for (var i = 0; i < this.taskList.length; i++) {
                task = this.taskList[i];

                if (task.id === id) {
                    this.taskList[i].complete = !task.complete;
                }
            }
        }
    }
}
</script>
