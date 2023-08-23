/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {},
    fontFamily: {
      sans: ['IBM Plex Sans']
    }
  },
  plugins: [
    require('@tailwindcss/typography'),
    require("daisyui")
  ],

  daisyui:{
    themes: ["light", "dracula"],
    darkTheme:'dracula',
  }
}

