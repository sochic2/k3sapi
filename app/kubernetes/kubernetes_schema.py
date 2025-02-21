from typing import Optional

from pydantic import BaseModel, Field

class NamespaceCreateRequest(BaseModel):
    namespace: str = Field(..., description='Name of the namespace')


class NamespaceDeleteRequest(BaseModel):
    namespace: str = Field(..., description='Name of the namespace')


class DeploymentCreateRequest(BaseModel):
    deployment_name: str = Field(..., description='deployment명')
    namespace: str = Field(..., description='deployment 생성될 네임스페이스')
    replicas: int = Field(..., description='replica 수, int')
    app_name: str = Field(..., description='spec.selector.matchLabels.app, spec.template.metadata.labels.app')
    container_name: str = Field(..., description='컨테이너명')
    image: str = Field(..., description='사용할 docker 이미지')
    port: int = Field(..., description='컨테이너 포트')
    cpu_request: Optional[str] = Field(None, pattern=r"^(?:\d+m|\d+(?:\.\d+)?)$",
                                       description="cpu_request는 선택적이며, '100m', '0.5', '1', '1.5'등의 값을 허용")
    memory_request: Optional[str] = Field(None, pattern=r"^(d+Mi|d+Gi)",
                                  description= 'memory_request는 선택정이며, 정수 + Mi or Gi의 형태로 입력')

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
