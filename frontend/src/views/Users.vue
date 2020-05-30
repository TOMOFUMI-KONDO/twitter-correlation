<template>
  <div id="users">
    <h1>This is user list</h1>
    <div align="center" class="mt-5">
      <b-form class="form">
        <b-form-group label="Name" label-for="name">
          <b-form-input id="name" type="text" required placeholder="Enter name">
          </b-form-input>
        <b-button block @click="registUser" variant="success">Regist!</b-button>
        </b-form-group>
      </b-form>
    </div>
    <div align="center" class="mt-5">
      <b-list-group>
        <b-list-group-item v-for="(user, index) in users" :key="index">
          id: {{user.id}}, name: {{user.name}}
          <b-button :src="user.id" block @click="deleteUser(index, user.id)">Delete</b-button>
        </b-list-group-item>
      </b-list-group>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      users: []
    }
  },
  methods: {
    getUsers () {
      const path = 'http://localhost:5000/api/get/'
      axios.get(path)
        .then(response => {
          this.users = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    registUser () {
      const path = 'http://localhost:5000/api/regist/'
      const name = document.getElementById('name')
      const params = new URLSearchParams()
      params.append('name', name.value)
      const nameValue = name.value
      name.value = ''
      axios.post(path, params)
        .then(response => {
          const id = response.data
          const task = { id: id, name: nameValue }
          this.users.unshift(task)
          alert(`Regist success! \n id: ${id}, name: ${nameValue}`)
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteUser (userIndex, userId) {
      console.log(userIndex)
      console.log(userId)
      const path = 'http://localhost:5000/api/delete/'
      const params = new URLSearchParams()
      params.append('id', userId)
      this.users.splice(userIndex, 1)
      axios.post(path, params)
        .then(response => {
          console.log(response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getUsers()
  }
}
</script>

<style lang="scss">
  .form, .list-group {
    max-width: 200px;
    width: 90%;
  }
</style>
