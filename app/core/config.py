import os

a = os.getcwd()
REMOTE_DOCKER_HOST = "tcp://192.168.0.233:2375"
HARBOR_URL = "harbor.rbpk3s.com"
HARBOR_REPO = "harbor_test"
HARBOR_ID = "admin"
HARBOR_PWD = "Okestro00!@#$"
DEPLOYMENT_TEMPLATE_PATH = os.path.abspath("app/core/yaml_templates/deployment_template.j2")
SERVICE_TEMPLATE_PATH = os.path.abspath("app/core/yaml_templates/service_template.j2")
INGRESS_TEMPLATE_PATH = os.path.abspath("app/core/yaml_templates/ingress_template.j2")
