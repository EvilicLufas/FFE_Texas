import lux
import pandas as pd

ffe_df = pd.read_csv('/home/developer/Downloads/DTM_HK/cost_estimation_galve/building_footprints_cost_FFE_BFE.csv')
ffe_df[['cost_2015', 'area_ft2']].plot.hist(bins=30)


ffe_df[['cost_2015', 'area_ft2']].plot.box()
