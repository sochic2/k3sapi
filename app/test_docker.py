from fastapi.testclient import TestClient

from .main import app
from .tmp import tmp_dockerfile
client = TestClient(app)



def test_docker_build():
    response = client.post(
        url="/api/docker/image/build",
        json={
            "docker_file_content": tmp_dockerfile,
            "image_name": "local-python-test",
            "tag": "latest"
        }
    )
    print(response.status_code)  # HTTP 상태 코드 출력
    print(response.json())  # 응답 JSON 출력
    assert response.status_code == 200



def test_docker_tag_check():
    response = client.post(
        url="/api/docker/image/exist",
        json={"image_name":"pythonbuildtest3123", "tag": "latest"}
        )
    print(response.status_code)  # HTTP 상태 코드 출력
    print(response.json())  # 응답 JSON 출력
    assert response.status_code == 200


def test_docker_image_push():
    response = client.post(
        url="/api/docker/image/push",
        json={"image_name":"pythonbuildtest3", "tag": "latest"}
        )

    print(response.status_code)  # HTTP 상태 코드 출력
    print(response.json())  # 응답 JSON 출력
    assert response.status_code == 200
