<script setup>
import { onMounted, onUnmounted, watch, ref, watchEffect } from "vue";
import moment from "moment";
import Stat from "./components/Stat.vue";
import Stats from "./components/Stats.vue";

import Cookies from "js-cookie";

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
          list: {
            "0000000000": "0.0",
          },
        },
      },
    },
    wind: {
      wind_speed: {
        unit: "km\/h",
        list: {
          list: {
            "0000000000": "0.0",
          },
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
</script>

<template>
  <div class="container mx-auto p-4">
    <!-- MAIN DATA -->
    <div
      class="flex justify-between mb-12 flex-col items-start gap-3 md:items-center md:flex-row"
    >
      <div>
        <h1 class="text-3xl font-bold">Instant Weather Data</h1>
        <h2 class="text-lg opacity-70"><img class="inline w-6" src="https://img.icons8.com/fluency/48/place-marker.png"/>Mirandola, Modena, Italy</h2>
      </div>

      <button
        class="btn btn-xs btn-ghost no-animation p-0"
        :class="{ loading: loading.status }"
      >
        {{ loading.text }}
      </button>
    </div>

    <Stats>
      <!--RAIN-->
      <Stat
        title="Current rainfall rate"
        icon="hygrometer"
        :value="istant_query.data.rainfall.rain_rate.value"
        :unit="istant_query.data.rainfall.rain_rate.unit"
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
      />

      <!--OUTDOOR STATS-->
      <Stat
        title="Outdoor temperature"
        icon="temperature-outside"
        :value="istant_query.data.outdoor.temperature.value"
        :unit="istant_query.data.outdoor.temperature.unit"
        :description="
          'Dew point: ' +
          istant_query.data.outdoor.dew_point.value +
          istant_query.data.outdoor.dew_point.unit
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
        icon="brightness-settings"
        :value="istant_query.data.solar_and_uvi.solar.value"
        :unit="istant_query.data.solar_and_uvi.solar.unit"
        :chart="daily_query.data.solar_and_uvi.solar.list"
      />
      <Stat
        title="UV Index"
        icon="solar-energy"
        :value="istant_query.data.solar_and_uvi.uvi.value"
        :unit="istant_query.data.solar_and_uvi.uvi.unit"
        :chart="daily_query.data.solar_and_uvi.uvi.list"
      />

      <!--WIND-->
      <Stat
        title="Wind speed"
        icon="windsock"
        :value="istant_query.data.wind.wind_speed.value"
        :unit="istant_query.data.wind.wind_speed.unit"
        :description="
          'Wind Gust: ' +
          istant_query.data.wind.wind_gust.value +
          istant_query.data.wind.wind_gust.unit
        "
        :chart="daily_query.data.wind.wind_speed.list"
      />

      <Stat
        title="Wind direction"
        icon="wind-rose"
        :value="istant_query.data.wind.wind_direction.value"
        :unit="istant_query.data.wind.wind_direction.unit"
        :chart="daily_query.data.wind.wind_direction.list"
      />
    </Stats>

    <!-- OTHER DATA -->

    <!--
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
    INDOOR STATS
    <div
      class="stats stats-vertical md:stats-horizontal shadow-xl"
      v-if="showMoreData"
    >
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
        icon="medium-battery"
        :value="
          batteryLevels[parseInt(istant_query.data.battery.sensor_array.value)]
        "
      />
    </div>
  </div>

  -->
    <!-- FOOTER AND OTHER DATA -->
    <footer class="footer footer-center mt-10">
      <div class="text-base-content opacity-40 text-xs">
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