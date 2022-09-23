from kubernetes import client, config, watch

from nginx_ui import generate_token, create_proxy
from cloudflare import create_dns

try:
  config.load_kube_config()
except:
  config.load_incluster_config()

v1 = client.CoreV1Api()
w = watch.Watch()

def _prettify(object): 
  return {
    "SVC_NAME": object.metadata.name,
    "SVC_NODEPORT": object.spec.ports[0].node_port,
    "SVC_PORT": object.spec.ports[0].port
  }

def deleted_svc(event):
  data = _prettify(event)
  print(data)

def created_svc(event):
  data = _prettify(event)
  token = generate_token()
  create_dns(data)
  create_proxy(data, token)

def modified_svc(event):
  data = _prettify(event)
  print(data)


def main():
  for event in w.stream(func=v1.list_namespaced_service, namespace="default", timeout_seconds=0):
    if event['object'].metadata.name != "kubernetes":
      if event['type'] == "DELETED":
        deleted_svc(event['object'])
      if event['type'] == "ADDED":
        created_svc(event['object'])
      else:
        modified_svc(event['object'])

if __name__ == "__main__":
   main()