import urllib.request
import json

def download_azure_ips_json(url):
    response = urllib.request.urlopen(url)
    if response.status == 200:
        data = response.read()
        return json.loads(data)
    else:
        print("Failed to download Azure IPs JSON.")
        return None

def generate_mikrotik_rsc(azure_ips_json, output_file):
    ipv4_addresses = set()
    with open(output_file, 'w') as f:
        f.write('/ip firewall address-list\n')
        for service in azure_ips_json['values']:
            service_name = service['name']
            for ip_prefix in service['properties']['addressPrefixes']:
                if ':' not in ip_prefix:  # Verificăm dacă adresa este IPv4
                    ipv4_addresses.add(ip_prefix)
        for ipv4_address in ipv4_addresses:
            f.write(f'add list=Azure address={ipv4_address}\n')
        print(f"Successfully generated Azure IPs .rsc file: {output_file}")

def main():
    azure_ips_url = "https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20240212.json"
    output_file = "azure-ips.rsc"

    azure_ips_json = download_azure_ips_json(azure_ips_url)
    if azure_ips_json:
        generate_mikrotik_rsc(azure_ips_json, output_file)

if __name__ == "__main__":
    main()
