#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygeoj
from shapely.geometry import Polygon, LineString, Point
import numpy as np

from dxf_playground.data_access.data_query import DB_Handler
from dxf_playground.render.coordinates import BoundingBox
from dxf_playground.utils.projections import project_point_collection, project_point


class subscriber_dwelling:
    def __init__(self, properties=None, geometry=None):
        self.properties = properties
        self.geometry = geometry


    def draw_subscriber_dwelling(self, cx, cy,bloc):
        geo = (self.geometry[0] - cx, self.geometry[1] - cy)
        bloc.add_blockref("The door", geo)
        bloc.add_text(self.properties.name_3,
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



class subscriber_dwelling_collection(list):
    def __init__(self, dwg,modelspace,scenario_id,bounding_box,bbox):
        list.__init__(self)

        self.dwg = dwg
        self.modelspace = modelspace
        self.scenario_id = scenario_id
        self.bounding_box = bounding_box
        self.bbox = bbox

    def from_data_base(self):
        hndl = DB_Handler()
        result = hndl.query_subscriber_dwelling(self.scenario_id)
        for res in result:
            cp = subscriber_dwelling_properties()
            cp.fromArray(res)
            c = subscriber_dwelling(cp,project_point((cp.lat, cp.lon)))
            self.append(c)
        hndl.close()

    def inside_bounding_box(self):
        tmp = subscriber_dwelling_collection(self.dwg, self.modelspace, self.scenario_id, self.bounding_box,self.bbox)
        for i in self:
            if self.bounding_box.contains(Point(i.geometry)):
                tmp.append(i)
        return tmp

    def draw(self):
        bloc = self.dwg.blocks.new(name="subscriber_dwelling.block1.A4")
        self.modelspace.add_blockref("subscriber_dwelling.block1.A4",
                                     (-95., 0.),
                                     dxfattribs={
                                         "xscale": 571. / self.bbox.width,
                                         "yscale": 458. / self.bbox.height})

        for i in self:
            i.draw_subscriber_dwelling(self.bbox.center[0], self.bbox.center[1], bloc)

        bloc = self.dwg.blocks.new(name="subscriber_dwelling.block2.A4")
        self.modelspace.add_blockref("subscriber_dwelling.block2.A4",
                                     (-95 + 840 + 151., 0.),
                                     dxfattribs={
                                         "xscale": 571. / self.bbox.width,
                                         "yscale": 458. / self.bbox.height})

        for i in self:
            i.draw_subscriber_dwelling(self.bbox.center[0], self.bbox.center[1], bloc)




class subscriber_dwelling_properties:
    def __init__(self):
        pass

    def fromArray(self,arr):
        self.id = arr[0]
        self.directionInversed = arr[1]
        self.id2 = arr[2]
        self.initialEq1 = arr[3]
        self.initialEq2 = arr[4]
        self.isIndoor = arr[5]
        self.length = arr[6]
        self.name = arr[7]
        self.state = arr[8]
        self.type = arr[9]
        self.cableModel_ID = arr[10]
        self.link = arr[11]
        self.subtubes_ID = arr[12]
        self.id_0 = arr[13]
        self.Attenuation_1310 = arr[14]
        self.Attenuation_1550 = arr[15]
        self.Description = arr[16]
        self.FOPerRibbon = arr[17]
        self.Height = arr[18]
        self.Max_Length = arr[19]
        self.NbUnitPerTube = arr[20]
        self.Nb_FO = arr[21]
        self.Nb_Slott = arr[22]
        self.Nb_Tubes = arr[23]
        self.Price = arr[24]
        self.Reference = arr[25]
        self.Weight = arr[26]
        self.Width = arr[27]
        self.application = arr[28]
        self.standard = arr[29]
        self.structure = arr[30]
        self.Constructor = arr[31]
        self.Code = arr[32]
        self.DeploymentType = arr[33]
        self.id_building = arr[34]
        self.adresse = arr[35]
        self.appartmentsPerFloorPerBlocString = arr[36]
        self.automated = arr[37]
        self.basementDevicePerBlocString = arr[38]
        self.type_1 = arr[39]
        self.businessPerFloorPerBlocString = arr[40]
        self.businessType = arr[41]
        self.connectionDate = arr[42]
        self.connectionType = arr[43]
        self.contractDate = arr[44]
        self.customerId = arr[45]
        self.distanceBasementAndFirstFloor = arr[46]
        self.distanceBetweenFloors = arr[47]
        self.floorDevicePerBlocString = arr[48]
        self.horizontalDistance = arr[49]
        self.id_2 = arr[50]
        self.interFloorDistance = arr[51]
        self.lat = arr[52]
        self.lon = arr[53]
        self.name_3 = arr[54]
        self.nbBloc = arr[55]
        self.nbPrise = arr[56]
        self.nbRequiredFibre = arr[57]
        self.numberInhabitant = arr[58]
        self.Phone_Number = arr[59]
        self.residOrBusiness = arr[60]
        self.residencePerFloorPerBlocString = arr[61]
        self.SpliceClosurePerBlocString = arr[62]
        self.state_4 = arr[63]
        self.status = arr[64]
        self.Box_ID = arr[65]
        self.Ont = arr[66]
        self.Scenario_ID = arr[67]
        self.zoneID = arr[68]
        self.id_5 = arr[69]
        self.name_6 = arr[70]
        self.Sheat_ID = arr[71]
        self.sheathModel_ID = arr[72]
        self.id_7 = arr[73]
        self.MaximumSubtubesCapacity = arr[74]
        self.name_8 = arr[75]
        self.position = arr[76]
        self.position2 = arr[77]
        self.sheathModel_ID_9 = arr[78]
        self.trench_ID = arr[79]
        self.id_10 = arr[80]
        self.Type = arr[81]
        self.name_11 = arr[82]
        self.styleCode = arr[83]
        self.Techno = arr[84]
        self.boxDst = arr[85]
        self.boxSrc = arr[86]
        self.link_ID = arr[87]
        self.scenario_ID = arr[88]
        self.trench_ID_12 = arr[89]
        self.id_13 = arr[90]
        self.address = arr[91]
        self.deploymentType = arr[92]
        self.equipmentType = arr[93]
        self.id2_14 = arr[94]
        self.isOutdoor = arr[95]
        self.lat_15 = arr[96]
        self.lon_16 = arr[97]
        self.NAME = arr[98]
        self.state_17 = arr[99]
        self.styleCode_18 = arr[100]
        self.tag = arr[101]
        self.tag_building = arr[102]
        self.BuildingID = arr[103]
        self.CableDrawinBoxModelID = arr[104]
        self.scenario_ID_19 = arr[105]
        self.iSite = arr[106]
