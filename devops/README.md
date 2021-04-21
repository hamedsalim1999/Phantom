## Setup
``` bash
kubectl create secret generic django-secrets --from-env-file=k8/django-secrets
```

``` bash
kubectl describe secret django-secret
```

``` bash
kubectl apply -f k8/django-deployment.yaml
```


``` bash
kubectl get deploy django-deployment
```

``` bash
kubectl get pod
```


``` bash
kubectl get node -o wide
```


