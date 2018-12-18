import pygeoj
from shapely.geometry import Polygon, LineString
import numpy as np

from dxf_playground.data_access.data_query import DB_Handler
from dxf_playground.render.coordinates import BoundingBox
from dxf_playground.utils.projections import project_point_collection


class trench:
    def __init__(self, properties=None, geometry=None):
        self.properties = properties
        self.geometry = geometry


    def draw_trench(self, cx, cy,bloc):
        geo = [(i[0] - cx, i[1] - cy) for i in self.geometry]


        bloc.add_lwpolyline(
            geo,
            dxfattribs={'color': 3})
        cent = BoundingBox(np.array(geo)).center
        bloc.add_text(str(int(self.properties.Length_18)) + "m",
                      dxfattribs={'color': 3}).set_pos(
            cent,
            align='CENTER')


class trench_collection(list):
    def __init__(self, dwg,modelspace,scenario_id,bounding_box,bbox):
        list.__init__(self)

        self.dwg = dwg
        self.modelspace = modelspace
        self.scenario_id = scenario_id
        self.bounding_box = bounding_box
        self.bbox = bbox

    def from_data_base(self):
        hndl = DB_Handler()
        result = hndl.query_trenches(self.scenario_id)
        for res in result:
            cp = trench_properties()
            cp.fromArray(res)

            c = trench(cp,project_point_collection([(cp.lat_38, cp.lon_39), (cp.lat_55, cp.lon_56)]))
            self.append(c)
        hndl.close()

    def inside_bounding_box(self):
        tmp = trench_collection(self.dwg, self.modelspace, self.scenario_id, self.bounding_box,self.bbox)
        for i in self:
            if self.bounding_box.contains(LineString(i.geometry)):
                tmp.append(i)
            elif self.bounding_box.intersection(LineString(i.geometry)):
                if str(type(self.bounding_box.intersection(
                        LineString(i.geometry)))) == "<class 'shapely.geometry.linestring.LineString'>":
                    inte = self.bounding_box.intersection(LineString(i.geometry)).coords
                    rd = trench(i.properties, inte)
                    tmp.append(rd)
                else:
                    for line in self.bounding_box.intersection(LineString(i.geometry)):
                        inte = line.coords
                        rd = trench(i.properties, inte)
                        tmp.append(rd)

        return tmp

    def draw(self):
        bloc = self.dwg.blocks.new(name="trench.block1.A4")
        self.modelspace.add_blockref("trench.block1.A4",
                                     (-95 + 840 + 151., 0.),
                                     dxfattribs={
                                         "xscale": 571. / self.bbox.width,
                                         "yscale": 458. / self.bbox.height})

        for i in self:
            i.draw_trench(self.bbox.center[0], self.bbox.center[1], bloc)


class trench_properties:
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