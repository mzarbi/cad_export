#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shapely.geometry import Polygon, LineString, Point
import numpy as np

from dxf_playground.data_access.data_query import DB_Handler
from dxf_playground.render.coordinates import BoundingBox
from dxf_playground.utils.projections import project_point_collection, project_point


class fdh:
    def __init__(self, properties=None, geometry=None):
        self.properties = properties
        self.geometry = geometry


    def draw_fdh(self, cx, cy,bloc):

        geo = (self.geometry[0] - cx, self.geometry[1] - cy)
        bloc.add_blockref("OCC", geo, dxfattribs={
            "xscale":0.5,
            "yscale":0.5
        })
        bloc.add_text("FDH",
                      dxfattribs={'color': 7}).set_pos(
            (geo[0], geo[1] - 3),
            align='CENTER')


class fdh_collection(list):
    def __init__(self, dwg,modelspace,scenario_id,bounding_box,bbox):
        list.__init__(self)

        self.dwg = dwg
        self.modelspace = modelspace
        self.scenario_id = scenario_id
        self.bounding_box = bounding_box
        self.bbox = bbox

    def from_data_base(self):
        hndl = DB_Handler()
        result = hndl.query_fdh(self.scenario_id)
        for res in result:
            cp = fdh_properties()
            cp.fromArray(res)
            c = fdh(cp,project_point((cp.lat_18, cp.lon_19)))
            self.append(c)
        hndl.close()

    def inside_bounding_box(self):
        tmp = fdh_collection(self.dwg, self.modelspace, self.scenario_id, self.bounding_box,self.bbox)
        for i in self:
            if self.bounding_box.contains(Point(i.geometry)):
                tmp.append(i)
        return tmp

    def draw(self):
        bloc = self.dwg.blocks.new(name="fdh.block1.A4")
        self.modelspace.add_blockref("fdh.block1.A4",
                                     (-95., 0.),
                                     dxfattribs={
                                         "xscale": 571. / self.bbox.width,
                                         "yscale": 458. / self.bbox.height})

        for i in self:
            i.draw_fdh(self.bbox.center[0], self.bbox.center[1], bloc)


class fdh_properties:
    def __init__(self):
        pass

    def fromArray(self,arr):
        self.Equipment_ID_0 = arr[0]
        self.bBackbone_1 = arr[1]
        self.NAME_2 = arr[2]
        self.tNetworkName_3 = arr[3]
        self.state_4 = arr[4]
        self.Tags_5 = arr[5]
        self.VerticalDistance_6 = arr[6]
        self.CableDrawnBox_ID_7 = arr[7]
        self.id2_8 = arr[8]
        self.isBasementDevice_9 = arr[9]
        self.FdhModelId_10 = arr[10]
        self.Scenario_ID_11 = arr[11]
        self.id_12 = arr[12]
        self.address_13 = arr[13]
        self.deploymentType_14 = arr[14]
        self.equipmentType_15 = arr[15]
        self.id2_16 = arr[16]
        self.isOutdoor_17 = arr[17]
        self.lat_18 = arr[18]
        self.lon_19 = arr[19]
        self.NAME_20 = arr[20]
        self.state_21 = arr[21]
        self.styleCode_22 = arr[22]
        self.tag_23 = arr[23]
        self.tag_building_24 = arr[24]
        self.BuildingID_25 = arr[25]
        self.CableDrawinBoxModelID_26 = arr[26]
        self.scenario_ID_27 = arr[27]
        self.iSite_28 = arr[28]