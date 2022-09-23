from email import header
import os
import requests

URL = os.environ.get("NGINX_MANAGER_URL")
NGINX_EMAIL = os.environ.get("NGINX_MANAGER_EMAIL")
NGINX_PASS = os.environ.get("NGINX_MANAGER_PASS")
CF_ROOT_DOMAIN_NAME = os.environ.get("CF_ROOT_DOMAIN_NAME")

IP = os.environ.get("KUBERNETES_HOST_IP")

if IP == "":
  r = requests.get("https://ifconfig.me")
  IP = r.text

def generate_token(): 
  r = requests.post(f'{URL}/api/tokens', json={"identity": NGINX_EMAIL, "secret":NGINX_PASS})
  token = r.json()['token']
  print(token)
  return token

def create_proxy(data, token):
  NAME = data['SVC_NAME']
  NODE_PORT = data['SVC_NODEPORT']
  r = requests.post(f'{URL}/api/nginx/proxy-hosts', json={"domain_names":[f"{NAME}.{CF_ROOT_DOMAIN_NAME}/"],"forward_scheme":"http","forward_host":f"{IP}","forward_port":NODE_PORT,"access_list_id":"0","certificate_id":0,"meta":{"letsencrypt_agree": False,"dns_challenge": False},"advanced_config":"","locations":[],"block_exploits": False,"caching_enabled":True,"allow_websocket_upgrade":False,"http2_support":False,"hsts_enabled":False,"hsts_subdomains":False,"ssl_forced":False},
                    headers={"Authorization": f"Bearer {token}"})
  print(r.json())