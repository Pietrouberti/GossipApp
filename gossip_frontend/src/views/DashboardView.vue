<template>
    <div class="dashboard">
        <UserInput></UserInput>
        <KanbanBoard></KanbanBoard>
    </div>
    
</template>
<script setup>
    import UserInput from '@/components/dashboard/UserInput.vue'
    import KanbanBoard from '@/components/dashboard/KanbanBoard.vue'
</script>