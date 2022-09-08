# LDAP & Multi-Factor Authentication

This repo builds a LDAP server and implement multi-factor authentication

LDAP server (Lightweight Directory Access Protocol) is a software protocol for enabling anyone to locate data about organizations, individuals and other resources such as files and devices in a network - like Active-Directory

I used these guides:

    https://soshace.com/integrate-ldap-authentication-with-flask/
    https://cloudolife.com/2020/11/21/Kubernetes-K8S/Helm/Helm-install-openldap-and-phpldapadmin-to-manage-LDAP-objects-within-Kubernetes-K8S/
    https://www.talkingquickly.co.uk/installing-openldap-kubernetes-helm
    https://docs.bitnami.com/tutorials/create-openldap-server-kubernetes/
    https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/

### Working tree:
```
├── app
│   ├── app.py
│   ├── form.py
│   ├── ldap_authentication.py
│   ├── __pycache__
│   │   ├── app.cpython-38.pyc
│   │   ├── app.cpython-39.pyc
│   │   └── settings.cpython-39.pyc
│   ├── settings.py
│   ├── static
│   │   └── lock.jpg
│   └── templates
│       ├── login.html
│       └── login_mfa.html
├── app.yaml
├── Dockerfile
├── ldap_deploy.yaml
├── README.md
└── requirements.txt
```

# creating (based on a local machine, using Minikube)
    docker build -t ldap .
    
    minikube image load ldap
    
    kubectl create secret generic openldap-secret --from-literal=adminpassword='adminpassword' --from-literal=users='meir' --from-literal=passwords='1234'

you can check if the users and passwords defined in the secret:

    echo "$(kubectl get secret openldap-secret -n default -o json | jq -r .data.users | base64 --decode)"

    echo "$(kubectl get secret openldap-secret -n default -o json | jq -r .data.passwords | base64 --decode)"
    
    kubectl apply -f .
    
# please wait for a few seconds for all the pods to start
    kubectl port-forward $(kubectl get pod -l app=ldap -o jsonpath="{.items[0].metadata.name}") 8888:8888

# cleaning
    minikube delete