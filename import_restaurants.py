import json
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SnrdnGrm.settings")
django.setup()

from sgapp.models import Restaurant

with open("hotosm_tur_points_of_interest_points_geojson.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

sayac = 0

for feature in data["features"]:
    props = feature["properties"]
    geometry = feature["geometry"]

    if props.get("amenity") == "restaurant":
        name = props.get("name")
        if not name:
            continue  # isimsiz restoran varsa atla

        address = props.get("addr:full") or props.get("name:tr") or "Adres yok"
        lon, lat = geometry["coordinates"]

        if not Restaurant.objects.filter(name=name, latitude=lat, longitude=lon).exists():
            Restaurant.objects.create(
                name=name,
                address=address,
                latitude=lat,
                longitude=lon
            )
            sayac += 1
