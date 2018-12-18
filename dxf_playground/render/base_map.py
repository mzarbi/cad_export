from dxf_playground.render.dwelling_units import building_collection
from dxf_playground.render.roads import road_collection


def add_base_maps(dwg,modelspace,resources_path,bounding_box):
    center = build_roads(dwg,modelspace,resources_path,bounding_box)
    build_dwelling_units(dwg,modelspace,resources_path,bounding_box,center)
    return center

def build_roads(dwg,modelspace,resource_path,bounding_box):
    roads = road_collection(dwg,modelspace,resource_path,bounding_box)
    roads.from_feature_file()
    ins = roads.inside_bounding_box()
    ins.draw()
    return ins.bbox()

def build_dwelling_units(dwg,modelspace,resource_path,bounding_box,center):
    buildings = building_collection(dwg,modelspace,resource_path,bounding_box,center)
    buildings.from_feature_file()

    ins = buildings.inside_bounding_box()
    ins.draw()


