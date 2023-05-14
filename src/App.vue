<script setup>
import { onMounted, onUnmounted, watch, ref, watchEffect } from "vue";
import moment from "moment"

const api_url = `https://weather-station-api.jacksalici.workers.dev/`;

var istant_query = ref({
  code: 0,
  msg: "success",
  time: "0",
  data: {
    outdoor: {
      temperature: { time: " ", unit: " ", value: "0" },
      feels_like: { time: " ", unit: " ", value: "0" },
      app_temp: { time: " ", unit: " ", value: "0" },
      dew_point: { time: " ", unit: " ", value: "0" },
      humidity: { time: " ", unit: " ", value: "0" },
    },
    indoor: {
      temperature: { time: " ", unit: " ", value: "0" },
      humidity: { time: " ", unit: " ", value: "0" },
    },
    solar_and_uvi: {
      solar: { time: " ", unit: " ", value: "0" },
      uvi: { time: " ", unit: "", value: "0" },
    },
    rainfall: {
      rain_rate: { time: " ", unit: " ", value: "0" },
      daily: { time: " ", unit: " ", value: "0" },
      event: { time: " ", unit: " ", value: "0" },
      hourly: { time: " ", unit: " ", value: "0" },
      weekly: { time: " ", unit: " ", value: "0" },
      monthly: { time: " ", unit: " ", value: "0" },
      yearly: { time: " ", unit: " ", value: "0" },
    },
    wind: {
      wind_speed: { time: " ", unit: " ", value: "0" },
      wind_gust: { time: " ", unit: " ", value: "0" },
      wind_direction: { time: " ", unit: " ", value: "0" },
    },
    pressure: {
      relative: { time: " ", unit: " ", value: "0" },
      absolute: { time: " ", unit: " ", value: "0" },
    },
    battery: { sensor_array: { time: " ", unit: " ", value: "0" } },
  },
});

var loading = ref({status: true, text:"Loading..."});



async function updateData(){
  loading.value = {status: true, text:"Loading..."};
  const res = await fetch(api_url);
  istant_query.value = await res.json();
  console.log(istant_query);
  loading.value = {status: false, text:`Updated at ${moment(istant_query.value.time * 1000).format('HH:mm')}`};
}


watchEffect(async () => {
  updateData()
  
});


onUnmounted(() => {
  cancelAnimationFrame(handle)
})

</script>

