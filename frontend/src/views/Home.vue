<template>
  <div id="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <Hello :msg="'click me!'" />
  </div>
</template>

<script>
// @ is an alias to /src
import Hello from '../components/Hello'

export default {
  name: 'Home',
  components: {
    Hello
  }
}
</script>

<style lang="scss">

</style>
