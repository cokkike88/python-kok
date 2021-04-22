from jinja2 import Template

def empty_template():
    data = {
        "name": "template test"
    }
    template = ''
    t = Template(template)
    response = t.render(object=data)
    print(response)

def empty_data():
    data = {}
    template = "{{object['name']['lname']}}"
    t = Template(template)
    response = t.render(object=data)
    print(response)

empty_data()
# empty_template()