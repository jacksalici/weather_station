export default {
  async fetch(request, env, ctx) {
    /**
     * Example someHost is set up to take in a JSON request
     * Replace url with the host you wish to send requests to
     * @param {string} someHost the host to send the request to
     * @param {string} url the URL to send the request to
     */
    const ecowittHost = "https://api.ecowitt.net/api/v3/device/";
    const url = ecowittHost + `real_time?application_key=${env.ECOWITT_APPLICATION_KEY}&api_key=${env.ECOWITT_API_KEY}&mac=${env.ECOWITT_MAC_ADDRESS}&temp_unitid=1&pressure_unitid=5&wind_speed_unitid=7&solar_irradiance_unitid=16&rainfall_unitid=12`;

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