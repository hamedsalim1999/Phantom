<template>
<main>
  <div class="album py-5 bg-light" >
    <div class="container">
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
        <div class="col" v-for="info in infos" v-bind:key ="info.id">
          <div class="card shadow-sm">
            <img :src="info.image" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">{{info.name}}</h5>
                <p class="card-text">{{info.description}}</p>
              </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</main>








</template>

<script>

import axios from 'axios'
export default {
  data () {
    return {
      infos:[]
    }
  },
  mounted () {
this.getCard()
  },
methods:{
  getCard(){
  axios({
    method:'get',
    url:'http://127.0.0.1:8000/',
    auth:{
      username:'hamed',
      password:'hamed123'
    }
  }).then(res => this.infos = res.data)
}
  }
  }

</script>
<style>

      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }

</style>
