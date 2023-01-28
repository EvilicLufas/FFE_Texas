# FID,FID_1,OBJECTID,Parcel_ID,area_m2,image,panoId,EC_id,confidence,col,bottom_row,top_row,
# FFE_gsv_m,delta_h,distance,sink_dista,camera_h,camera_dem,phi,pano_lat,pano_lon,target_lat,target_lon,
# image_date,edge,is_lowest_,SFHA_TF,STATIC_BFE,Under_fld

import pandas as pd


# data = pd.read_csv('C:/Users/asus/Desktop/Python/test.csv',chunksize=1000000,header=None,sep=';'

# ffe_df = pd.read_csv('/home/developer/Downloads/DTM_HK/cost_estimation_galve/building_footprints_BFE.csv')
# ffe_df = pd.read_csv(r'F:\A_CUHK\DTM_HK\cost_estimation_galve\building_footprints_BFE.csv')
ffe_df = pd.read_csv(r'F:\A_CUHK\DTM_HK\cost_estimation_galve\Building_footprints_220602.csv')

cost_df = pd.DataFrame(columns=['FID', 'FID_1', 'OBJECTID', 'Parcel_ID', 'area_m2', 'image', 'panoId', 'EC_id',
                                'confidence', 'col', 'bottom_row', 'top_row', 'FFE_gsv_m', 'delta_h', 'distance',
                                'sink_dista', 'camera_h', 'camera_dem', 'phi', 'pano_lat', 'pano_lon', 'target_lat',
                                'target_lon', 'image_date',
                                'edge',
                                'is_lowest_', 'SFHA_TF', 'STATIC_BFE', 'Under_fld',
                                # =============== below new cost info==================================
                                'area_m2', 'area_ft2', 'FFE_gsv_m', 'FFE_gsv_ft', 'STATIC_BFE',
                                'FFE_need_Elevate',
                                'FFE_elevation_ft', 'BFE_MINUS_FFE',
                                'galveston_building_systems_location_factor_2021',
                                'galveston_area_modification_factor_2015',
                                # 'galveston_location_factor_2015',
                                'ENR_Construction_index_2015', 'ENR_Construction_index_1998',
                                'rsmeans_ENR_Construction_index_2015',
                                'rsmeans_construction_index_2021',

                                # 'ENR_BCI_index_2015',
                                'area_ft_unreal_too_low',

                                'ENR_Construction_index_2021',

                                'PCI_Family_house_construction_1998',
                                'PCI_Family_house_construction_2015',
                                'PCI_Family_house_construction_2021',

                                # 'foundation_type_set_as'  frame / slab

                                'cost_1998_equal', 'cost_2015_equal',
                                'cost_2021_RSMeans', 'cost_2021_ENR_BCI', 'cost_2021_PCI_Family_house'
                                ,'is_residential'])

print(cost_df)

# Galveston requires 1.5 ft
Elev_galveston = 1.5
#FEMA requires at least 1 ft
Elev_FEMA = 1


# 775 Galveston 98.8 64.0 83.8

# 775 Galveston Residential, Commercial  .81 .84

# galveston_residential_location_factor_2021 = 0.81
galveston_building_systems_location_factor_2021 = 0.838
galveston_building_systems_location_factor_2015 = 0.852
# galveston's mod factor is 775, 10% , Texas average is -1%
galveston_area_modification_factor_2015 = 1.1

# https://data.gov.ie/dataset/national-house-construction-cost-index
# ENR_Construction_index_1998 = 124.9
# ENR_Construction_index_2015 = 207.1

ENR_Construction_index_1998 = 5920
ENR_Construction_index_2015 = 10035
# construction_index_2021 = 12133


# https://edzarenski.com/2022/02/11/construction-inflation-2022/

