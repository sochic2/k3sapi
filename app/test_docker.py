from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

image_name = "buildpush-test"

def test_docker_tag_check():
    response = client.post(
        url="/api/docker/image/exist",
        json={"image_name":image_name,
              "tag": "latest"}
        )
    print(response.status_code)  # HTTP 상태 코드 출력
    print(response.json())  # 응답 JSON 출력
    assert response.status_code == 200


def test_docker_build():
    tmp_dockerfile = """
    FROM python:3.10-slim
    RUN echo "Asia/Seoul" > /etc/timezone
    RUN apt-get update && apt-get install -y git
    RUN git clone https://github.com/sochic2/k3sbuildpush.git
    WORKDIR /k3sbuildpush
    RUN pip install --no-cache-dir -r requirements.txt
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
    """
    response = client.post(
        url="/api/docker/image/build",
        json={
            "docker_file_content": tmp_dockerfile,
            "image_name": image_name,
            "tag": "latest"
        }
    )
    print(response.status_code)  # HTTP 상태 코드 출력
    print(response.json())  # 응답 JSON 출력
    assert response.status_code == 200


def test_docker_image_push():
    response = client.post(
        url="/api/docker/image/push",
        json={"image_name":image_name,
              "tag": "latest"}
        )

    print(response.status_code)  # HTTP 상태 코드 출력
    print(response.json())  # 응답 JSON 출력
    assert response.status_code == 200
