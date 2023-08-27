<script setup>
import { Line } from "vue-chartjs";
import zoomPlugin from 'chartjs-plugin-zoom';
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
  Colors,
  zoomPlugin
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
  chartDot: {
    type: Boolean,
    default: false
  }
});

const chartOptions = {
  responsive: true,
  mantainAspectRatio: false,
  scales: {
    x: {
      display: true,
      title: {
        display: false,
       
      },
      ticks: {
            mirror: false
         }
    },
    y: {
      display: true,
      title: {
        display: false,
      },
      ticks: {
        display: true,
            mirror: false
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
       
      },
      zoom: {
        zoom: {
          wheel: {
            enabled: true,
            modifierKey: 'ctrl',
          },
          pinch: {
            enabled: true
          },
          mode: 'xy',
        },
        limits:{
          x: {min: 0, max: 'original'},
          y: {min: 0, max: 'original'}
        }
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
      label: props.title,
      data: Object.values(props.chart),
      tension:0.4,
      pointStyle: props.chartDot ? true: false,
      cubicInterpolationMode: 'monotone',
    },
  ],
}
})

</script>

<template>
  <div class="card xl:card-side shadow-none rounded-lg border-2 border-primary">
    
    <div class="card-body w-full p-2 m-4 sm:p-4 pb-2">
      
      <div class="card-title items-center mb-2">
        <img
            :src="'https://img.icons8.com/fluency/' + icon + '.png'"
            :alt="icon"
            class="block pr-1 h-12"
          />
          {{ title }}
          
          
        </div>
        <div class="text-4xl font-bold">
          {{ value }}{{ unit }}
        </div>
        <div class="text-xs" v-html="description"></div>
    </div>
      
      <figure class="w-full p-2 h-full" v-if="Object.keys(chart).length">
      <Line :data="chartData" :options="chartOptions" id="Line" />

    </figure>
      
    
  </div>
</template>
