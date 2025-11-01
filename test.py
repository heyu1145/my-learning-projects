from radixsort import radixsort
from quicksort import quicksort
import random
import time
test: list[list[int]] = [
    [random.randint(1,100) for _ in range(random.randint(50,500))],
    [random.randint(1,1000) for _ in range(random.randint(500,5000))],
    [random.randint(5,10000) for _ in range(random.randint(5000,10000))]
]
for testcase in test:
    starttime = time.time()
    radix = radixsort(*testcase)
    radixtime = time.time()
    quick = quicksort(testcase)
    quicktime = time.time()
    sort = sorted(testcase)
    sorttime = time.time()
    print(f'Python排序时间: {sorttime - quicktime:3f}\n桶排序时间: {radixtime - starttime:3f}\n桶排序是否正确: {'yes' if radix == sort else 'no'}\n快速排序时间: {quicktime - radixtime:3f}\n快速排序是否正确: {'yes' if quick == sort else 'no'}')
    print('=' * 30,end='\n\n')
