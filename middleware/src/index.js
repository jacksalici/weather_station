export default {
  async fetch(request, env, ctx) {
    
    
    const { searchParams } = new URL(request.url)
    
    let mode = searchParams.get('mode')
    let start_date = searchParams.get('start_date')
    let end_date = searchParams.get('end_date')

    if (!mode || !start_date || !end_date){
      mode = "real_time"
    }

    const ecowittHost = "https://api.ecowitt.net/api/v3/device/";
    var url = ecowittHost + `${mode}?application_key=${env.ECOWITT_APPLICATION_KEY}&api_key=${env.ECOWITT_API_KEY}&mac=${env.ECOWITT_MAC_ADDRESS}&temp_unitid=1&pressure_unitid=5&wind_speed_unitid=7&solar_irradiance_unitid=16&rainfall_unitid=12`;

    if (mode == 'history'){
      url = url.concat(`&start_date=${start_date}&end_date=${end_date}&cycle_type=auto&call_back=outdoor,indoor,solar_and_uvi,rainfall,wind,pressure`)
    }


    /**
     * gatherResponse awaits and returns a response body as a string.
     * Use await gatherResponse(..) in an async function to get the response body
     * @param {Response} response
     */
    async function gatherResponse(response) {
      const { headers } = response;
      const contentType = headers.get("content-type") || "";
      if (contentType.includes("application/json")) {
        return JSON.stringify(await response.json());
      }
      return response.text();
    }

    const init = {
      headers: {
        "content-type": "application/json;charset=UTF-8",
        "Access-Control-Allow-Origin": '*',

      },
    };

    const response = await fetch(url, init);
    const results = await gatherResponse(response);
    return new Response(results, init);
  },
};