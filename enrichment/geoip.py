import geoip2.database
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "GeoLite2-City.mmdb")

reader = geoip2.database.Reader(DB_PATH)

def get_country(ip):
    try:
        response = reader.city(ip)
        return response.country.name
    except:
        return "Unknown"
