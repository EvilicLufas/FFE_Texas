ENR_Construction_index_1998 = 5920
ENR_Construction_index_2015 = 10035

ENR_Construction_index_2009 = 8570
ENR_Construction_index_2021 = 12133

#ENR BUILIDNG COST INDEX
ENR_BCI_1998 = 3391
ENR_BCI_2009 = 4769
ENR_BCI_2015 = 5517
ENR_BCI_2021 = 6912

List = [19 ,31 ,40, 47, 55, 64, 73, 83, 95, 111, 126]

trans_1 = ENR_Construction_index_2021/ENR_Construction_index_1998
trans_2 = ENR_BCI_2021/ENR_BCI_1998

trans = trans_2/trans_1
trans = trans_1/trans_2

for i in range(len(List)):
    List[i] = List[i]*trans
print(List)