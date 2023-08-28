<script setup>
import { onMounted, onUnmounted, watch, ref, watchEffect } from "vue";
import moment from "moment";
import Stat from "./components/Stat.vue";
import Stats from "./components/Stats.vue";
import VueTailwindDatepicker from 'vue-tailwind-datepicker'

import Cookies from "js-cookie";

const date = ref();

const api_url = `https://weather-station-api.jacksalici.workers.dev/`;
const daily_api_url = `https://weather-station-api.jacksalici.workers.dev/?mode=history&start_date=${encodeURIComponent(
  moment().subtract(24, "hours").format("YYYY-MM-DD HH:mm:ss")
)}&end_date=${encodeURIComponent(moment().format("YYYY-MM-DD HH:mm:ss"))}`;

var daily_query = ref({
  code: 0,
  msg: "success",
  time: "1684187731",
  data: {
    outdoor: {
      temperature: {
        unit: "℃",
        list: {
          "0000000000": "0.0",
        },
      },
      feels_like: {
        unit: "℃",
        list: {
          "0000000000": "0.0",
        },
      },
      app_temp: {
        unit: "℃",
        list: {
          "0000000000": "0.0",
        },
      },
      dew_point: {
        unit: "℃",
        list: {
          "0000000000": "0.0",
        },
      },
      humidity: {
        unit: "%",
        list: {
          "0000000000": "0.0",
        },
      },
    },
    indoor: {
      temperature: {
        unit: "℃",
        list: {
          "0000000000": "0.0",
        },
      },
      humidity: {
        unit: "%",
        list: {
          "0000000000": "0.0",
        },
      },
    },
    solar_and_uvi: {
      solar: {
        unit: "W\/m²",
        list: {
          "0000000000": "0.0",
        },
      },
      uvi: {
        unit: "",
        list: {
          "0000000000": "0.0",
        },
      },
    },
    rainfall: {
      rain_rate: {
        unit: "mm\/hr",
        list: {
          "0000000000": "0.0",
        },
      },
      daily: {
        unit: "mm",
        list: {
          "0000000000": "0.0",
        },
      },
      event: {
        unit: "mm",
        list: {
          "0000000000": "0.0",
        },
      },
      hourly: {
        unit: "mm",
        list: {
          "0000000000": "0.0",
        },
      },
      weekly: {
        unit: "mm",
        list: {
          "0000000000": "0.0",
        },
      },
      monthly: {
        unit: "mm",
        list: {
          "0000000000": "0.0",
        },
      },
      yearly: {
        unit: "mm",
        list: {
          "0000000000": "0.0",
        },
      },
    },
    wind: {
      wind_speed: {
        unit: "km\/h",
        list: {
          "0000000000": "0.0",
        },
      },
      wind_gust: {
        unit: "km\/h",
        list: {
          "0000000000": "0.0",
        },
      },
      wind_direction: {
        unit: "º",
        list: {
          "0000000000": "0.0",
        },
      },
    },
  },
  pressure: {
    relative: {
      unit: "mmHg",
      list: {
        "0000000000": "0.0",
      },
    },
    absolute: {
      unit: "mmHg",
      list: {
        "0000000000": "0.0",
      },
    },
  },
});

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

var showMoreData = ref(
  Cookies.get("showMoreData") != undefined ? Cookies.get("showMoreData") : false
);

const tab_daily_active = ref(true); //1 is daily, 0 is historic

async function updateData() {
  loading.value = { status: true, text: "Loading..." };
  const res = await fetch(api_url);
  istant_query.value = await res.json();
  const res_d = await fetch(daily_api_url);
  daily_query.value = await res_d.json();
  console.log(istant_query.value);
  console.log(daily_query.value);
  loading.value = {
    status: false,
    text: `Updated at ${moment(istant_query.value.time * 1000).format(
      "HH:mm"
    )}`,
  };
}

function lastTime(list) {
  return String(Math.max(Object.keys(list).map((key) => parseInt(key))));
}

const batteryLevels = ["Normal", "Low"];

watchEffect(async () => {
  updateData();
});

watchEffect(async () => {
  console.log(date.value)
});
</script>

