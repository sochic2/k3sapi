from jinja2 import Template
import yaml


file_path = "D:\\PythonSrc\\k3sapi\\app\\core\\yaml_templates\\service_template.yaml"
with open(file_path, 'r', encoding='UTF-8') as f:
    template = Template(f.read())