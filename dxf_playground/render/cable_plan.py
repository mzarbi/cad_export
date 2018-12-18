from dxf_playground.render.boxes import box_collection
from dxf_playground.render.cables import cable_collection
from dxf_playground.render.equipments import equipment_collection
from dxf_playground.render.fdhs import fdh_collection
from dxf_playground.render.olts import olt_collection
from dxf_playground.render.splicers import splicer_collection
from dxf_playground.render.subscriber_dwellings import subscriber_dwelling_collection
from dxf_playground.render.trenches import trench_collection


def add_cable_plan(dwg,modelspace,scenario_id,bounding_box,center):
    build_cables(dwg, modelspace, scenario_id, bounding_box, center)
    build_subscriber_dwellings(dwg, modelspace, scenario_id, bounding_box, center)
    add_splicers(dwg, modelspace, scenario_id, bounding_box, center)
    add_fdhs(dwg, modelspace, scenario_id, bounding_box, center)
    add_olts(dwg, modelspace, scenario_id, bounding_box, center)
    add_boxes(dwg, modelspace, scenario_id, bounding_box, center)
    add_trenches(dwg, modelspace, scenario_id, bounding_box, center)

def build_cables(dwg, modelspace, scenario_id, bounding_box, center):
    cable = cable_collection(dwg, modelspace, scenario_id, bounding_box, center)
    cable.from_data_base()
    ins = cable.inside_bounding_box()
    ins.draw()

def build_subscriber_dwellings(dwg, modelspace, scenario_id, bounding_box, center):
    subscriber_dwelling = subscriber_dwelling_collection(dwg, modelspace, scenario_id, bounding_box, center)
    subscriber_dwelling.from_data_base()
    ins = subscriber_dwelling.inside_bounding_box()
    ins.draw()

def add_splicers(dwg, modelspace, scenario_id, bounding_box, center):
    splicers = splicer_collection(dwg, modelspace, scenario_id, bounding_box, center)
    splicers.from_data_base()
    ins = splicers.inside_bounding_box()
    ins.draw()

def add_fdhs(dwg, modelspace, scenario_id, bounding_box, center):
    fdhs = fdh_collection(dwg, modelspace, scenario_id, bounding_box, center)
    fdhs.from_data_base()
    ins = fdhs.inside_bounding_box()
    ins.draw()

def add_olts(dwg, modelspace, scenario_id, bounding_box, center):
    olts = olt_collection(dwg, modelspace, scenario_id, bounding_box, center)
    olts.from_data_base()
    ins = olts.inside_bounding_box()
    ins.draw()

def add_boxes(dwg, modelspace, scenario_id, bounding_box, center):
    boxes = box_collection(dwg, modelspace, scenario_id, bounding_box, center)
    boxes.from_data_base()
    ins = boxes.inside_bounding_box()
    ins.draw()


def add_trenches(dwg, modelspace, scenario_id, bounding_box, center):
    trenches = trench_collection(dwg, modelspace, scenario_id, bounding_box, center)
    trenches.from_data_base()
    ins = trenches.inside_bounding_box()
    ins.draw()