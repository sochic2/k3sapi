from pydantic import BaseModel, Field

class NamespaceCreateRequest(BaseModel):
    namespace: str


class NamespaceDeleteRequest(BaseModel):
    namespace: str


class DeploymentCreateRequest(BaseModel):
    deployment_name: str
    namespace: str
    replicas: int
    app_name: str
    container_name: str
    image: str
    port: int
    cpu_request: str | None = None
    memory: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples" : [
                {
                    "deployment_name": "k3sapi-test",
                    "namespace": "k3sapi-namespace",
                    "replicas": 2,
                    "app_name": "k3sapi-app",
                    "container_name": "k3sapi-app-container",
                    "image": "harbor.rbpk3s.com/harbor_test/buildpush-test",
                    "port": 8000,
                    "cpu_request": "50m",
                    "memory_request": "50Mi",
                }
            ]
        }
    }


class ServiceCreateRequest(BaseModel):
    service_name: str
    namespace: str
    app_name: str
    protocol: str
    service_port: int
    target_port: int

    model_config = {
        "json_schema_extra": {
            "examples" : [
                {
                    "service_name": "k3sapi-service",
                    "namespace": "k3sapi-namespace",
                    "app_name": "k3sapi-app",
                    "protocol": "TCP",
                    "service_port": 80,
                    "target_port": 8000,
                }
            ]
        }
    }


class IngressCreateRequest(BaseModel):
    ingress_name: str
    namespace: str
    host: str
    service_name: str

    model_config = {
        "json_schema_extra": {
            "examples" : [
                {
                    "ingress_name": "k3sapi-ingress",
                    "namespace": "k3sapi-namespace",
                    "host": "k3sapitest.com",
                    "service_name": "k3sapi-service",
                }
            ]
        }
    }
