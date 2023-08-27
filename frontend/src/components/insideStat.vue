<template>
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

  
</template>