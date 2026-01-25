import math

r1 = 4
r2 = 2
d = math.sqrt(20)  # 2√5 ≈ 4.472

# 计算角度
theta1 = math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
theta2 = math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))

# 计算面积
area = (r1**2 * theta1 + r2**2 * theta2 - 
        0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2)))

print(f"两个圆的完整重叠面积: {area:.6f}")
