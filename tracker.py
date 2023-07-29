import requests
import pyfiglet
def get_location_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        print(f"IP Adresi: {data['query']}")
        print(f"Ülke: {data['country']}")
        print(f"Şehir: {data['city']}")
        print(f"Enlem: {data['lat']}")
        print(f"Boylam: {data['lon']}")
    else:
        print("Konum bilgisi bulunamadı")

if __name__ == "__main__":
    print(pyfiglet.figlet_format("IP Tracker"))
    print("                         [Created by Sars]\n")
    ip_address = input("IP adresini gir: ")
    get_location_info(ip_address)