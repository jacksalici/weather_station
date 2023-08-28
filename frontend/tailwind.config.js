/** @type {import('tailwindcss').Config} */
const colors = require("tailwindcss/colors")

module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}',"./node_modules/vue-tailwind-datepicker/**/*.js"],
  theme: {
    extend: {
      colors: {
        "vtd-primary": colors.sky,
        "vtd-secondary": colors.gray,
      }
    },
    fontFamily: {
      sans: ['IBM Plex Sans']
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require("daisyui")
  ],

  daisyui:{
    themes: ["light", "dracula"],
    darkTheme:'dracula',
  }
}

