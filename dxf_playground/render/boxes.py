#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from shapely.geometry import Polygon, LineString, Point
import numpy as np

from dxf_playground.data_access.data_query import DB_Handler
from dxf_playground.render.coordinates import BoundingBox
from dxf_playground.utils.projections import project_point_collection, project_point


class box:
    def __init__(self, properties=None, geometry=None):
        self.properties = properties
        self.geometry = geometry

    def compute_rotation(self):
        x1 = self.properties.lat_38
        y1 = self.properties.lon_39

        x2 = self.properties.lat_55
        y2 = self.properties.lon_56

        vec = (x2 -x1,y2-y1)
        return np.math.atan2(vec[1],vec[0])
    def rectangle(self,geo):
        wi = 2
        return [(geo[0] - wi,geo[1] -wi),
                (geo[0] - wi, geo[1] + wi),
                (geo[0] + wi, geo[1] + wi),
                (geo[0] + wi, geo[1] - wi),
                (geo[0] - wi, geo[1] - wi)
                ]
    def draw_box(self, cx, cy,bloc):

        rx = random.randint(2,5)
        ry = random.randint(2, 5)
        rr = random.randint(0, 360)
        geo = (self.geometry[0] - cx , self.geometry[1] - cy )

        coords = []
        bloc.add_lwpolyline(
            self.rectangle(geo),
            dxfattribs={'color': 3,
                        'layer': "roads", })

        bloc.add_text("Box",
                      dxfattribs={'color': 3}).set_pos(
            (geo[0], geo[1] + 3),
            align='CENTER')




class box_collection(list):
    def __init__(self, dwg,modelspace,scenario_id,bounding_box,bbox):
        list.__init__(self)

        self.dwg = dwg
        self.modelspace = modelspace
        self.scenario_id = scenario_id
        self.bounding_box = bounding_box
        self.bbox = bbox

    def from_data_base(self):
        hndl = DB_Handler()
        result = hndl.query_box(self.scenario_id)
        for res in result:
            cp = box_properties()
            cp.fromArray(res)
            c = box(cp,project_point((cp.lat_38, cp.lon_39)))
            self.append(c)
        print len(self)
        hndl.close()

    def inside_bounding_box(self):
        tmp = box_collection(self.dwg, self.modelspace, self.scenario_id, self.bounding_box,self.bbox)
        for i in self:
            if self.bounding_box.contains(Point(i.geometry)):
                tmp.append(i)
        return tmp

    def draw(self):

        bloc = self.dwg.blocks.new(name="box.block2.A4")
        self.modelspace.add_blockref("box.block2.A4",
                                     (-95 + 840 + 151., 0.),
                                     dxfattribs={
                                         "xscale": 571. / self.bbox.width,
                                         "yscale": 458. / self.bbox.height})

        for i in self:
            i.draw_box(self.bbox.center[0], self.bbox.center[1], bloc)


class box_properties:
    def __init__(self):
        pass

    def fromArray(self,arr):
        self.id_0 = arr[0]
        self.Type_1 = arr[1]
        self.name_2 = arr[2]
        self.styleCode_3 = arr[3]
        self.Techno_4 = arr[4]
        self.boxDst_5 = arr[5]
        self.boxSrc_6 = arr[6]
        self.link_ID_7 = arr[7]
        self.scenario_ID_8 = arr[8]
        self.trench_ID_9 = arr[9]
        self.id_10 = arr[10]
        self.MaxDimaterSheath1_11 = arr[11]
        self.MaxDimaterSheath2_12 = arr[12]
        self.MaxPossibleSheath1_13 = arr[13]
        self.MaxPossibleSheath2_14 = arr[14]
        self.Cost_15 = arr[15]
        self.deploymentType_16 = arr[16]
        self.id2_17 = arr[17]
        self.Length_18 = arr[18]
        self.name_19 = arr[19]
        self.state_20 = arr[20]
        self.cable_Link_21 = arr[21]
        self.link_22 = arr[22]
        self.scenario_ID_23 = arr[23]
        self.trenchModelModel_ID_24 = arr[24]
        self.id_25 = arr[25]
        self.cost_26 = arr[26]
        self.depth_Max_27 = arr[27]
        self.depth_Min_28 = arr[28]
        self.length_Max_29 = arr[29]
        self.length_Min_30 = arr[30]
        self.name_31 = arr[31]
        self.id_32 = arr[32]
        self.address_33 = arr[33]
        self.deploymentType_34 = arr[34]
        self.equipmentType_35 = arr[35]
        self.id2_36 = arr[36]
        self.isOutdoor_37 = arr[37]
        self.lat_38 = arr[38]
        self.lon_39 = arr[39]
        self.NAME_40 = arr[40]
        self.state_41 = arr[41]
        self.styleCode_42 = arr[42]
        self.tag_43 = arr[43]
        self.tag_building_44 = arr[44]
        self.BuildingID_45 = arr[45]
        self.CableDrawinBoxModelID_46 = arr[46]
        self.scenario_ID_47 = arr[47]
        self.iSite_48 = arr[48]
        self.id_49 = arr[49]
        self.address_50 = arr[50]
        self.deploymentType_51 = arr[51]
        self.equipmentType_52 = arr[52]
        self.id2_53 = arr[53]
        self.isOutdoor_54 = arr[54]
        self.lat_55 = arr[55]
        self.lon_56 = arr[56]
        self.NAME_57 = arr[57]
        self.state_58 = arr[58]
        self.styleCode_59 = arr[59]
        self.tag_60 = arr[60]
        self.tag_building_61 = arr[61]
        self.BuildingID_62 = arr[62]
        self.CableDrawinBoxModelID_63 = arr[63]
        self.scenario_ID_64 = arr[64]
        self.iSite_65 = arr[65]