nbalon, npred = map(int,input().split())
balons = list(map(int,input().split()))
preds = list(map(int,input().split()))

def optimized_find_subsets_sums(arr, preds):
    results = {}
    preds_set = set(preds)  # Convert list to set for O(1) look-up
    max_pred = max(preds)
    subset_sums = set([0])

    for num in arr:
        new_sums = set()
        for sum in subset_sums:
            new_sum = sum + num
            if new_sum <= max_pred:
                new_sums.add(new_sum)
                if new_sum in preds_set:
                    results[new_sum] = "yes"
                    if preds_set.issubset(results.keys()):
                        return results
        subset_sums.update(new_sums)

    for pred in preds:
        if pred not in results:
            results[pred] = "no"

    return results 
 

results = optimized_find_subsets_sums(balons, preds)

for pred in preds:
    print(results.get(pred, "no"))

