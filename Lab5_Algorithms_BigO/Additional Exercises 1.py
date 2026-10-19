import string

LAST_NAME = "MAKINANO"
STUDENT_ID = "261256"
FAVORITE_ARTIST = "ADO"

NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)
SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(digit) for digit in STUDENT_ID if digit.isdigit())

char_values = {char: idx + 1 for idx, char in enumerate(string.ascii_uppercase)}
ARTIST_SUM = sum(char_values.get(char.upper(), 0) for char in FAVORITE_ARTIST)

base_val = NAME_LENGTH * ARTIST_LENGTH
original_dataset = sorted(list(set([base_val + i * 3 for i in range(15)])))

rotation_pivot = SEED_DIGIT % len(original_dataset)
if rotation_pivot == 0: 
    rotation_pivot = 3
rotated_dataset = original_dataset[rotation_pivot:] + original_dataset[:rotation_pivot]

target_incident = original_dataset[(ID_SUM + ARTIST_SUM) % len(original_dataset)]

def linear_search(arr, target):
    comparisons = 0
    for idx, val in enumerate(arr):
        comparisons += 1
        if val == target:
            return idx, comparisons
    return -1, comparisons

def rotated_binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0
    
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid, comparisons
            
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1, comparisons

lin_idx, lin_comps = linear_search(rotated_dataset, target_incident)
bin_idx, bin_comps = rotated_binary_search(rotated_dataset, target_incident)

print("--- Assessment Data ---")
print(f"Original Dataset:  {original_dataset}")
print(f"Rotated Dataset:   {rotated_dataset} (Rotated by index {rotation_pivot})")
print(f"Target Incident:   {target_incident}")
print(f"Binary Search Index Found: {bin_idx} (in {bin_comps} comparisons)")
print(f"Linear Search Index Found: {lin_idx} (in {lin_comps} comparisons)\n")