<template>
  <div class="container mx-auto p-4 min-h-screen flex flex-col">
    <div
      class="flex justify-between mb-12 flex-col items-start gap-3 md:items-center md:flex-row"
    >
      <div class="flex space-x-3 flex-row-reverse md:flex-row">
        <div class="w-full">
          <h1 class="text-3xl font-bold">Weather Data</h1>
          <h2 class="text-lg">
            <img
              class="inline w-6"
              src="https://img.icons8.com/fluency/48/place-marker.png"
            />Mirandola, Modena, Italy
          </h2>

          <span
            class="badge badge-md"
            :class="{
              'badge-primary': loading.status,
              'badge-ghost': !loading.status,
            }"
          >
            {{ loading.text }}
          </span>
        </div>
      </div>

    </div>

    <!-- CURRENT DATA -->
    <div>
      <Stats>
        <!--RAIN-->
        <Stat
          title="Instant rainfall rate"
          icon="hygrometer"
          :value="istant_query.data.rainfall.rain_rate.value"
          unit="mm/h"
          :description="
            'in the last 5 min. <br /> Hourly: ' +
            istant_query.data.rainfall.hourly.value +
            istant_query.data.rainfall.hourly.unit +
            '<br /> Daily: ' +
            istant_query.data.rainfall.daily.value +
            istant_query.data.rainfall.daily.unit
          "
          :chart="daily_query.data.rainfall.rain_rate.list"
        />

        <Stat
          title="Total rainfall event"
          icon="rain"
          :value="istant_query.data.rainfall.event.value"
          :unit="istant_query.data.rainfall.event.unit"
          :description="
            'Weekly: ' +
            istant_query.data.rainfall.weekly.value +
            istant_query.data.rainfall.weekly.unit +
            '<br />Monthly: ' +
            istant_query.data.rainfall.monthly.value +
            istant_query.data.rainfall.monthly.unit +
            '<br />Yearly: ' +
            istant_query.data.rainfall.yearly.value +
            istant_query.data.rainfall.yearly.unit
          "
          :chart="daily_query.data.rainfall.event.list"
          hide-min-max
        />

        <!--OUTDOOR STATS-->
        <Stat
          title="Outdoor temperature"
          icon="temperature-outside"
          :value="istant_query.data.outdoor.temperature.value"
          unit="°C"
          :description="
            'Dew point: ' + istant_query.data.outdoor.dew_point.value + '°C'
          "
          :chart="daily_query.data.outdoor.temperature.list"
        />

        <Stat
          title="Outdoor humidity"
          icon="barometer-gauge"
          :value="istant_query.data.outdoor.humidity.value"
          :unit="istant_query.data.outdoor.humidity.unit"
          :description="
            'Abs. Pressure: ' +
            istant_query.data.pressure.absolute.value +
            istant_query.data.pressure.absolute.unit
          "
          :chart="daily_query.data.outdoor.humidity.list"
        />

        <!--SOLAR AND UVI-->
        <Stat
          title="Solar Irradiance"
          icon="solar-energy"
          :value="istant_query.data.solar_and_uvi.solar.value"
          :unit="istant_query.data.solar_and_uvi.solar.unit"
          :chart="daily_query.data.solar_and_uvi.solar.list"
          :description="
            'UV Index: ' + istant_query.data.solar_and_uvi.uvi.value + '<br/>'
          "
        />

        <!--WIND-->
        <Stat
          title="Wind speed and direction"
          icon="windsock"
          :value="istant_query.data.wind.wind_speed.value"
          :unit="istant_query.data.wind.wind_speed.unit"
          :description="
            'Wind Gust: ' +
            istant_query.data.wind.wind_gust.value +
            istant_query.data.wind.wind_gust.unit +
            '<br/> Wind Direction: ' +
            istant_query.data.wind.wind_direction.value +
            istant_query.data.wind.wind_direction.unit
          "
          :chart="daily_query.data.wind.wind_speed.list"
        />
      </Stats>
    </div>


    <!-- FOOTER AND OTHER DATA -->
    <footer class="footer footer-center mt-auto">
      <div class="text-base-content opacity-40 text-xs mt-10">
        <p>
          Developed and designed by
          <a class="font-bold" href="https://jacksalici.com">jacksalici</a
          >.<br />© {{ moment().format("YYYY") }} MIT Licence - Icons by
          <a class="link" href="https://icons8.com/">Icons8</a><br />
          Check the project on
          <a class="link" href="https://github.com/jacksalici/weather_station"
            >GitHub</a
          >.
        </p>
      </div>
    </footer>
  </div>
</template>
