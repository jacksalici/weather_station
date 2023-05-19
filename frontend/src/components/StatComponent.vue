<script setup>
import { Line } from "vue-chartjs";
import moment from "moment";


import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  PointElement,
  LineElement,
  CategoryScale,
  LinearScale,
Colors,
} from "chart.js";
ChartJS.register(
  Title,
  Tooltip,
  Legend,
  PointElement,
  LineElement,
  CategoryScale,
  LinearScale,
  Colors
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


const chartOptions = {
  responsive: true,
  scales: {
      x: {
        display: false,
        title: {
          display: false
        }
      },
      y: {
        display: true,
        title: {
          display: false,
          
        },
        
        
      }
    },
  plugins: {
    legend:{
    display: false
  }}
};

const chartData = {
  labels: Object.keys(props.chart).map(label => {return moment.unix(label).format("HH:mm")}),
  datasets: [
    {
      lavel: props.title,
      data: Object.values(props.chart),
      tension: 0.4,
      pointStyle: false,
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


