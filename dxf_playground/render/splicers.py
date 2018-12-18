#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shapely.geometry import Polygon, LineString, Point
import numpy as np

from dxf_playground.data_access.data_query import DB_Handler
from dxf_playground.render.coordinates import BoundingBox
from dxf_playground.utils.projections import project_point_collection, project_point


class splicer:
    def __init__(self, properties=None, geometry=None):
        self.properties = properties
        self.geometry = geometry


    def draw_splicer(self, cx, cy,bloc):
        geo = (self.geometry[0] - cx, self.geometry[1] - cy)
        bloc.add_blockref("Closure", geo)


        bloc.add_text(str(self.properties.FusionSpliceNb_32) + "C",
                      dxfattribs={'color': 7}).set_pos(
            (geo[0],geo[1]-3),
            align='CENTER')
        """
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

class splicer_collection(list):
    def __init__(self, dwg,modelspace,scenario_id,bounding_box,bbox):
        list.__init__(self)

        self.dwg = dwg
        self.modelspace = modelspace
        self.scenario_id = scenario_id
        self.bounding_box = bounding_box
        self.bbox = bbox

    def from_data_base(self):
        hndl = DB_Handler()
        result = hndl.query_splicer(self.scenario_id)
        for res in result:
            cp = splicer_properties()
            cp.fromArray(res)
            c = splicer(cp,project_point((cp.lat_6, cp.lon_7)))
            self.append(c)
        hndl.close()

    def inside_bounding_box(self):
        tmp = splicer_collection(self.dwg, self.modelspace, self.scenario_id, self.bounding_box,self.bbox)
        for i in self:
            if self.bounding_box.contains(Point(i.geometry)):
                tmp.append(i)
        return tmp

    def draw(self):
        bloc = self.dwg.blocks.new(name="splicers.block1.A4")
        self.modelspace.add_blockref("splicers.block1.A4",
                                     (-95., 0.),
                                     dxfattribs={
                                         "xscale": 571. / self.bbox.width,
                                         "yscale": 458. / self.bbox.height})

        for i in self:
            i.draw_splicer(self.bbox.center[0], self.bbox.center[1], bloc)

        bloc = self.dwg.blocks.new(name="splicers.block2.A4")
        self.modelspace.add_blockref("splicers.block2.A4",
                                     (-95 + 840 + 151., 0.),
                                     dxfattribs={
                                         "xscale": 571. / self.bbox.width,
                                         "yscale": 458. / self.bbox.height})

        for i in self:
            i.draw_splicer(self.bbox.center[0], self.bbox.center[1], bloc)


class splicer_properties:
    def __init__(self):
        pass

    def fromArray(self,arr):
        self.id_0 = arr[0]
        self.address_1 = arr[1]
        self.deploymentType_2 = arr[2]
        self.equipmentType_3 = arr[3]
        self.id2_4 = arr[4]
        self.isOutdoor_5 = arr[5]
        self.lat_6 = arr[6]
        self.lon_7 = arr[7]
        self.NAME_8 = arr[8]
        self.state_9 = arr[9]
        self.styleCode_10 = arr[10]
        self.tag_11 = arr[11]
        self.tag_building_12 = arr[12]
        self.BuildingID_13 = arr[13]
        self.CableDrawinBoxModelID_14 = arr[14]
        self.scenario_ID_15 = arr[15]
        self.iSite_16 = arr[16]
        self.Equipment_ID_17 = arr[17]
        self.bBackbone_18 = arr[18]
        self.NAME_19 = arr[19]
        self.tNetworkName_20 = arr[20]
        self.state_21 = arr[21]
        self.Tags_22 = arr[22]
        self.VerticalDistance_23 = arr[23]
        self.CableDrawnBox_ID_24 = arr[24]
        self.attenuation_25 = arr[25]
        self.id2_26 = arr[26]
        self.Splice_ClosureModel_ID_27 = arr[27]
        self.id_28 = arr[28]
        self.Reference_29 = arr[29]
        self.ProductCode_30 = arr[30]
        self.Constructor_ID_31 = arr[31]
        self.FusionSpliceNb_32 = arr[32]
        self.MechanicalSpliceNb_33 = arr[33]
        self.FusionSpliceLoss_34 = arr[34]
        self.MechanicalSpliceLoss_35 = arr[35]
        self.InputCable_36 = arr[36]
        self.OutputCable_37 = arr[37]
        self.NbCassette_38 = arr[38]
        self.Height_39 = arr[39]
        self.Length_40 = arr[40]
        self.Depth_41 = arr[41]
        self.Diameter_42 = arr[42]
        self.Weight_43 = arr[43]
        self.Price_44 = arr[44]
        self.SpliceType_45 = arr[45]
        self.Constructor_46 = arr[46]
        self.NbColumn_47 = arr[47]
        self.Description_48 = arr[48]
        self.InputSplitter_49 = arr[49]
        self.OutputSplitter_50 = arr[50]