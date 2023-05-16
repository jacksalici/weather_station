<script setup>
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  PointElement,
  LineElement,
  CategoryScale,
  LinearScale,
} from "chart.js";
ChartJS.register(
  Title,
  Tooltip,
  Legend,
  PointElement,
  LineElement,
  CategoryScale,
  LinearScale
);

const props = defineProps({
  icon: String,
  title: String,
  value: String,
  unit: String,
  description: String,
  chart: {
    type: Object,
    default: {}
  },
});

console.log(props.chart);
let a =  Object.keys(props.chart)
console.log(a)
const chartOptions = {
  responsive: true,
};

const chartData = {
  labels:a,
  datasets: [
    {
      data: Object.values(props.chart),
    },
  ],
};
</script>

<template>
  <div class="stat overflow-hidden">
    <div class="stat-figure text-secondary">
      <div class="w-16">
        <img
          :src="'https://img.icons8.com/fluency/' + icon + '.svg'"
          alt="{{icon}}"
        />
      </div>
    </div>
    <div class="stat-title">{{ title }}</div>
    <div class="stat-value">
      {{ value }}
      <span class="text-sm">{{ unit }}</span>
    </div>
    <div class="stat-desc" v-html="description"></div>
    <div class="stat-actions col-span-2 mt-5" v-if="Object.keys(chart).length">
      <Line :data="chartData" :options="chartOptions" id="Line" />
    </div>
  </div>
</template>
