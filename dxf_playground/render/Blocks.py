import zdxf
import os
import io
import jinja2


def add_blocks(dwg,modelspace,res_dir):
    import_blocks(dwg,res_dir)

    modelspace.add_blockref("big_block", (0,0))


    pass

def import_blocks(dwg,res_dir):
    prev = os.getcwd()
    os.chdir(res_dir)

    update_template()

    source_drawing = zdxf.readfile("template2.dxf")
    importer = zdxf.Importer(source_drawing,dwg)
    importer.import_blocks("*")
    os.chdir(prev)




def update_template():
    context = {
        'department': 'unknown',
        'CMP': 'unknown',
        'CZ_olt': "EQOS1",
        'GPS_olt_N': "N:36.47",
        'GPS_olt_E': "E:7.47",
        "CCite": "C240-005",
        "CName": "unkonown"
    }

    path, filename = os.path.split("template2Draft.dxf")
    result = jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)


    with io.open("template2.dxf", mode="w", encoding="utf-8") as f:
        f.write(result)