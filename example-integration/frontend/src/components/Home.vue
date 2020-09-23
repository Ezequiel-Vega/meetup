<template lang="html">
    <div>
        <h1> {{message}} </h1>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Home',
    data() {
        return {
            message: 'Nuevo mensaje con Vue.js'
        }
    },
    methods: {
        getMessage() {
            const path = 'http://localhost:3000/api/v1/message'
            axios.get(path).then((res) => {
                this.message = res.data
            })
            .catch((err) => {
                console.error(err)
            })
        }
    },
    created() {
        this.getMessage()
    }
}
</script>

<style lang="css" scoped>
    
</style>