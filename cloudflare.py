import requests
import os

TOKEN = os.environ.get("CLOUDFLARE_API_TOKEN")
ZONE = os.environ.get("CLOUDFLARE_ZONE")
IP = os.environ.get("KUBERNETES_HOST_IP")

if IP == "":
  r = requests.get("https://ifconfig.me")
  IP = r.text


def create_dns(data):
  NAME = data['SVC_NAME']
  print(ZONE, TOKEN, IP)
  r = requests.post(f'https://api.cloudflare.com/client/v4/zones/{ZONE}/dns_records', 
                   headers={'Authorization': f'Bearer {TOKEN}', "Content-Type": "application/json"},
                   json={"type": "A", "name": f"{NAME}", "content": f'{IP}'})  

  print(r.json())