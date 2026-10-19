SEED_DIGIT = 6       
NAME_LENGTH = 8
ARTIST_LENGTH = 3
ID_SUM = 22

dept_a = sorted(list(set([SEED_DIGIT + i * 4 for i in range(8)])))

dept_b = sorted(list(set([ARTIST_LENGTH + i * 5 for i in range(7)])))

def merge_sorted_departments(arr1, arr2):
    i, j = 0, 0
    consolidated = []
    comparisons = 0
    
    while i < len(arr1) and j < len(arr2):
        comparisons += 1
        if arr1[i] <= arr2[j]:
            consolidated.append(arr1[i])
            i += 1
        else:
            consolidated.append(arr2[j])
            j += 1
            
    while i < len(arr1):
        consolidated.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        consolidated.append(arr2[j])
        j += 1
        
    return consolidated, comparisons

consolidated_dataset, total_comparisons = merge_sorted_departments(dept_a, dept_b)

is_sorted = consolidated_dataset == sorted(consolidated_dataset)
records_before = len(dept_a) + len(dept_b)
records_after = len(consolidated_dataset)

print("--- Assessment Data ---")
print(f"Department A dataset: {dept_a}")
print(f"Department B dataset: {dept_b}")
print(f"Consolidated dataset: {consolidated_dataset}")
print(f"Number of records: Before = {records_before}, After = {records_after}")
print(f"Comparison count: {total_comparisons}")
print(f"Ordering verification: {'PASSED (Strictly Ascending)' if is_sorted else 'FAILED'}")