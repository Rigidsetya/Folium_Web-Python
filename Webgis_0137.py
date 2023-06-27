import folium
import json
import requests

url = (
    "https://raw.githubusercontent.com/Rigidsetya/Folium_Web-Python/main/ADMIN_KAB-KOTA-BEKASI_AR.geojson"
)

m = folium.Map(
    location=[-6.365634233115968, 107.17628254886996],
    tiles="cartodbpositron",
    zoom_start=10,
)

folium.GeoJson(url, name="geojson").add_to(m)

folium.LayerControl().add_to(m)

m.save("Kab_Bekasi.html")