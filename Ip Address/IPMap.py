import geocoder
import folium

g = geocoder.ip("146.70.3.0")

myAddress = g.latlng
print(myAddress)

my_map1 = folium.Map(location=myAddress,
                     zoom_start=12)



folium.CircleMarker(location=myAddress,
                    radius=50, popup="Yorkshire").add_to(my_map1)

folium.Marker(myAddress,
              popup="Yorkshire").add_to(my_map1)

my_map1.save("my_map.html ")