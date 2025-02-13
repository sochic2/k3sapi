from jinja2 import Template
import yaml

def yaml_to_dict(context, file_path):
    with open(file_path, 'r', encoding='UTF-8') as f:
        template = Template(f.read())
        rendered_template = template.render(context)
        return yaml.safe_load(rendered_template)