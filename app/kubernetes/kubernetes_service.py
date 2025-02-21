from kubernetes import config, client, utils
from app.kubernetes.utils import yaml_to_dict


class KubernetesService:
    def __init__(self):
        config.load_kube_config()
        self.api_client = client.ApiClient()
        self.core = client.CoreV1Api()
        self.apps = client.AppsV1Api()
        self.network = client.NetworkingV1Api()


    def check_dup_namespace(self, namespace_name):
        namespaces = [item.metadata.name for item in self.core.list_namespace().items]
        if namespace_name in namespaces:
            return True
        else:
            return False

    def create_namespace(self, namespace):
        body = client.V1Namespace(
            metadata=client.V1ObjectMeta(name=namespace)
        )
        self.core.create_namespace(body)
        return {"success": True, "message": f"Namespace {namespace} created"}

    def delete_namespace(self, namespace):
        self.core.delete_namespace(namespace)
        return {"success": True, "message": f"{namespace} deleted"}

    def apply_yaml(self, context, yaml_path):
        try:
            dict_yaml = yaml_to_dict(context, yaml_path)
            namespace = context['namespace']
            if not self.check_dup_namespace(namespace):
                self.create_namespace(namespace)
            utils.create_from_dict(self.api_client, dict_yaml)
            return {"success": True, "message": f"yaml applied on {namespace}"}

        except Exception as e:
            return {"success": False, "message": str(e)}


def get_kubernetes_service():
    return KubernetesService()

