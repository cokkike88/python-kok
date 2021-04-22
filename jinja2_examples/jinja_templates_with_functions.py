from jinja2 import Template
import rapidjson

template = '{"Address": "{{sanitize_string(address)}}"}'
t = Template(template)

def sanitize_string(text) -> str:
    text = text.replace('\n', "").replace('\\n', "").replace('%2F', "/").\
        replace('%3A', ':').replace('\r', '').replace('/','').replace('"', '').replace('\\', '')
    return text

text = 'Street 34th\\\\\\\\\\"'

body = t.render(address=text,sanitize_string=sanitize_string)
print(body)
body_object = rapidjson.loads(body)
print(body_object)