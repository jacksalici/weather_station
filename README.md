# Ecowitt Weather Station Client

![](/screenshot.png)

A custom front-end and middleware for displaying data from my Ecowitt weather station.  

## Details  

The front-end is built using Vue and relies on Tailwind, DaisyUI and GraphJS for the UI. 
The middleware is a Cloudflare Worker and is needed to hide to the users the token key.

### Frontend Project Setup

```sh
# Install dependencies
npm install

# Compile and Hot-Reload for Development
npm run dev

# Compile and Minify for Production
npm run build

```

### Middleware  

To start developing your Worker, run `npx wrangler dev`
To publish your Worker to the Internet, run `npx wrangler publish`

Environment variables should be put for local dev in a `.dev.vars` file using _dotenv_ format, and then pushed using `npx wrangler secret`.


### API endpoints

- Istant weather data: `https://weather-station-api.jacksalici.workers.dev`  

- Daily weather data (5 minute span from the last 24h):
    ```js
    const api_url = `https://weather-station-api.jacksalici.workers.dev/?mode=history&start_date=${encodeURIComponent(moment().subtract(24, 'hours').format('YYYY-MM-DD HH:mm:ss'))}&end_date=${encodeURIComponent(moment().format('YYYY-MM-DD HH:mm:ss'))};
    ```

