from fastapi import APIRouter, Depends
from app.kubernetes.kubernetes_schema import DeploymentCreateRequest, ServiceCreateRequest, IngressCreateRequest
from app.kubernetes.kubernetes_service import KubernetesService, get_kubernetes_service
from app.core.config import DEPLOYMENT_TEMPLATE_PATH, SERVICE_TEMPLATE_PATH, INGRESS_TEMPLATE_PATH

router = APIRouter(
    prefix="/kubernetes",
    tags=["kubernetes"],
)


@router.post("/deployment/create")
def deployment_create(context: DeploymentCreateRequest, ks: KubernetesService = Depends(get_kubernetes_service)):
    ks.apply_yaml(context.dict(), DEPLOYMENT_TEMPLATE_PATH)
    return


@router.post("/service/create")
def service_create(context: ServiceCreateRequest, ks: KubernetesService = Depends(get_kubernetes_service)):
    ks.apply_yaml(context.dict(), SERVICE_TEMPLATE_PATH)
    return


@router.post("/ingress/create")
def ingress_create(context: IngressCreateRequest, ks: KubernetesService = Depends(get_kubernetes_service)):
    ks.apply_yaml(context.dict(), INGRESS_TEMPLATE_PATH)
    return
