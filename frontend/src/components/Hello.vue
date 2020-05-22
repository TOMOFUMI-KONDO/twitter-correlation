<template>
  <div id="hello">
    <button class="button" @click="callHello">{{ msg }}</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Hello',
  props: ['msg'],
  methods: {
    callHello () {
      const path = 'http://localhost:5000/api/hello/'
      axios.get(path)
        .then(response => {
          alert(response.data.msg)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style lang="scss">
  .button {
    padding: 10px;

    &:hover {
      background-color: #aaa;
      cursor: pointer;
      outline: none;
    }
  }
</style>
