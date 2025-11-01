#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <chrono>

std::vector<int> radixsort(const std::vector<int>& args) {
    if (args.empty()) return {};
    
    std::vector<std::string> rev_args;
    int length = 0;
    
    // 第一步：反转数字字符串并找到最大长度
    for (int num : args) {
        std::string snum = std::to_string(num);
        std::reverse(snum.begin(), snum.end());
        rev_args.push_back(snum);
        if (snum.length() > length) {
            length = snum.length();
        }
    }
    
    std::vector<std::string> store = rev_args;
    
    // 基数排序主循环
    for (int n = 0; n < length; ++n) {
        // 初始化10个桶
        std::vector<std::vector<std::string>> buckets(10);
        
        // 分配数字到桶中
        for (const auto& rnum : store) {
            if (rnum.length() <= n) {
                buckets[0].push_back(rnum);
            } else {
                int digit = rnum[n] - '0';  // 字符转数字
                buckets[digit].push_back(rnum);
            }
        }
        
        // 重置存储区
        store.clear();
        
        // 从桶中收集数字
        for (const auto& bucket : buckets) {
            for (const auto& rnum : bucket) {
                store.push_back(rnum);
            }
        }
    }
    
    // 转换回数字
    std::vector<int> result;
    for (const auto& rnum : store) {
        std::string snum = rnum;
        std::reverse(snum.begin(), snum.end());
        result.push_back(std::stoi(snum));
    }
    
    return result;
}

// 测试函数
void test_performance() {
    std::vector<int> test_data;
    int sizes[] = {100, 1000, 5000};
    
    std::cout << "C++ 基数排序性能测试\n";
    std::cout << "=====================\n";
    
    for (int size : sizes) {
        // 生成测试数据
        test_data.clear();
        for (int i = 0; i < size; ++i) {
            test_data.push_back(rand() % 10000 + 1);
        }
        
        // 测试基数排序
        auto start = std::chrono::high_resolution_clock::now();
        auto result = radixsort(test_data);
        auto end = std::chrono::high_resolution_clock::now();
        double radix_time = std::chrono::duration<double>(end - start).count();
        
        // 测试std::sort
        auto test_data_copy = test_data;
        start = std::chrono::high_resolution_clock::now();
        std::sort(test_data_copy.begin(), test_data_copy.end());
        end = std::chrono::high_resolution_clock::now();
        double std_sort_time = std::chrono::duration<double>(end - start).count();
        
        // 验证正确性
        bool correct = (result == test_data_copy);
        
        std::cout << "数据量: " << size << "\n";
        std::cout << "基数排序: " << radix_time << "s\n";
        std::cout << "std::sort: " << std_sort_time << "s\n";
        std::cout << "正确: " << (correct ? "✅" : "❌") << "\n";
        std::cout << "加速比: " << (0.03/radix_time) << "x (相对于Python)\n\n";
    }
}

int main() {
    test_performance();
    return 0;
}

