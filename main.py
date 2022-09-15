'''
Author: Xiaoxin Mi
Date: 14-09-2022
'''
import shapefile


# 1. read shp file, save the coordinates and feature code
# 2. cluster the polylines according to feature code
# 3. write the polylines separately
# reference: https://pypi.org/project/pyshp/#description

def read_shapefile(filepath):
    polylines = dict()
    shape_reader = shapefile.Reader(filepath)
    dashed_lane_writer = shapefile.Writer('/media/mxx/Mixixizi_Passport/2_Data/1_zhangjiang_8qu_chengshi/ContinuousLane/dashed_lane', \
                                          shapeType=shape_reader.shapeType)
    solid_lane_writer = shapefile.Writer('/media/mxx/Mixixizi_Passport/2_Data/1_zhangjiang_8qu_chengshi/ContinuousLane/solid_lane',\
                                         shapeType=shape_reader.shapeType)
    dashed_lane_writer.fields = shape_reader.fields[1:] # skip first deletion field
    solid_lane_writer.fields = shape_reader.fields[1:]  # skip first deletion field
    for shaperec in shape_reader.iterShapeRecords():
        feature_code = shaperec.record[2]
        if feature_code == '401111' or feature_code == '401112' or feature_code == '401113' or \
            feature_code == '401114' or feature_code == '401115' or feature_code == '401116' or \
            feature_code == '401117' or feature_code == '401131' or feature_code == '401132' or \
            feature_code == '401133' or feature_code == '401134' or feature_code == '401135' or \
            feature_code == '401136' or feature_code == '401137':
            # dashed lane
            print("I'm  dashed lane. ", feature_code)
            dashed_lane_writer.record(*shaperec.record)
            dashed_lane_writer.shape(shaperec.shape)
        elif feature_code == '401121' or feature_code == '401141':
            # solid lane:
            print("I'm solid lane. ", feature_code)
            solid_lane_writer.record(*shaperec.record)
            solid_lane_writer.shape(shaperec.shape)
        else:
            # 401122 == 'Stop line'
            # 401211 == 'Zebra crossing'
            # 401142 == ??? to confirm
            print("I'm not dashed nor solid lane. ", feature_code)

    dashed_lane_writer.close()
    solid_lane_writer.close()
    return polylines

def write_shapefile(filepath, data):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    raw_filepath = "/media/mxx/Mixixizi_Passport/2_Data/1_zhangjiang_8qu_chengshi/ContinuousLane/TrafficInfo_L/TrafficInfo_L.shp"
    read_shapefile(raw_filepath)

