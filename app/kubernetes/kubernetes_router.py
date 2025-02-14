from fastapi import APIRouter, Depends
from app.kubernetes.kubernetes_schema import (DeploymentCreateRequest
                                            , ServiceCreateRequest
                                            , IngressCreateRequest
                                            , NamespaceCreateRequest
                                            , NamespaceDeleteRequest)
from app.kubernetes.kubernetes_service import KubernetesService, get_kubernetes_service
from app.core.config import DEPLOYMENT_TEMPLATE_PATH, SERVICE_TEMPLATE_PATH, INGRESS_TEMPLATE_PATH

router = APIRouter(
    prefix="/kubernetes",
    tags=["kubernetes"],
)

@router.post("/namespace/create")
def namespace_create(request: NamespaceCreateRequest, ks: KubernetesService = Depends(get_kubernetes_service)):
    res = ks.create_namespace(request.namespace)
    return res


@router.delete("/namespace/delete")
def namespace_delete(request: NamespaceDeleteRequest, ks: KubernetesService = Depends(get_kubernetes_service)):
    res = ks.delete_namespace(request.namespace)
    print(res)
    return res


@router.post("/deployment/create")
def deployment_create(context: DeploymentCreateRequest, ks: KubernetesService = Depends(get_kubernetes_service)):
    res = ks.apply_yaml(context.dict(), DEPLOYMENT_TEMPLATE_PATH)
    return res


@router.post("/service/create")
def service_create(context: ServiceCreateRequest, ks: KubernetesService = Depends(get_kubernetes_service)):
    res = ks.apply_yaml(context.dict(), SERVICE_TEMPLATE_PATH)
    return res


@router.post("/ingress/create")
def ingress_create(context: IngressCreateRequest, ks: KubernetesService = Depends(get_kubernetes_service)):
    res = ks.apply_yaml(context.dict(), INGRESS_TEMPLATE_PATH)
    return res
