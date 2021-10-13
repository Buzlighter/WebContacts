<template>
    <div>
      <p>{{ users }}</p>
    </div>
</template>
<script>
    import axios from 'axios'

    export default {
        name: 'Users',
        data() {
            return {
              users: [],
            };
        },
        created() {
          const path = 'http://localhost:5000/users'
            axios.get(path).then(res => {
                   this.users = res.data
            })

        }
    };
</script>
