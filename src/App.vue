<script setup>
import { onMounted, watch, ref, watchEffect } from "vue";

const api_url = `https://weather-station-api.jacksalici.workers.dev/`;

var istant_query = ref({
  code: 0,
  msg: "success",
  time: "0",
  data: {
    outdoor: {
      temperature: { time: " ", unit: " ",     value: "0" },
      feels_like: { time: " ", unit: " ",     value: "0" },
      app_temp: { time: " ", unit: " ",     value: "0" },
      dew_point: { time: " ", unit: " ",     value: "0" },
      humidity: { time: " ", unit: " ",   value: "0" },
    },
    indoor: {
      temperature: { time: " ", unit: " ",     value: "0" },
      humidity: { time: " ", unit: " ",   value: "0" },
    },
    solar_and_uvi: {
      solar: { time: " ", unit: " ",     value: "0" },
      uvi: { time: " ", unit: "",   value: "0" },
    },
    rainfall: {
      rain_rate: { time: " ", unit: " ",     value: "0" },
      daily: { time: " ", unit: " ",     value: "0" },
      event: { time: " ", unit: " ",     value: "0" },
      hourly: { time: " ", unit: " ",     value: "0" },
      weekly: { time: " ", unit: " ",     value: "0" },
      monthly: { time: " ", unit: " ",     value: "0" },
      yearly: { time: " ", unit: " ",     value: "0" },
    },
    wind: {
      wind_speed: { time: " ", unit: " ",     value: "0" },
      wind_gust: { time: " ", unit: " ",     value: "0" },
      wind_direction: { time: " ", unit: " ",     value: "0" },
    },
    pressure: {
      relative: { time: " ", unit: " ",     value: "0" },
      absolute: { time: " ", unit: " ",     value: "0" },
    },
    battery: { sensor_array: { time: " ", unit: " ",   value: "0" } },
  },
});

watchEffect(async () => {
  const res = await fetch(api_url);
  istant_query = await res.json();
  console.log(istant_query);
});
</script>

<template>
  <div class="navbar bg-base-100">
    <div class="flex-1">
      <a class="btn btn-ghost normal-case text-xl">Mirandola Weather Station</a>
    </div>
    <div class="flex-none">
      <button class="btn btn-square btn-ghost">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          class="inline-block w-5 h-5 stroke-current"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"
          ></path>
        </svg>
      </button>
    </div>
  </div>

  <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 m-2">
    <!--RAIN-->
    <div class="stats stats-vertical md:stats-horizzontal shadow-xl">
      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-12">
            <img
              src="https://img.icons8.com/fluency/hygrometer.svg"
              alt="hygrometer"
            />
          </div>
        </div>
        <div class="stat-title">Current rainfall rate</div>
        <div class="stat-value">
          {{ istant_query.data.rainfall.rain_rate.value}}
          <span class="text-sm">mm/h</span>
        </div>
        <div class="stat-desc">
          Last 5 min <br />
          Hourly: 4 mm
        </div>
      </div>

      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-12">
            <img src="https://img.icons8.com/fluency/rain.svg" alt="rain" />
          </div>
        </div>
        <div class="stat-title">Total rainfall event</div>
        <div class="stat-value">
          {{ istant_query.data.rainfall.event.value }} <span class="text-sm">mm</span>
        </div>
        <div class="stat-desc">Weekly: mm<br />Monthly: mm<br />Yearly: mm</div>
      </div>
    </div>

    <!--OUTDOOR STATS-->
    <div class="stats stats-vertical md:stats-horizzontal shadow-xl">
      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-12">
            <img
              src="https://img.icons8.com/fluency/temperature-outside.svg"
              alt="temperature-outside"
            />
          </div>
        </div>
        <div class="stat-title">Outdoor temperature</div>
        <div class="stat-value">31<span class="text-sm">°C</span></div>
        <div class="stat-desc">
          Day <br />
          Hourly: 4 mm
        </div>
      </div>

      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-12">
            <img src="https://img.icons8.com/fluency/wet.svg" alt="wet" />
          </div>
        </div>
        <div class="stat-title">Outdoor humidity</div>
        <div class="stat-value">23 <span class="text-sm">mm</span></div>
        <div class="stat-desc">
          Weekly: 45 mm<br />Monthly: 123 mm<br />Yearly: 234 mm
        </div>
      </div>
    </div>
  </div>
  {{ data }}
</template>
