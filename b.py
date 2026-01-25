import numpy as np
import math

def monte_carlo_area():
    """用蒙特卡洛方法计算约束区域内的重叠面积"""
    
    # 正方形区域: [-2,2]×[-2,2]，面积 = 4×4 = 16
    n_points = 1000000
    points_x = np.random.uniform(-2, 2, n_points)
    points_y = np.random.uniform(-2, 2, n_points)
    
    # 检查点是否在两个圆内
    in_circle1 = (points_x + 2)**2 + (points_y - 2)**2 <= 16
    in_circle2 = points_x**2 + (points_y + 2)**2 <= 4
    
    # 在两个圆内的点
    in_both = in_circle1 & in_circle2
    
    # 计算面积比例
    area_ratio = np.sum(in_both) / n_points
    area = area_ratio * 16  # 正方形面积
    
    return area

# 完整圆重叠面积（已验证）
full_overlap = 3.846957

# 约束区域内的重叠面积
constrained_area = monte_carlo_area()
print(f"完整圆重叠面积: {full_overlap:.6f}")
print(f"约束区域内重叠面积: {constrained_area:.6f}")
