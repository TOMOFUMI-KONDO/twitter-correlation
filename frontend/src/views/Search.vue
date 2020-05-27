<template>
  <div id="search">
    <h1>親密度検索</h1>
    <p>動画のツイート履歴からあなたに似ているユーザーを探します。</p>
     <div align="center" class="mt-5">
       <b-form-group label="TwitterId" label-for="TwitterId">
         <b-form-input id="twitterID" type="text" required placeholder="twitterIDを入力してください">
         </b-form-input>
       <b-button block @click="search" variant="検索中…">Search!</b-button>
       </b-form-group>
   </div>
     <div align="center" class="mt-5">
       <b-list-group>
         <p>{{search_user}}さんに似ているユーザーはこんな人たちです</p>
         <b-list-group-item v-for="(user, index) in users" :key="index">
           id: {{user.id}}, name: {{user.name}}
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
      similar_user: [],
      search_user: ''
    }
  },
  methods: {
    search () {
      const path = 'http://localhost:5000/api/search'
      const twitterid = document.getElementById('twitterID')
      const params = new URLSearchParams()
      params.append('id', twitterid.value)
      const IdValue = twitterid.value
      twitterid.value = ''
      this.search_user = IdValue
      axios.post(path, params)
        .then(response => {
          this.similar_user = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
<style lang="scss">
  .form-group,.list-group{
    max-width: 400px;
    width: 90%;
  }
</style>
