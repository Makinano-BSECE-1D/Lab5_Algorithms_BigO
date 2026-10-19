import time
import random

base_dataset = [24, 27, 30, 33, 36, 39, 42, 45, 48, 51]

sorted_input = sorted(base_dataset)
reverse_input = sorted(base_dataset, reverse=True)
random.seed(42)  
random_input = base_dataset.copy()
random.shuffle(random_input)

def bubble_sort(arr_in):
    arr = arr_in.copy()
    n = len(arr)
    comps, moves = 0, 0
    start_time = time.perf_counter()
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comps += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                moves += 1  
                swapped = True
        if not swapped:
            break
            
    exec_time = (time.perf_counter() - start_time) * 1000  
    return comps, moves, exec_time

def selection_sort(arr_in):
    arr = arr_in.copy()
    n = len(arr)
    comps, moves = 0, 0
    start_time = time.perf_counter()
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comps += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            moves += 1  
            
    exec_time = (time.perf_counter() - start_time) * 1000
    return comps, moves, exec_time

def insertion_sort(arr_in):
    arr = arr_in.copy()
    n = len(arr)
    comps, moves = 0, 0
    start_time = time.perf_counter()
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comps += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                moves += 1 
                j -= 1
            else:
                break
        arr[j + 1] = key
        
    exec_time = (time.perf_counter() - start_time) * 1000
    return comps, moves, exec_time

datasets = {"Sorted": sorted_input, "Reverse": reverse_input, "Random": random_input}
results = {}

for name, data in datasets.items():
    results[name] = {
        "Bubble": bubble_sort(data),
        "Selection": selection_sort(data),
        "Insertion": insertion_sort(data)
    }

print(f"Generated Order Dataset Base: {base_dataset}\n")
for state in ["Sorted", "Reverse", "Random"]:
    print(f"--- {state} Input State Metrics ---")
    for algo in ["Bubble", "Selection", "Insertion"]:
        c, m, t = results[state][algo]
        print(f" * {algo} Sort -> Comparisons: {c} | Movements: {m} | Time: {t:.4f} ms")
    print()