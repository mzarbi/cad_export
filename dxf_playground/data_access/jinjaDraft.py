import os
import jinja2
import io

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


context = {
    'department': 'unknown',
    'CMP': 'unknown',
    'CZ_olt':"EQOS1",
    'GPS_olt_N' : "N:36.47",
    'GPS_olt_E' : "E:7.47",
    "CCite" : "C240-005",
    "CName" : "unkonown"
}
result = render(r'/home/medzied/Documents/cad_export/dxf_playground/resources/template2Draft.dxf', context)

with io.open("ddd.dxf",mode="w", encoding="utf-8") as f:
    f.write(result)