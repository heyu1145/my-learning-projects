function quicksort(nums)
    if #nums <= 1 then
        return nums
    end
    
    local pivot = nums[math.floor(#nums / 2) + 1]  -- Lua 索引从1开始
    local left = {}
    local middle = {}
    local right = {}
    
    for _, num in ipairs(nums) do
        if num < pivot then
            table.insert(left, num)
        elseif num == pivot then
            table.insert(middle, num)
        else
            table.insert(right, num)
        end
    end
    
    return merge_tables(quicksort(left), middle, quicksort(right))
end

function merge_tables(...)
    local result = {}
    local tables = {...}
    
    for _, tbl in ipairs(tables) do
        for _, value in ipairs(tbl) do
            table.insert(result, value)
        end
    end
    
    return result
end

-- 测试函数
function test_quicksort()
    math.randomseed(os.time())
    
    local test_cases = {
        {3, 1, 4, 1, 5, 9, 2, 6},
        {64, 34, 25, 12, 22, 11, 90},
        {5, 2, 3, 1},
        {1},
        {}
    }
    
    print("Lua 快速排序测试")
    print("================")
    
    for i, test in ipairs(test_cases) do
        local result = quicksort(test)
        local expected = {}
        for i, v in ipairs(test) do expected[i] = v end
        table.sort(expected)
        
        local correct = true
        if #result ~= #expected then
            correct = false
        else
            for i = 1, #result do
                if result[i] ~= expected[i] then
                    correct = false
                    break
                end
            end
        end
        
        print("测试 " .. i .. ": " .. table.concat(test, ", "))
        print("结果: " .. table.concat(result, ", "))
        print("期望: " .. table.concat(expected, ", "))
        print("正确: " .. (correct and "✅" or "❌"))
        print()
    end
end

-- 性能测试
function performance_test()
    local sizes = {100, 1000, 5000}
    
    print("Lua 快速排序性能测试")
    print("====================")
    
    for _, size in ipairs(sizes) do
        local test_data = {}
        for i = 1, size do
            table.insert(test_data, math.random(1, 10000))
        end
        
        -- 测试快速排序
        local start_time = os.clock()
        local quick_result = quicksort(test_data)
        local quick_time = os.clock() - start_time
        
        -- 测试table.sort
        local test_copy = {}
        for i, v in ipairs(test_data) do test_copy[i] = v end
        start_time = os.clock()
        table.sort(test_copy)
        local table_sort_time = os.clock() - start_time
        
        -- 验证正确性
        local correct = true
        for i = 1, #quick_result do
            if quick_result[i] ~= test_copy[i] then
                correct = false
                break
            end
        end
        
        print("数据量: " .. size)
        print("快速排序: " .. string.format("%.6f", quick_time) .. "s")
        print("table.sort: " .. string.format("%.6f", table_sort_time) .. "s")
        print("正确: " .. (correct and "✅" or "❌"))
        print("相对table.sort慢: " .. string.format("%.2f", quick_time/table_sort_time) .. "x")
        print()
    end
end

-- 运行测试
test_quicksort()
performance_test()
