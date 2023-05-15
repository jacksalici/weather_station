<script setup>
import { onMounted, onUnmounted, watch, ref, watchEffect } from "vue";
import moment from "moment";
import StatComponent from "./components/StatComponent.vue";
import Cookies from "js-cookie"


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

var loading = ref({ status: true, text: "Loading..." });

var showMoreData = ref(Cookies.get("showMoreData")!=undefined ? Cookies.get("showMoreData") : false);

watch(showMoreData, ()=>{
    Cookies.set("showMoreData", showMoreData.value, { expires: 350 })
  }, { immediate: true })



async function updateData() {
  loading.value = { status: true, text: "Loading..." };
  const res = await fetch(api_url);
  istant_query.value = await res.json();
  console.log(istant_query);
  loading.value = {
    status: false,
    text: `Updated at ${moment(istant_query.value.time * 1000).format(
      "HH:mm"
    )}`,
  };
}



const batteryLevels = ["Normal", "Low"]

watchEffect(async () => {
  updateData();
});

onUnmounted(() => {
  cancelAnimationFrame(handle);
});
</script>

<template>
  <!--NAVBAR-->
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
        </svg>
      </label>
      <ul
        tabindex="0"
        class="menu menu-compact dropdown-content p-2 shadow-xl bg-base-100 rounded-box w-36"
      >
        <li>
          <label class="flex-1" for="show-more-data-modal"
            ><img
              class="h-8"
              src="https://img.icons8.com/fluency/administrative-tools.svg"
              alt="settings"
            />
            Settings</label
          >
        </li>
        <li>
          <label class="flex-1" for="show-about-modal"
            ><img
              class="h-8"
              src="https://img.icons8.com/fluency/about.svg"
              alt="about"
            />
            About</label
          >
        </li>
      </ul>
    </div>
  </div>

  <!-- MAIN DATA -->
  <h1 class="text-2xl font-bold m-2 mb-4 bg-base-100 shadow-xl p-5 rounded-xl">
    Istant Data
    <span
      class="btn btn-xs btn-ghost no-animation"
      :class="{ loading: loading.status }"
      >{{ loading.text }}</span
    >
  </h1>

  <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 m-2">
    <!--RAIN-->
    <div class="stats stats-vertical md:stats-horizontal shadow-xl">
      <StatComponent
        title="Current rainfall rate"
        icon="hygrometer"
        :value="istant_query.data.rainfall.rain_rate.value"
        :unit="istant_query.data.rainfall.rain_rate.unit"
        :description="
          'in the last 5 min. <br /> Hourly: ' +
          istant_query.data.rainfall.hourly.value +
          istant_query.data.rainfall.hourly.unit + '<br /> Daily: ' +
          istant_query.data.rainfall.daily.value +
          istant_query.data.rainfall.daily.unit
        "
      />

      <StatComponent
        title="Total rainfall event"
        icon="rain"
        :value="istant_query.data.rainfall.event.value"
        :unit="istant_query.data.rainfall.event.unit"
        :description="
          'Weekly: ' + istant_query.data.rainfall.weekly.value +
          istant_query.data.rainfall.weekly.unit + '<br />Monthly: ' +
          istant_query.data.rainfall.monthly.value +
          istant_query.data.rainfall.monthly.unit + '<br />Yearly: ' +
          istant_query.data.rainfall.yearly.value +
          istant_query.data.rainfall.yearly.unit
        "
      />
    </div>

    <!--OUTDOOR STATS-->
    <div class="stats stats-vertical md:stats-horizontal shadow-xl">
      <StatComponent
        title="Outdoor temperature"
        icon="temperature-outside"
        :value="istant_query.data.outdoor.temperature.value"
        :unit="istant_query.data.outdoor.temperature.unit"
        :description="
          'Dew point: ' +
          istant_query.data.outdoor.dew_point.value +
          istant_query.data.outdoor.dew_point.unit 
        "
      />
      
      <StatComponent
        title="Outdoor humidity"
        icon="barometer-gauge"
        :value="istant_query.data.outdoor.humidity.value"
        :unit="istant_query.data.outdoor.humidity.unit"
        :description="
          'Abs. Pressure: ' +
          istant_query.data.pressure.absolute.value +
          istant_query.data.pressure.absolute.unit 
        "
      />
    
    </div>

    <!--SOLAR AND UVI-->
    <div class="stats stats-vertical md:stats-horizontal shadow-xl">
      
      <StatComponent
        title="Solar Irradiance"
        icon="brightness-settings"
        :value="istant_query.data.solar_and_uvi.solar.value"
        :unit="istant_query.data.solar_and_uvi.solar.unit"
      />
      <StatComponent
        title="UV Index"
        icon="solar-energy"
        :value="istant_query.data.solar_and_uvi.uvi.value"
        :unit="istant_query.data.solar_and_uvi.uvi.unit"
      />

    </div>

    <!--WIND-->
    <div class="stats stats-vertical md:stats-horizontal shadow-xl">
      <StatComponent
        title="Wind speed"
        icon="windsock"
        :value="istant_query.data.wind.wind_speed.value"
        :unit="istant_query.data.wind.wind_speed.unit"
        :description="
        'Wind Gust: ' +
        istant_query.data.wind.wind_gust.value +
        istant_query.data.wind.wind_gust.unit
        "
      />
      
      <StatComponent
        title="Wind speed"
        icon="wind-rose"
        :value="istant_query.data.wind.wind_direction.value"
        :unit="istant_query.data.wind.wind_direction.unit"
      />
     
    </div>
  </div>

   <!-- OTHER DATA -->
  <h1
    class="text-2xl font-bold m-2 mb-4 mt-6 bg-base-100 shadow-xl p-5 rounded-xl"
    v-if="showMoreData"
  >
    Other Stats
    <span
      class="btn btn-xs btn-ghost no-animation"
      :class="{ loading: loading.status }"
      >{{ loading.text }}</span
    >
  </h1>

  <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 m-2" v-if="showMoreData">
    <!--INDOOR STATS-->
    <div class="stats stats-vertical md:stats-horizontal shadow-xl" v-if="showMoreData">
      <StatComponent
        title="Inside temperature"
        icon="temperature-inside"
        :value="istant_query.data.indoor.temperature.value"
        :unit="istant_query.data.indoor.temperature.unit"
        :description="
        'Indoor humidity: ' +
        istant_query.data.indoor.humidity.value +
        istant_query.data.indoor.humidity.unit
        "
      />
      
      <StatComponent
        title="Battery Level"
        icon="battery"
        :value="batteryLevels[parseInt(istant_query.data.battery.sensor_array.value)]"
      />
  </div>
  </div>

  
  <!-- FOOTER AND OTHER DATA -->
  <footer class="footer footer-center p-4 bg-base-100 text-base-content">
    <div class="text-base-300">
      <p>
        Developed and designed by
        <a class="link font-bold" href="https://jacksalici.com">jacksalici</a
        ><br />MIT Licence {{ moment().format("YYYY") }} - Icons by
        <a class="link" href="https://icons8.com/">Icons8</a>
      </p>
    </div>
  </footer>

  <input type="checkbox" id="show-more-data-modal" class="modal-toggle" />
  <label
    for="show-more-data-modal"
    class="modal cursor-pointer modal-bottom sm:modal-middle"
  >
    <label class="modal-box relative">
      <h3 class="font-bold text-lg">Sort of settings</h3>

      <div class="form-control">
        <label class="label cursor-pointer">
          <span class="label-text">Show more data</span>
          <input type="checkbox" class="toggle" v-model="showMoreData" />
        </label>
      </div>
    </label>
  </label>

  <input type="checkbox" id="show-about-modal" class="modal-toggle" />
  <label
    for="show-about-modal"
    class="modal cursor-pointer modal-bottom sm:modal-middle"
  >
    <label class="modal-box relative">
      <h3 class="font-bold text-lg">About</h3>
      <p class="font-sm">
        I didn't have any clue what to write here. If you are a developer check
        the
        <a class="link" href="https://github.com/jacksalici/weather_station"
          >project repo</a
        >.
      </p>
    </label>
  </label>
</template>
