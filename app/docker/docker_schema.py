from pydantic import BaseModel

class ImagebuildRequest(BaseModel):
    docker_file_content: str
    image_name: str
    tag: str= "latest"


class ImagebuildResponse(BaseModel):
    success: bool
    logs: str
    image_tag: str


class TagcheckRequest(BaseModel):
    image_name: str
    tag: str= "latest"


class TagcheckResponse(BaseModel):
    exist: bool


class ImagepushRequest(BaseModel):
    image_name: str
    tag: str= "latest"


class ImagepushResponse(BaseModel):
    success: bool
    logs: str