<template>
    <h1>Kanban</h1>

    <div class="kanban">
        <div 
            class="kanban__row" 
            v-for="row in lowestPriority" 
            :key="row" 
            :style="{ '--hue-count': calcHue(row) }"
            @dragover.prevent
            @drop="handleDrop($event, row)"
        >
            <div 
                class="kanban__task" 
                :data-id="`${task.id}`" 
                v-for="task in filteredTasks(row)" 
                draggable="true"
                @dragstart="handleDragStart($event, task)"
                @dragend="handleDragEnd($event, task)" 
                ref="taskElements"
            >
                <span class="kanban__title">{{task.title}}</span>
                <span class="kanban__desc">{{task.desc}}</span>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const taskElements = ref([]);
const globalPositionObject = ref([]);
const draggedTask = ref(null); // To store the dragged task temporarily

onMounted(() => {
    taskElements.value.forEach(taskElement => {
        if (taskElement) {
            console.log(taskElement.getBoundingClientRect());
            console.log(taskElement.dataset.id);
            globalPositionObject.value.push([
                {
                    x: taskElement.getBoundingClientRect().x,
                    y: taskElement.getBoundingClientRect().y,
                    width: taskElement.getBoundingClientRect().width,
                    height: taskElement.getBoundingClientRect().height
                },
                taskElement.dataset.id
            ]);
        }
    });
    console.log(globalPositionObject.value);
});

const data = ref([
    { id: 0, title: 'Ollie', desc: 'Helloooo mate', priority: 1 },
    { id: 1, title: 'ITALO', desc: 'THis is a test description', priority: 2 },
    { id: 2, title: 'Ellis', desc: 'Ohhhhdknfn dljkfnsdklnfsdknfkldsnf nd k.fsd', priority: 1 },
    { id: 3, title: 'Pietro', desc: 'nfdksnfsdnk i ndfknsdfnsd n', priority: 3 }
]);

const lowestPriority = ref(3);

const calcHue = (count) => {
    return ((count - 1) / 10 * 360) % 360;
};

const filteredTasks = (priority) => {
    return data.value.filter(task => task.priority === priority);
};

const handleDragStart = (event, task) => {
    draggedTask.value = task; // Store the dragged task
    console.log(`Drag started for task: ${task.id}`);
};

const handleDragEnd = (event, task) => {
    console.log(`Drag ended for task: ${task.id}`);
    draggedTask.value = null; // Clear the dragged task after drop
};

const handleDrop = (event, newPriority) => {
    if (draggedTask.value) {
        console.log(`Dropped task ID: ${draggedTask.value.id} to priority: ${newPriority}`);
        draggedTask.value.priority = newPriority; // Update the priority of the dragged task
        // add api call here
    }
};
</script>

<style scoped>
.kanban__row {
    margin-bottom: 20px;
    padding: 10px;
    border: 1px dashed #aaa; /* Optional: Styling for drop zone */
}
.kanban__task {
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 4px;
    cursor: grab;
}
</style>