<template>
  <div class="navbar bg-base-100">
    <div class="flex-1">
      <a class="btn btn-ghost normal-case text-xl">Mirandola Weather Station</a>
    </div>
    <div class="dropdown dropdown-end">
      <label tabindex="0" class="btn btn-ghost btn-square">
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
        </svg>      </label>
      <ul tabindex="0" class="menu menu-compact dropdown-content  p-2 shadow-xl bg-base-100 rounded-box w-36">
        <li><label class="flex-1" for="my-modal-6"><img
              class="h-8"
              src="https://img.icons8.com/fluency/administrative-tools.svg"
              alt="settings"
            /> Settings</label></li>
        <li><a><img
              class="h-8"
              src="https://img.icons8.com/fluency/about.svg"
              alt="about"
            /> About</a></li>
            
      </ul>
    </div>
  </div>

  <h1 class="text-2xl font-bold m-2 mb-4 bg-base-100 shadow-xl p-5 rounded-xl">
    Istant Data
    <span class="btn btn-xs btn-ghost no-animation" @click="updateData" :class="{ loading : loading.status }"
      >{{loading.text}}</span
    >
  </h1>

  <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 m-2">
    <!--RAIN-->
    <div class="stats stats-vertical md:stats-horizontal shadow-xl">
      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-16">
            <img
              src="https://img.icons8.com/fluency/hygrometer.svg"
              alt="hygrometer"
            />
          </div>
        </div>
        <div class="stat-title">Current rainfall rate</div>
        <div class="stat-value">
          {{ istant_query.data.rainfall.rain_rate.value }}
          <span class="text-sm">{{
            istant_query.data.rainfall.rain_rate.unit
          }}</span>
        </div>
        <div class="stat-desc">
          in the last 5 min. <br />
          Hourly: {{ istant_query.data.rainfall.hourly.value }}
          {{ istant_query.data.rainfall.hourly.unit }}
        </div>
      </div>

      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-16">
            <img src="https://img.icons8.com/fluency/rain.svg" alt="rain" />
          </div>
        </div>
        <div class="stat-title">Total rainfall event</div>
        <div class="stat-value">
          {{ istant_query.data.rainfall.event.value }}
          <span class="text-sm">{{
            istant_query.data.rainfall.event.unit
          }}</span>
        </div>
        <div class="stat-desc">
          Weekly: {{ istant_query.data.rainfall.weekly.value }}
          {{ istant_query.data.rainfall.weekly.unit }}<br />Monthly:
          {{ istant_query.data.rainfall.monthly.value }}
          {{ istant_query.data.rainfall.monthly.unit }}<br />Yearly:
          {{ istant_query.data.rainfall.yearly.value }}
          {{ istant_query.data.rainfall.yearly.unit }}
        </div>
      </div>
    </div>

    <!--OUTDOOR STATS-->
    <div class="stats stats-vertical md:stats-horizontal shadow-xl">
      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-16">
            <img
              src="https://img.icons8.com/fluency/temperature-outside.svg"
              alt="temperature-outside"
            />
          </div>
        </div>
        <div class="stat-title">Outdoor temperature</div>
        <div class="stat-value">
          {{ istant_query.data.outdoor.temperature.value }}
          <span class="text-sm">{{
            istant_query.data.outdoor.temperature.unit
          }}</span>
        </div>
        <div class="stat-desc">
          Dew point: {{ istant_query.data.outdoor.dew_point.value
          }}{{ istant_query.data.outdoor.dew_point.unit }}
        </div>
      </div>

      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-16">
            <img
              src="https://img.icons8.com/fluency/barometer-gauge.svg"
              alt="barometer-gauge"
            />
          </div>
        </div>
        <div class="stat-title">Outdoor humidity</div>
        <div class="stat-value">
          {{ istant_query.data.outdoor.humidity.value }}
          <span class="text-sm">{{
            istant_query.data.outdoor.humidity.unit
          }}</span>
        </div>
        <div class="stat-desc">
          Abs. pressure: {{ istant_query.data.pressure.absolute.value }}
          {{ istant_query.data.pressure.absolute.unit }}
        </div>
      </div>
    </div>

    <!--SOLAR AND UVI-->
    <div class="stats stats-vertical md:stats-horizontal shadow-xl">
      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-16">
            <img
              src="https://img.icons8.com/fluency/brightness-settings.svg"
              alt="brightness"
            />
          </div>
        </div>
        <div class="stat-title">Solar Irradiance</div>
        <div class="stat-value">
          {{ istant_query.data.solar_and_uvi.solar.value }}
          <span class="text-sm">{{
            istant_query.data.solar_and_uvi.solar.unit
          }}</span>
        </div>
        <div class="stat-desc"></div>
      </div>

      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-16">
            <img
              src="https://img.icons8.com/fluency/solar-energy.svg"
              alt="solar-energy"
            />
          </div>
        </div>
        <div class="stat-title">UV Index</div>
        <div class="stat-value">
          {{ istant_query.data.solar_and_uvi.uvi.value }}
          <span class="text-sm">{{
            istant_query.data.solar_and_uvi.uvi.unit
          }}</span>
        </div>
        <div class="stat-desc"></div>
      </div>
    </div>

    <!--WIND-->
    <div class="stats stats-vertical md:stats-horizontal shadow-xl">
      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-16">
            <img
              src="https://img.icons8.com/fluency/windsock.svg"
              alt="windsock"
            />
          </div>
        </div>
        <div class="stat-title">Wind Speed</div>
        <div class="stat-value">
          {{ istant_query.data.wind.wind_speed.value }}
          <span class="text-sm">{{
            istant_query.data.wind.wind_speed.unit
          }}</span>
        </div>
        <div class="stat-desc">
          Gust: {{ istant_query.data.wind.wind_gust.value
          }}{{ istant_query.data.wind.wind_gust.unit }}
        </div>
      </div>

      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-16">
            <img
              src="https://img.icons8.com/fluency/wind-rose.svg"
              alt="windrose"
            />
          </div>
        </div>
        <div class="stat-title">Wind Direction</div>
        <div class="stat-value">
          {{ istant_query.data.wind.wind_direction.value }}
          <span class="text-sm">{{
            istant_query.data.wind.wind_direction.unit
          }}</span>
        </div>
        <div class="stat-desc"></div>
      </div>
    </div>
  </div>

  <h1
    class="text-2xl font-bold m-2 mb-4 mt-6 bg-base-100 shadow-xl p-5 rounded-xl"
  >
    Other Stats
    <span class="btn btn-xs btn-ghost no-animation" @click="updateData" :class="{ loading : loading.status }"
      >{{loading.text}}</span
    >
  </h1>

  <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 m-2">
    <!--INDOOR STATS-->
    <div class="stats stats-vertical md:stats-horizontal shadow-xl">
      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-16">
            <img
              src="https://img.icons8.com/fluency/temperature-inside.svg"
              alt="temperature-inside"
            />
          </div>
        </div>
        <div class="stat-title">Indoor temperature</div>
        <div class="stat-value">
          {{ istant_query.data.indoor.temperature.value }}
          <span class="text-sm">{{
            istant_query.data.indoor.temperature.unit
          }}</span>
        </div>
        <div class="stat-desc">
          Indoor humidity: {{ istant_query.data.indoor.humidity.value
          }}{{ istant_query.data.indoor.humidity.unit }}
        </div>
      </div>
      <div class="stat">
        <div class="stat-figure text-secondary">
          <div class="w-16">
            <img
              src="https://img.icons8.com/fluency/medium-battery.svg"
              alt="battery"
            />
          </div>
        </div>
        <div class="stat-title">Battery Level</div>
        <div class="stat-value">
          <span v-if="istant_query.data.battery.sensor_array.value == '0'"
            >Normal </span
          ><span v-else>Low</span>
        </div>
      </div>
    </div>
  </div>


  <footer class="footer footer-center p-4 bg-base-100 text-base-content">
  <div class="text-base-300">
    <p>Developed and designed by <a class="link font-bold" href="https://jacksalici.com">jacksalici</a><br/>MIT Licence {{ moment().format('YYYY') }} - Icons by <a class="link" href="https://icons8.com/">Icons8</a></p>
  </div>
</footer>

<input type="checkbox" id="my-modal-6" class="modal-toggle" />
<label for="my-modal-6" class="modal cursor-pointer modal-bottom sm:modal-middle">
  <label class="modal-box relative">
    <h3 class="font-bold text-lg">Sort of ettings</h3>
    
    <div class="form-control">
  <label class="label cursor-pointer">
    <span class="label-text">Sow more data</span> 
    <input type="checkbox" class="toggle" />
  </label>
  </div>
  </label>
</label>

</template>
