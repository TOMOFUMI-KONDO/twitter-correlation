<template>
  <div id="search">
    <h1>親密度検索</h1>
    <p>動画のツイート履歴からあなたに似ているユーザーを探します。</p>
    <div align="center" class="mt-5">
      <b-form-group label="" label-for="TwitterId">
        <div class="d-flex align-items-center">
          @<b-form-input id="twitterID" type="text" required placeholder="twitterIDを入力してください" class="ml-1"></b-form-input>
        </div>
        <b-button block @click="search" variant="success" class="mt-3">Search!</b-button>
      </b-form-group>
    </div>
    <div v-if="is_searching">
      <p>searching...</p>
    </div>
    <div align="center" class="mt-5" v-if="is_searched">
      <b-list-group>
        <p><b>@{{search_user}}</b>さんに似ているユーザーはこんな人たちです</p>
        <b-list-group-item v-for="(user, index) in similar_user" :key="index" class="border-0 mb-5">
          <p align="center"><b>{{index+1}}位</b></p>
          <div class="border">
            <a :href="'https://twitter.com/' + user.user_id" class="d-block p-3">
              <p>@{{user.user_id}}</p>
              <p>{{user.name}}</p>
              <p>{{similarity}}</p>
            </a>
          </div>
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
      search_user: '',
      is_searching: false,
      is_searched: false
    }
  },
  methods: {
    search () {
      const path = 'http://localhost:5000/api/search/'
      const twitterid = document.getElementById('twitterID')

      if (twitterid.value === '') {
        alert('twitterIdを入力してください。')
        return
      }

      this.is_searching = true
      this.is_searched = false

      const params = new URLSearchParams()
      params.append('id', twitterid.value)

      const IdValue = twitterid.value
      twitterid.value = ''
      this.search_user = IdValue

      const self = this
      axios.post(path, params)
        .then(response => {
          this.is_searching = false
          this.is_searched = true
          self.similar_user = response.data.ranking
          console.log(self.similar_user)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
<style lang="scss">
  .form-group {
    max-width: 300px;
    width: 90%;

    button {
      max-width: 150px;
      width: 50%;
    }
  }

  .list-group {
    max-width: 500px;
    width: 90%;

    .list-group-item {
      div {
        border-color: rgb(167, 167, 167) !important;

        a {
          color: rgb(33, 37, 41);

          &:hover {
            background-color: darken(#fff, 10%);
            text-decoration: none;
          }
        }
      }
    }
  }
</style>
