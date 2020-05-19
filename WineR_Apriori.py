import pandas as pd
import numpy as np
import itertools
import json

def generate_counts_C(candidate_C,dict_table):
    temp_C=[]
    for candidate_itemset in candidate_C:
        temp_C.append({"itemset":candidate_itemset,"support":0})
        for dict_list in dict_table.values(): 
            if(all(x in dict_list for x in candidate_itemset)):
                temp_C[-1]["support"]+=1   
    return temp_C
def has_infrequent_subset(candidate_itemset,set_itemset,k):
    subsets = list(itertools.combinations(candidate_itemset, k-1))
    for x in subsets:
        if(list(x) not in set_itemset):
            return True
    return False
def check_share_condition(itemset_l1,itemset_l2,num_share): 
    for x in range(num_share):
        if(itemset_l1[x]!=itemset_l2[x]):
            return False
    if(itemset_l1[num_share]>=itemset_l2[num_share]): 
        return False
    return True
def generate_candidate_C(set_itemset,k):
    num_share=k-2 
    candidate_C=[]
    for itemset_l1_index, itemset_l1 in enumerate(set_itemset):
        for itemset_l2_index, itemset_l2 in enumerate(set_itemset):
            if(check_share_condition(itemset_l1,itemset_l2,num_share)):
                candidate_itemset=sorted(list(set().union(itemset_l1,itemset_l2))) 
                if(has_infrequent_subset(candidate_itemset,set_itemset,k) is False): 
                    candidate_C.append(candidate_itemset)    
    return candidate_C 
def prune(temp_C, min_sup_count):
    pruned_temp_C = [x for x in temp_C if x["support"] >= min_sup_count]
    pruned_temp_L = sorted([x["itemset"] for x in temp_C if x["support"] >= min_sup_count])
    return pruned_temp_L,pruned_temp_C
def generate_counts_C1(dict_table):
    temp_C=[]
    items = [item for dict_list in dict_table.values() for item in dict_list]
    values, counts = np.unique(items, return_counts=True)
    for x in range(len(values)):
        temp_C.append({"itemset":[values[x]],"support":counts[x]})
    return temp_C

def apriori(dict_table,support):
    L=[]
    C=[]
    min_sup_count = len(dict_table)*support    
    print("Generating Frequent 1-itemsets")
    counts_C1 = generate_counts_C1(dict_table) 
    pruned_L1,pruned_C1 = prune(counts_C1, min_sup_count) 
    L.append(pruned_L1)
    for x in pruned_C1:
        x['support']=(float(x['support'])/float(len(dict_table)))
    C.append(pruned_C1)  
    k=2
    while(1):
        print("Generating Frequent "+str(k)+"-itemsets")
        candidate_C = generate_candidate_C(L[k-2],k=k) 
        counts_C = generate_counts_C(candidate_C,dict_table) 
        pruned_L,pruned_C = prune(counts_C, min_sup_count)       
        if(not pruned_L): 
            break       
        L.append(pruned_L)
        for x in pruned_C:
            x['support']=(float(x['support'])/float(len(dict_table)))
        C.append(pruned_C)
        k=k+1
    return L,C

if __name__=='__main__':
    adult = pd.read_csv('F:\course\web\data\item_wine.csv', index_col = 0)    # 对应于ipynb文件中的csv存放地址 不要第一列 (0 - index)
    # adult.columns = ['country', 'province','variety', 'points_new', 'price_new']   # 选中的wine产生的country province variety points_new price_new
   
    candidate = {}
    temp_list=[]
    for index, data in adult.iterrows():
        candidate[str(index)] = data.tolist()
    support = 0.0772    #  对应于ipynb中的rule_1(10000个) 耗时则可以调高
    L,C = apriori(candidate, support=support)
    number_of_frequent_itemsets = sum(len(x) for x in L)
    print(number_of_frequent_itemsets)  # frequent item的个数
    with open("wine_review_w2.json","w") as f:
        f.write(json.dumps(C, indent=4))
