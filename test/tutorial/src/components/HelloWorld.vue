<script setup>

console.log("hello princeton")

import { ref } from 'vue'

import { reactive } from "vue"

const state = reactive({
      name: "Por",
    })

defineProps({
  msg: String,
})

const count = ref(0);

const incrementCount = () => {

  console.log("click")
  fetch(`/increment/${count.value}`)
    .then((response) => {
      if (response.ok) {
        return response.text();
      } else {
        throw new Error(`${response.status} ${response.statusText}`);
      }
    })
    .then((val) => {
      count.value = parseInt(val);
    })
    .catch((error) => {
      console.error(`Error: ${error.message}`);
    });
};


const talker = () => {

  console.log("talk flask")
  fetch(`/talk/`)
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error(`${response.status} ${response.statusText}`);
      }
    })
    .then((val) => {
      console.log(response["author"])
      state.name = response["author"];
    })
    .catch((error) => {

      console.error(`Error: ${error.message}`);
    });

  
}

</script>

<template>
  <h1>{{ msg }}</h1>

<div class="card">
  <button type="button" @click="incrementCount">count asdf is {{ count }}</button>
  <p>
    Edit
    <code>components/HelloWorld.vue</code> to test HMR
  </p>
</div>

<div class = "talker" @click="talker">

Hello new component here {{ state.name }}  Por
</div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank"
      >create-vue</a
    >, the official Vue + Vite starter
  </p>
  <p>
    Install
    <a href="https://github.com/vuejs/language-tools" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click oasdfn the Vite and Vue logos to learn more</p>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>


