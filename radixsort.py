def radixsort(*args) -> list[int]:
    """
        桶排序
    """
    
    # 获取反转字符串后的list以及最大长度
    rev_args:list[str] = []
    length: int = 0
    for num in args:
        snum = str(num)
        rev_args.append(snum[::-1])
        if len(snum) > length:
            length = len(snum)

    # 初始化存储区
    store: list[str] = rev_args.copy()

    n: int = 0

    # 对反转list做桶排序
    while n < length:
        # 初始化0~9的桶
        buckets:list[list[str]] = [[] for _ in range(10)]
        
        # 把翻转后的字符串放进桶里
        for rnum in store:
            if len(rnum) <= n:
                buckets[0].append(rnum)
                continue
            buckets[int(rnum[n])].append(rnum)
        
        # 重置存储区
        store = []

        # 取出桶里的翻转字符串
        for bucket in buckets:
            for rnum in bucket:
                store.append(rnum)
        
        n += 1

    result: list[int] = []
    # 把翻转字符串翻转回来并转为数字
    for rnum in store:
        snum = rnum[::-1]
        result.append(int(snum))
    
    return result

