from fastapi import APIRouter, Depends

from app.docker.docker_schema import (ImagebuildRequest,
                                      ImagebuildResponse,
                                      TagcheckRequest,
                                      TagcheckResponse,
                                      ImagepushRequest,
                                      ImagepushResponse
                                      )
from app.docker.docker_service import get_docker_service, DockerService

router = APIRouter(
    prefix="/docker"
)



@router.post("/image/exist", response_model=TagcheckResponse)
def tag_check(request: TagcheckRequest, ds: DockerService = Depends(get_docker_service)):
    response = ds.check_dup_image_name(request.image_name, request.tag)
    return response


@router.post("/image/build", response_model=ImagebuildResponse)
def docker_build(request: ImagebuildRequest, ds: DockerService = Depends(get_docker_service)):
    response = ds.image_build(request.docker_file_content, request.image_name, request.tag)
    return response


@router.post("/image/push", response_model=ImagepushResponse)
def docker_push(request: ImagepushRequest, ds: DockerService = Depends(get_docker_service)):
    response = ds.image_push(request.image_name, request.tag)
    return response


