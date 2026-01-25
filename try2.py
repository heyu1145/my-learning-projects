import numpy as np

# 使用 numpy 求解所有根（包括复数）
coefficients = [16, 0, 0, 20, 300]
all_roots = np.roots(coefficients)
print("所有根（包括复数）:")
for i, root in enumerate(all_roots):
    print(f"根 {i+1}: {root}")

# 提取实数根
real_roots = [root.real for root in all_roots]
print(f"\n根: {real_roots}")
