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
              src="https://img.icons8.com/fluency/administrative-tools.png"
              alt="settings"
            />
            Settings</label
          >
        </li>
        <li>
          <label class="flex-1" for="show-about-modal"
            ><img
              class="h-8"
              src="https://img.icons8.com/fluency/about.png"
              alt="about"
            />
            About</label
          >
        </li>
      </ul>
    </div>
  </div>


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
        the<a class="link" href="https://github.com/jacksalici/weather_station"
          >project repo</a
        >.
        
      </p>
    </label>
  </label>




</template>