from kubernetes import config, client, utils
from app.kubernetes.utils import yaml_to_dict


class KubernetesService:
    def __init__(self):
        config.load_kube_config()
        self.api_client = client.ApiClient()
        self.v1 = client.CoreV1Api(self.api_client)

    def check_dup_namespace(self, namespace_name):
        namespaces = [item.metadata.name for item in self.v1.list_namespace().items]
        if namespace_name in namespaces:
            return True
        else:
            return False

    def create_namespace(self, namespace):
        body = client.V1Namespace(
            metadata=client.V1ObjectMeta(name=namespace)
        )
        self.v1.create_namespace(body)

    def apply_yaml(self, context, yaml_path):
        dict_yaml = yaml_to_dict(context, yaml_path)
        if not self.check_dup_namespace(context['namespace']):
            self.create_namespace(context['namespace'])

        utils.create_from_dict(self.api_client, dict_yaml)





def get_kubernetes_service():
    return KubernetesService()

