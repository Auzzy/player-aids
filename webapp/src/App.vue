<template>
  <div id="app">
     <b-container fluid>
        <b-card-group columns>
          <b-card
            v-for="info in games"
            :key="info.id"
            :img-src="info.image"
            img-alt="Image"
            img-top
            @click="openAid(info.name)"
          >
            <b-card-title>{{ info.name }} ({{ info.year }})</b-card-title>
            <b-card-sub-title>by {{ info.designers.join(', ') }}</b-card-sub-title>
          </b-card>
        </b-card-group>
     </b-container>
  </div>
</template>

<script>
export default {
  data(){
    return {
      games: []
    };
  },
  async created() {
    const gResponse = await fetch(`${process.env.VUE_APP_API_URL}/games`);
    const gObject = await gResponse.json();
    this.games = gObject.games;
  },
  methods: {
    openAid: function(game) {
      console.log(`CLICK ${game}`);
      return {"name": game };
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