# https://www.mortenson.com/cost-index
# (JANUARY 2009 = 100)  167.4 national Overall Construction Cost Index (2021)
# https://www.census.gov/construction/nrc/historical_data/-----------------------------------------------+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# RS Means construction index // 2015 : 88.8 // 2021 : 112  (base 2019 : 100)
# ENR BCI index 2015 : 89.9 // 2021 : 112.7  (base 2019 : 100)

# PPI residential inputs + labor // 2015 : 88.7 // 2021 : 121.1  (base 2019 : 100)
# US Cen Bur NEW homes Lasperyes // 2015 : 84.8 // 2021 : 116.1
# S&P/case shiller HomePrice NATIONAL // 2015 : 82 // 2021 : 123.7


rsmeans_ENR_Construction_index_2015 = 88.8
rsmeans_construction_index_2021 = 121.1
# ENR_BCI_index_2015 = 89.9

ENR_Construction_index_2021 = 12133

# https://www.census.gov/construction/cpi/pdf/descpi_uc.pdf
# Lasperyes Price Index of New Single-family houses under construction // 1998 : 72.5 // 2015 : 114 // 2021 : 156

PCI_Family_house_construction_1998 = 72.5
PCI_Family_house_construction_2015 = 114
PCI_Family_house_construction_2021 = 156

C_basic_slab = 47  # slab

C_basic_frame = 17  # frame
C_mid = 0.75  # (2< range =<8) , 17 + 0.75 = 17.75 per sq ft
C_high = 1  # (range > 8) , 17 + 0.

# 75 = 17.75 per sq ft

