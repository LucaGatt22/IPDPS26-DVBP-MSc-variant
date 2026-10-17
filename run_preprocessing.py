# %%
import pandas as pd


vmType = pd.read_csv("data/vmType.csv")
vm = pd.read_csv("data/vm.csv")

# %%
mapping = {}
for index, df in vmType.groupby('machineId'):
    if index == 17: # empty requests
        continue
    if index == 20: # empty requests
        continue
    if index == 33: # crash 
        continue
    
    df_list = df.vmTypeId.to_list()
    yes = True
    
    for k,v in mapping.items():
        if(index == 30):
            break
        if(set(v) == set(df_list)):
            print(index, k)
            yes = False
            break
        
    if yes:
        mapping[index] = df_list
validIds = list(mapping.keys())
print(validIds)
print(len(validIds))

#%%
for machineId, vmTypeIds in mapping.items():
    vm_sub = vm[vm['vmTypeId'].isin(vmTypeIds)]
    vm_sub = vm_sub[(vm_sub['starttime'] >= 0) & (vm_sub['endtime'] <= 14)]
    vm_sub.to_csv(f"data/vm_pId_{machineId}.csv", header=True, index=False)

#%%
del vm
del vmType