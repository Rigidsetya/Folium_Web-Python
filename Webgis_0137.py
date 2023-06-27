import folium

maps = folium.Map(location=[-6.362904577664523, 107.17147603051227], zoom_start=10, tiles="CartoDB positron")
maps.save("Kab_Bekasi.html")