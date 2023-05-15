<script setup>
defineProps(["icon", "title", "value", "unit", "description"]);
</script>

<template>
  <div class="stat overflow-hidden">
    <div class="stat-figure text-secondary">
      <div class="w-16">
        <img :src="'https://img.icons8.com/fluency/'+icon+'.svg'" alt="{{icon}}" />
      </div>
    </div>
    <div class="stat-title">{{ title }}</div>
    <div class="stat-value">
      {{ value }}
      <span class="text-sm">{{ unit }}</span>
    </div>
    <div class="stat-desc" v-html="description"></div>
    <!--<div class="stat-actions col-span-2 -m-10 mt-5">
          <img src="https://images.unsplash.com/photo-1683085809775-d9ac53fcbe21?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2372&q=80"/>
        </div>-->
  </div>
</template>
