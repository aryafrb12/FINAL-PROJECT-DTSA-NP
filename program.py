import requests
import os

base_url = "http://localhost:58000/api/v1"
user = "bima"
password = "sakti"

def menu():
    print ("\nMenu: ")
    print
    print ("1. Menampilkan Site Health - Network Device")
    print ("2. Menampilkan Network Device")
    print ("3. Menampilkan Host")
    print ("4. Exit")

def get_ticket():
    headers = {"content-type": "application/json"}
    data = {"username": user, "password": password}

    response = requests.post(base_url+"/ticket", headers=headers, json=data)
    ticket = response.json()
    service_ticket = ticket["response"]["serviceTicket"]
    return service_ticket

def get_site_health():
    ticket = get_ticket()
    headers = {"X-Auth-Token": ticket}
    response = requests.get(base_url+"/network-health", headers=headers)
    device = response.json()
    site_health = device['healthyNetworkDevice']
    return site_health

def get_network_device():
    ticket = get_ticket()
    headers = {"X-Auth-Token": ticket}
    response = requests.get(base_url+"/network-device", headers=headers)
    device = response.json()
    network_device = device['response']
    return network_device

def get_host():
    ticket = get_ticket()
    headers = {"X-Auth-Token": ticket}
    response = requests.get(base_url+"/host", headers=headers)
    device = response.json()
    host_device = device['response']
    return host_device

if __name__ == "__main__":
    os.system('cls')
    print ("Selamat Datang di Program Implementasi REST API")
    print("===============================================")

    while 1:
        menu()
        print("============================")

    
        pilih = input("\nMasukkan pilihan : ")

        if pilih == ('1'):
            health = get_site_health()
            print("Site Health: ", health)
        if pilih == ('2'):
            for networkDevice in get_network_device():
                print("\n", networkDevice["hostname"], "\t", networkDevice["upTime"], "\t", networkDevice["platformId"],"\t",networkDevice["managementIpAddress"])
        elif pilih == ('3'):
            for host in get_host():
                print("\n", host["hostName"], "\t", host["hostIp"], "\t", host["hostMac"], "\t", host["connectedInterfaceName"])
        elif pilih == ('4'):
            exit()
        
        print("\n============================")
