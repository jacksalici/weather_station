from flask import Flask, request
from deta import Deta
from dotenv import dotenv_values
    

app = Flask(__name__)

@app.route("/")
def root():
    return "Ecowitt Service on Deta"

@app.route('/data/report/', methods=["POST"] )
def handle_post():
    return_data_keys_old_names=['dateutc', 'tempinf', 'humidityin', 'baromrelin', 'baromabsin', 'tempf', 'humidity', 'winddir', 'windspeedmph', 'windgustmph', 'maxdailygust', 'solarradiation', 'uv', 'rainratein', 'eventrainin', 'hourlyrainin', 'dailyrainin', 'weeklyrainin', 'monthlyrainin', 'yearlyrainin', 'totalrainin']  
    return_data_keys=['time_utc', 'temp_in', 'humidity_in', 'barom_rel_in', 'barom_abs_in', 'temp', 'humidity', 'wind_dir', 'wind_speed', 'wind_gust', 'max_daily_gust', 'solar_radiation', 'uv', 'rain_rate', 'event_rain', 'hourly_rain', 'daily_rain', 'weekly_rain', 'monthly_rain', 'yearly_rain', 'total_rain']  
    
    detadb = Deta("")
    db = detadb.Base("instant_records")

    data = request.get_json(force=True)

    
    print(data)
    
    print(type(data))

        
    
    return_data= {}
    
    for index, key in enumerate(return_data_keys_old_names):

        val = data.get(key)     
        if val is not None:
            if key.startswith("temp") and key.endswith("f"):
                    val = round((float(val) - 32) * 5 / 9, 2)
                    key = key[:-1] + 'c'
            if key.startswith("barom") and key.endswith("in"):
                # Convert inches to hPa
                val = round(float(val) * 33.6585, 2)
                key = key[:-2] + 'hpa'
            if key.endswith("rainin") or key == "rainratein":
                # Convert inches to mm
                val = round(float(val) * 25.4, 2)
                key = key[:-2] + 'mm'
            if key.endswith('mph') or key == "maxdailygust":
                # Convert mph
                val = round(float(val) * 1.60934,2)
                key = key[:-3] + 'kph'
                
            if index == 2 or index == 6 or index == 7 or index == 11 or index == 12:
                val = float(val)
                
            return_data[return_data_keys[index]] = val
    
    
    db.put(return_data, return_data[return_data_keys[0]])
    return return_data