for index, row in ffe_df.iterrows():

    FID, FID_1, OBJECTID, Parcel_ID, area_m2, image, panoId, EC_id, confidence, col, bottom_row, top_row, FFE_gsv_m, delta_h, distance, sink_dista, camera_h, camera_dem, phi, pano_lat, pano_lon, target_lat, target_lon, image_date, edge, is_lowest_, SFHA_TF, STATIC_BFE, Under_fld = \
        row['FID'], row['FID_1'], row['OBJECTID'], row['Parcel_ID'], row['area_m2'], row['image'], row['panoId'], row[
            'EC_id'], row['confidence'], row['col'], row['bottom_row'], row['top_row'], row['FFE_gsv_m'], row[
            'delta_h'], \
        row['distance'], row['sink_dista'], row['camera_h'], row['camera_dem'], row['phi'], row['pano_lat'], row[
            'pano_lon'], row['target_lat'], row['target_lon'], row['image_date'], row['edge'], row['is_lowest_'], row[
            'SFHA_TF'], row['STATIC_BFE'], row['Under_fld']

    # print(row['area_m2'], row['FFE_gsv_m'], row['STATIC_BFE'])
    print(FID, FID_1, OBJECTID, Parcel_ID, area_m2, image, panoId, EC_id, confidence, col, bottom_row, top_row,
          FFE_gsv_m, delta_h, distance, sink_dista, camera_h, camera_dem, phi, pano_lat, pano_lon, target_lat,
          target_lon, image_date, edge, is_lowest_, SFHA_TF, STATIC_BFE, Under_fld)

    area_m2, FFE_gsv_m, STATIC_BFE = row['area_m2'], row['FFE_gsv_m'], row['STATIC_BFE']

    FFE_gsv_ft = row['FFE_gsv_m'] / 0.3048
    area_ft2 = row['area_m2'] / (0.3048 * 0.3048)

    # if STATIC_BFE == -9999:
    #     STATIC_BFE = 0

    is_residential = 'N'
    if area_ft2 < 8000:
        is_residential = 'Y'

    BFE_MINUS_FFE = STATIC_BFE - FFE_gsv_ft

    # if BFE_MINUS_FFE <= 0:
    if BFE_MINUS_FFE <= -1.5:
        FFE_need_Elevate = 'N'
        FFE_elevation_ft = 0
    elif STATIC_BFE == -9999:
        FFE_need_Elevate = 'N' # -9999 means no BFE, 0.2% flood zone no need to elevate
        FFE_elevation_ft = 0
    else:
        FFE_need_Elevate = 'Y'
        # FFE_elevation_ft = BFE_MINUS_FFE
        FFE_elevation_ft = BFE_MINUS_FFE + 1.5

    if area_ft2 < 765:
        area_ft_unreal_too_low = 'Y'
    else:
        area_ft_unreal_too_low = 'N'

    if FFE_elevation_ft == 0:
        cost_1998_equal = 0
    elif 0 < FFE_elevation_ft <= 2:
        cost_1998_equal = area_ft2 * C_basic_frame
    elif FFE_elevation_ft <= 8:
        cost_1998_equal = area_ft2 * C_basic_frame + area_ft2 * C_mid * (FFE_elevation_ft - 2)
    else:
        # cost_1998_equal = area_ft2 * C_basic_frame + area_ft2 * C_high * (FFE_elevation_ft - 8)
        cost_1998_equal = area_ft2 * C_basic_frame + area_ft2 * C_mid * 6 + area_ft2 * C_high * (FFE_elevation_ft - 8)


    cost_2015_equal = cost_1998_equal * (
            ENR_Construction_index_2015 / ENR_Construction_index_1998) * galveston_building_systems_location_factor_2015

    cost_2021_RSMeans = cost_2015_equal * (
            rsmeans_construction_index_2021 / rsmeans_ENR_Construction_index_2015) * galveston_building_systems_location_factor_2021

    cost_2021_ENR_BCI = cost_2015_equal * (
            ENR_Construction_index_2021 / ENR_Construction_index_2015) * galveston_building_systems_location_factor_2021

    cost_2021_PCI_Family_house = cost_2015_equal * (
            PCI_Family_house_construction_2021 / PCI_Family_house_construction_2015) * galveston_building_systems_location_factor_2021

    df_tmp = pd.DataFrame([[FID, FID_1, OBJECTID, Parcel_ID, area_m2, image, panoId, EC_id,
                            confidence, col, bottom_row, top_row, FFE_gsv_m, delta_h, distance,
                            sink_dista, camera_h, camera_dem, phi, pano_lat, pano_lon, target_lat, target_lon,
                            image_date,
                            edge,
                            is_lowest_, SFHA_TF, STATIC_BFE, Under_fld,

                            area_m2, area_ft2, FFE_gsv_m, FFE_gsv_ft, STATIC_BFE, FFE_need_Elevate,
                            FFE_elevation_ft, BFE_MINUS_FFE, galveston_building_systems_location_factor_2021,
                            # galveston_location_factor_2015,
                            galveston_area_modification_factor_2015,

                            ENR_Construction_index_2015, ENR_Construction_index_1998,
                            rsmeans_ENR_Construction_index_2015,
                            rsmeans_construction_index_2021,
                            # ENR_BCI_index_2015,
                            area_ft_unreal_too_low,
                            ENR_Construction_index_2021,

                            PCI_Family_house_construction_1998,
                            PCI_Family_house_construction_2015,
                            PCI_Family_house_construction_2021,

                            cost_1998_equal, cost_2015_equal,
                            cost_2021_RSMeans, cost_2021_ENR_BCI, cost_2021_PCI_Family_house, is_residential
                            ]])
    # 修改df4的column和df3的一致
    df_tmp.columns = cost_df.columns
    # 把两个dataframe合并，需要设置 ignore_index=True
    cost_df = pd.concat([cost_df, df_tmp], ignore_index=True)
    # new_df.append()
# cost_df.to_csv('/home/developer/Downloads/DTM_HK/cost_estimation_galve/building_footprints_cost_FFE_BFE.csv')
# cost_df.to_csv(r'F:\A_CUHK\DTM_HK\cost_estimation_galve\15_equal_Galvest_building_footprints_cost_FFE.csv')
cost_df.to_csv(r'F:\A_CUHK\DTM_HK\cost_estimation_galve\above1_5feet_Galvest_cost_FFE_2022_6_2.csv')
