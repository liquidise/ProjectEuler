import math

sums = {};
for i in range(1, 1000):
    for k in range(1, 1000):
        if i <= k:
            continue

        root = math.sqrt( (i * i) + (k * k) )
        intRoot = int( root )
        if root == intRoot:
            total = i + k + intRoot
            
            if total > 1000:
                continue
            
            if not total in sums:
                sums[total] = 0

            sums[total] += 1

most = {"count": 0, "p": 0}
for i in sums.keys():
    if most['count'] < sums[i]:
        most['count'] = sums[i]
        most['p'] = i
    
    print "p = " , i, "  count = ", sums[i]

print "Most: ", most