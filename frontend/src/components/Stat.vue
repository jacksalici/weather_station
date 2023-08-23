<script setup>
import { Line } from "vue-chartjs";
import moment from "moment";
import {ref, watchEffect} from 'vue';

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
    default: {},
  },
});

const chartOptions = {
  responsive: true,
  scales: {
    x: {
      display: false,
      title: {
        display: false,
      },
    },
    y: {
      display: true,
      title: {
        display: false,
      },
      ticks: {
            mirror: true
         }
    },
  },
  plugins: {
    legend: {
      display: false,
    },
    tooltip: {
        enabled: true,
        position: 'nearest',
       
      }
  },
};

const chartData = ref();

watchEffect(()=>{
  chartData.value = {
  labels: Object.keys(props.chart).map((label) => {
    return moment.unix(label).format("HH:mm");
  }),
  datasets: [
    {
      lavel: props.title,
      data: Object.values(props.chart),
      tension:0.2,
      pointStyle: false,
      cubicInterpolationMode: 'monotone',
    },
  ],
}
})

</script>

<template>
  <div class="card w-full shadow-lg rounded-lg border-2 border-opacity-10 border-base-content">
    <div class="card-body p-0">
      <div class="p-4 sm:p-8 pb-2">
        <div class="card-title">
          {{ title }}
          <img
            :src="'https://img.icons8.com/fluency/' + icon + '.png'"
            :alt="icon"
            class="inline pr-1 h-10"
          />
        </div>
        <div class="text-4xl font-bold">
          {{ value }}
          <span class="text-sm">{{ unit }}</span>
        </div>
        <div class="stat-desc" v-html="description"></div>
      </div>
      <div class="" v-if="Object.keys(chart).length">
        <Line :data="chartData" :options="chartOptions" id="Line" />
      </div>
    </div>
  </div>
</template>
