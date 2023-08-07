# ticketing-python
Ticketing microservices-based ecommerce built with Python

# Local Execution
From the root of this project, run the following command to spin up all containers in your local k8s cluster:
```shell
skaffold dev --port-forward
```
All containers will be available at their designated ports.

You can also just run:
```shell
skaffold dev
```
and use the included Ingress nginx configuration for each necessary service.
Then you only need to edit your hosts file:
```shell
sudo vim/etc/hosts
```
Add this line at the end of the file: `127.0.0.1 ticketing.dev`.
You can then access the app going to `ticketing.dev` in your web browser.
