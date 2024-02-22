import pandas as pd


network_df = pd.read_excel("reseau_en_arbre.xlsx")  # Replace with your own file path to the network excel sheet
network_df.shape
network_df.head()

sub_network_df = network_df[network_df['infra_type'] == "a_remplacer"]
sub_network_df.head(50)

infra_sdfs = sub_network_df.groupby(by='infra_id')

for id_infra, infra_sdfs in infra_sdfs:
    print(id_infra)
    print(infra_sdfs)
    print("_"*30)


batiment_sdfs = sub_network_df.groupby(by='id_batiment')

for id_batiment, batiment_sdfs in batiment_sdfs:
    print(id_batiment)
    print(batiment_sdfs)
    print("_"*30)