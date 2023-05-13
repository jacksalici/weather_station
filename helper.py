dict = {
    'PASSKEY': '---', 
    'stationtype': 'GW1100A_V2.2.3',
    'runtime': '213035',
    'dateutc': '2023-05-07 10:39:35',
    'tempinf': '72.68',
    'humidityin': '65',
    'baromrelin': '29.961',
    'baromabsin': '29.961',
    'tempf': '76.46',
    'humidity': '48',
    'winddir': '310',
    'windspeedmph': '0.22',
    'windgustmph': '1.12',
    'maxdailygust': '4.47', 
    'solarradiation': '661.25',
    'uv': '6', 
    'rainratein': '0.000',
    'eventrainin': '0.000',
    'hourlyrainin': '0.000',
    'dailyrainin': '0.000',
    'weeklyrainin': '2.748',
    'monthlyrainin': '2.748',
    'yearlyrainin': '8.819',
    'totalrainin': '8.819',
    'wh65batt': '0', 
    'freq': '868M',
    'model': 'GW1100A',
    'interval': '20'
}


stra = '''dateutc: str
    tempinf: float 
    humidityin: float 
    baromrelin: float 
    baromabsin: float
    tempf: float
    humidity: float
    winddir: float
    windspeedmph: float
    windgustmph: float
    maxdailygust: float
    solarradiation: float
    uv: int
    rainratein: float
    eventrainin: float
    hourlyrainin: float
    dailyrainin: float
    weeklyrainin: float
    monthlyrainin: float
    yearlyrainin: float
    totalrainin: float'''



list = ['dateutc', 'tempinf ', ' humidityin ', ' baromrelin ', ' baromabsin', ' tempf', ' humidity', ' winddir', ' windspeedmph', ' windgustmph', ' maxdailygust', ' solarradiation', ' uv','rainratein', ' eventrainin', ' hourlyrainin', ' dailyrainin', ' weeklyrainin', ' monthlyrainin', ' yearlyrainin', ' totalrainin ']
newl = [i.strip() for i in list]
    