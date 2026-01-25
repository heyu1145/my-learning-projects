import numpy as np
from scipy.integrate import quad
import math

def exact_constrained_area():
    """精确计算约束区域内的重叠面积"""
    
    def integrand(x):
        # 检查x是否在约束范围内
        if x < -2 or x > 2:
            return 0
            
        # 圆1在约束范围内的y范围
        rad1 = 16 - (x + 2)**2
        if rad1 < 0:
            y1_low, y1_high = -2, -2  # 无交点
        else:
            sqrt_rad1 = math.sqrt(rad1)
            y1_low = max(-2, 2 - sqrt_rad1)   # 约束 y ≥ -2
            y1_high = min(2, 2 + sqrt_rad1)   # 约束 y ≤ 2
        
        # 圆2在约束范围内的y范围  
        rad2 = 4 - x**2
        if rad2 < 0:
            y2_low, y2_high = -2, -2  # 无交点
        else:
            sqrt_rad2 = math.sqrt(rad2)
            y2_low = max(-2, -2 - sqrt_rad2)  # 约束 y ≥ -2
            y2_high = min(2, -2 + sqrt_rad2)  # 约束 y ≤ 2
        
        # 计算重叠高度
        overlap_low = max(y1_low, y2_low)
        overlap_high = min(y1_high, y2_high)
        
        height = max(0, overlap_high - overlap_low)
        return height
    
    # 积分计算面积
    area, error = quad(integrand, -2, 2)
    return area, error

# 计算面积
area, error_estimate = exact_constrained_area()
print(f"精确的约束区域内重叠面积: {area:.8f}")
print(f"积分误差估计: {error_estimate:.2e}")
