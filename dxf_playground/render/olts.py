#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shapely.geometry import Polygon, LineString, Point
import numpy as np

from dxf_playground.data_access.data_query import DB_Handler
from dxf_playground.render.coordinates import BoundingBox
from dxf_playground.utils.projections import project_point_collection, project_point


class olt:
    def __init__(self, properties=None, geometry=None):
        self.properties = properties
        self.geometry = geometry

    def draw_olt(self, cx, cy, bloc):
        geo = (self.geometry[0] - cx, self.geometry[1] - cy)
        bloc.add_blockref("OLT", geo)
        bloc.add_text("OLT",
                      dxfattribs={'color': 7}).set_pos(
            (geo[0], geo[1] - 3),
            align='CENTER')

        """
        bloc.add_text(str(self.properties.FusionSpliceNb_32) + "C",
                      dxfattribs={'color': 7}).set_pos(
            (geo[0],geo[1]-3),
            align='CENTER')

        bloc.add_text("LGTS " + str(len(self.properties.appartmentsPerFloorPerBlocString.split("/")) - 1),
                      dxfattribs={'color': 7}).set_pos(
            (geo[0] , geo[1] - 5),
            align='CENTER')

        self.properties.appartmentsPerFloorPerBlocString.split("/")
        floor_raw = []
        for i in self.properties.appartmentsPerFloorPerBlocString.split("/"):
            try:
                floor_raw.append(int(i.split(";")[1]))
            except:
                pass
        bloc.add_text("R + " + str(max(floor_raw)),
                      dxfattribs={'color': 7}).set_pos(
            (geo[0], geo[1] - 7),
            align='CENTER')

        bloc.add_text("ODB/ " + str(self.properties.Nb_FO),
                      dxfattribs={'color': 7}).set_pos(
            (geo[0], geo[1] + 3),
            align='CENTER')

        """


class olt_collection(list):
    def __init__(self, dwg, modelspace, scenario_id, bounding_box, bbox):
        list.__init__(self)

        self.dwg = dwg
        self.modelspace = modelspace
        self.scenario_id = scenario_id
        self.bounding_box = bounding_box
        self.bbox = bbox

    def from_data_base(self):
        hndl = DB_Handler()
        result = hndl.query_olt(self.scenario_id)
        for res in result:
            cp = olt_properties()
            cp.fromArray(res)
            c = olt(cp, project_point((cp.lat_16, cp.lon_17)))
            self.append(c)
        hndl.close()

    def inside_bounding_box(self):
        tmp = olt_collection(self.dwg, self.modelspace, self.scenario_id, self.bounding_box, self.bbox)
        for i in self:
            if self.bounding_box.contains(Point(i.geometry)):
                tmp.append(i)
        return tmp

    def draw(self):
        bloc = self.dwg.blocks.new(name="olt.block1.A4")
        self.modelspace.add_blockref("olt.block1.A4",
                                     (-95., 0.),
                                     dxfattribs={
                                         "xscale": 571. / self.bbox.width,
                                         "yscale": 458. / self.bbox.height})

        for i in self:
            i.draw_olt(self.bbox.center[0], self.bbox.center[1], bloc)


class olt_properties:
    def __init__(self):
        pass

    def fromArray(self, arr):
        self.Equipment_ID_0 = arr[0]
        self.bBackbone_1 = arr[1]
        self.NAME_2 = arr[2]
        self.tNetworkName_3 = arr[3]
        self.state_4 = arr[4]
        self.Tags_5 = arr[5]
        self.VerticalDistance_6 = arr[6]
        self.CableDrawnBox_ID_7 = arr[7]
        self.id2_8 = arr[8]
        self.oltModel_id_9 = arr[9]
        self.id_10 = arr[10]
        self.address_11 = arr[11]
        self.deploymentType_12 = arr[12]
        self.equipmentType_13 = arr[13]
        self.id2_14 = arr[14]
        self.isOutdoor_15 = arr[15]
        self.lat_16 = arr[16]
        self.lon_17 = arr[17]
        self.NAME_18 = arr[18]
        self.state_19 = arr[19]
        self.styleCode_20 = arr[20]
        self.tag_21 = arr[21]
        self.tag_building_22 = arr[22]
        self.BuildingID_23 = arr[23]
        self.CableDrawinBoxModelID_24 = arr[24]
        self.scenario_ID_25 = arr[25]
        self.iSite_26 = arr[26]