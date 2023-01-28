import pandas as pd

# ffe_df = pd.read_csv(r'F:\A_CUHK\DTM_HK\cost_estimation_galve\processed_need_elevate_residential_2022_6-5.csv')
ffe_df = pd.read_csv(r'F:\A_CUHK\DTM_HK\cost_estimation_galve\FFE_result_new2_2022_6_2.csv')

indexes_to_drop = []

for index, row in ffe_df.iterrows():

    image_date = str(row['image_date'])
    image_date = image_date.replace('[', '')

    date_process = image_date.split(',')[0]

    if int(date_process) <= 2013:

        indexes_to_drop.append(index)

ffe_df.drop(ffe_df.index[indexes_to_drop], inplace=True )

ffe_df.to_csv(r'F:\A_CUHK\DTM_HK\cost_estimation_galve\FFE_result_new2_after_2014_2022_6_5.csv')
