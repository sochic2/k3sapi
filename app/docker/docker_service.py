import docker
import json
import io
from app.core.config import REMOTE_DOCKER_HOST, HARBOR_URL, HARBOR_REPO, HARBOR_ID, HARBOR_PWD


class DockerService:
    def __init__(self):
        self.client = docker.DockerClient(base_url=REMOTE_DOCKER_HOST)
        self.client.login(username=HARBOR_ID, password=HARBOR_PWD, registry=HARBOR_URL)

    def check_dup_image_name(self, image_name, tag):
        images = self.client.images.list()
        build_tag = f'{HARBOR_URL}/{HARBOR_REPO}/{image_name}:{tag}'
        for image in images:
            if build_tag in image.tags:
                return {"exist": True}
        return {"exist": False}

    def image_build(self, docker_file_content, image_name, tag):
        dockerfile_bytes = io.BytesIO(docker_file_content.encode('utf-8'))
        build_tag = f'{HARBOR_URL}/{HARBOR_REPO}/{image_name}:{tag}'

        try:
            image, build_logs = self.client.images.build(
                fileobj=dockerfile_bytes,
                tag=build_tag,
                rm=True
            )
            build_logs = "".join([log.get("stream", "") for log in build_logs])
            return {
                    "success": True,
                    "logs": build_logs.strip(),
                    "image_tag": image.tags
                    }
        except docker.errors.BuildError as e:
            return {
                    "success": False,
                    "logs" : "".join([log.get("error", "") for log in e.build_log if "error" in log]),
                    "image_tag": []
                    }

    def image_push(self, image_name, tag):
        build_tag = f'{HARBOR_URL}/{HARBOR_REPO}/{image_name}:{tag}'
        if self.check_dup_image_name(image_name, tag):
            push_logs = self.client.images.push(build_tag)
            if 'error' in push_logs:
                return {
                    "success": False,
                    "logs": push_logs
                }

            else:
                return {
                    "success": True,
                    "logs" : push_logs
                }
        else:
            return {
                "success": False,
                "logs": f"{build_tag} is not exist"
            }


def get_docker_service():
    return DockerService()