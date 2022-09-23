# nginx-manager-watcher
A wrapper for NGINX Manager that watches NodePort creations, create a DNS in Cloudflare and create a proxy in NGINX Manager

## How To

Simply grab the files from `./k8s/` and apply, changing the environment as needed. Kindly note that the environment will be plaintext. You may use `External Secrets Operator` or anything that matches your expectations to deliver the environmental variables to the pods.

The k8s watcher will monitor every Service created with type NodePort and create the Proxy on NGINX Manager using the credentials on envs, so as the DNS Entries on Cloudflare
## To Do
- Allow for SSL configuration based on the Service annotations (nginx-manager-watcher-ssl: enable)
- Delete methods
- Update methods
- Create boilerplate for cluster creation either using KinD, Minikube or anything that fits
- Allow for multiple CF zones based on configmap/secret reading
- Implement a Logger
