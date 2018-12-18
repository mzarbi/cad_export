# -*- coding: utf-8 -*-
import os

import datetime
from os.path import dirname

import zdxf
from shapely.geometry import Polygon

from dxf_playground.render.Blocks import add_blocks
from dxf_playground.render.base_map import add_base_maps
from dxf_playground.render.cable_plan import add_cable_plan
from dxf_playground.utils.projections import project_point_collection, transform_array


class exporter:
    def __init__(self,
                 uri,
                 scenario_id,
                 poly,
                 dxf_version="AC1027",
                 name="Drawing Title",
                 unit="Meters",
                 contact_name="Unknown",
                 contact_phone="00-000-000",
                 contact_mail="medzied.arbi@qosdesign.fr",
                 mid_scale=0.002,
                 max_scale=0.004,
                 include_basemap=True,
                 include_infrastructure=True,
                 include_equipment=True,
                 include_sat_image=True,
                 separate=True,
                 horizontal_spacing=False):

        # Parameters
        self.resources_path = dirname(dirname(os.getcwd())) + "/dxf_playground/resources"
        self.template_path = self.resources_path + r"/template.dxf"

        self.workspace = uri
        self.scenario_id = scenario_id
        self.bounding_box = poly
        self.dxf_version = dxf_version
        self.name = name
        self.unit = unit
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.contact_mail = contact_mail
        self.include_basemap = include_basemap
        self.include_infrastructure = include_infrastructure
        self.include_equipment = include_equipment
        self.include_sat_image = include_sat_image
        self.mid_scale = mid_scale
        self.max_scale = max_scale
        self.separate = separate
        self.horizontal_spacing = horizontal_spacing

        # Fonctional fields
        self.dwg = zdxf.new(self.dxf_version)
        self.modelspace = self.dwg.modelspace()
        self.db_handler = None
        pass

    def render(self):
        add_blocks(self.dwg, self.modelspace,self.resources_path)
        center = add_base_maps(self.dwg,self.modelspace,self.resources_path,self.bounding_box)
        add_cable_plan(self.dwg, self.modelspace, self.scenario_id, self.bounding_box,center)
        return self

    def save(self):
        self.dwg.saveas("export.dxf")
        return self

def create_workspace():

    now = str(datetime.datetime.now())
    uri = now.replace(" ", "").replace("-", "_").replace(":", "_")
    os.mkdir(os.getcwd() + "/nest.cache/" + uri)
    os.chdir(os.getcwd() + "/nest.cache/" + uri)
    return uri

def export_dxf(  scenario_id,
                 bounding_box,
                 uri=None,
                 dxf_version="AC1027",
                 name="Drawing Title",
                 unit="Meters",
                 contact_name="Unknown",
                 contact_phone="00-000-000",
                 contact_mail="medzied.arbi@qosdesign.fr",
                 mid_scale=0.002,
                 max_scale=0.004,
                 include_basemap=True,
                 include_infrastructure=True,
                 include_equipment=True,
                 include_sat_image=True,
                 separate= True,
                 horizontal_spacing = False):


    # Transform Bounding Box
    poly = Polygon(
        project_point_collection(
            transform_array(bounding_box)
        )
    )


    # Start Export
    uri = create_workspace()

    dx = exporter(   uri,
                     scenario_id,
                     poly,
                     dxf_version="AC1027",
                     name="Drawing Title",
                     unit="Meters",
                     contact_name="Unknown",
                     contact_phone="00-000-000",
                     contact_mail="medzied.arbi@qosdesign.fr",
                     mid_scale=0.002,
                     max_scale=0.004,
                     include_basemap=True,
                     include_infrastructure=True,
                     include_equipment=True,
                     include_sat_image=True,
                     separate= True,
                     horizontal_spacing = False).\
        render().\
        save()
    os.chdir(os.getcwd())
    return uri





if __name__ == "__main__":
    pass