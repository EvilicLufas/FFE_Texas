import pandas as pd
old_df = pd.read_csv(r'F:\A_CUHK\DTM_HK\cost_estimation_galve\above1_5feet_Galvest_cost_FFE_2022_6_4.csv')
new_df = pd.DataFrame(columns=old_df.columns)
new_df_1 = pd.DataFrame(columns=old_df.columns)
new_df_2 = pd.DataFrame(columns=old_df.columns)

for index, row in old_df.iterrows():
    if row['FFE_need_Elevate'] == 'Y':
        new_df.append(row)
        if row['is_residential'] == 'Y':
            new_df_1.append(row)
            if row['area_ft_unreal_too_low'] == 'Y':
                new_df_2.append(row)

new_df.to_csv(r'F:\A_CUHK\DTM_HK\cost_estimation_galve\processed_need_elevate_cost_FFE_2022_6_4.csv')
new_df_1.to_csv(r'F:\A_CUHK\DTM_HK\cost_estimation_galve\processed_with_unreal_area_cost_FFE_2022_6_4.csv')
new_df_2.to_csv(r'F:\A_CUHK\DTM_HK\cost_estimation_galve\processed_true_residential_cost_FFE_2022_6_4.csv')