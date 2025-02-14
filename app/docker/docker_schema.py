from pydantic import BaseModel

class ImagebuildRequest(BaseModel):
    docker_file_content: str
    image_name: str
    tag: str= "latest"

    model_config = {
        "json_schema_extra": {
            "examples" : [
                {
                    "docker_file_content": 'FROM python:3.10-slim'
                                           '\nRUN echo "Asia/Seoul" > /etc/timezone'
                                           '\nRUN apt-get update && apt-get install -y git'
                                           '\nRUN git clone https://github.com/sochic2/k3sbuildpush.git'
                                           '\nWORKDIR /k3sbuildpush'
                                           '\nRUN pip install --no-cache-dir -r requirements.txt'
                                           '\nCMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]',
                    "image_name": "buildpush-test2",
                    "tag": "latest"
                }
            ]
        }
    }


class ImagebuildResponse(BaseModel):
    success: bool
    logs: str
    image_tag: list[str]


class TagcheckRequest(BaseModel):
    image_name: str
    tag: str= "latest"


class TagcheckResponse(BaseModel):
    exist: bool


class ImagepushRequest(BaseModel):
    image_name: str
    tag: str= "latest"

    model_config = {
        "json_schema_extra": {
            "examples" : [
                {
                    "image_name": "buildpush-test2",
                    "tag": "latest"
                }
            ]
        }
    }


class ImagepushResponse(BaseModel):
    success: bool
    logs: str