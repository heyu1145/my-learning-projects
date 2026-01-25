import math
from typing import List, Tuple

class EquationSolver:
    def __init__(self):
        self.coefficients = []
        self.search_range = (-100, 100)
        self.precision = 6
    
    def f(self, x: float) -> float:
        """计算多项式在x处的值"""
        return sum(coef * (x ** i) for i, coef in enumerate(reversed(self.coefficients)))
    
    def bisection_solve(self, left: float, right: float, precision: float = 1e-10) -> float:
        """二分法在区间内求解"""
        f_left = self.f(left)
        f_right = self.f(right)
        
        # 检查端点是否正好是根
        if abs(f_left) < precision:
            return left
        if abs(f_right) < precision:
            return right
        
        if f_left * f_right > 0:
            return None
        
        for _ in range(1000):
            mid = (left + right) / 2
            f_mid = self.f(mid)
            
            if abs(f_mid) < precision:
                return mid
            
            if f_left * f_mid < 0:
                right = mid
                f_right = f_mid
            else:
                left = mid
                f_left = f_mid
        
        return (left + right) / 2
    
    def find_roots(self) -> List[float]:
        """查找所有实数根"""
        left, right = self.search_range
        num_intervals = 2000
        interval_width = (right - left) / num_intervals
        roots = []
        
        # 先检查所有区间端点
        for i in range(num_intervals + 1):
            x = left + i * interval_width
            if abs(self.f(x)) < 1e-10:
                root = round(x, self.precision)
                if not roots or abs(root - roots[-1]) > 10**(-self.precision):
                    roots.append(root)
        
        # 再检查区间内部
        for i in range(num_intervals):
            a = left + i * interval_width
            b = a + interval_width
            
            # 如果端点已经是根，跳过这个区间
            if any(abs(a - root) < 1e-10 for root in roots):
                continue
            if any(abs(b - root) < 1e-10 for root in roots):
                continue
            
            f_a = self.f(a)
            f_b = self.f(b)
            
            if f_a * f_b <= 0:
                root = self.bisection_solve(a, b)
                if root is not None:
                    formatted_root = round(root, self.precision)
                    # 严格检查重复
                    is_duplicate = any(abs(formatted_root - existing_root) < 10**(-self.precision) 
                                      for existing_root in roots)
                    if not is_duplicate:
                        roots.append(formatted_root)
        
        # 排序并返回
        roots.sort()
        return roots
    
    def display_equation(self) -> str:
        """显示方程字符串 - 修复显示顺序"""
        if not self.coefficients:
            return "方程未定义"
        
        terms = []
        n = len(self.coefficients) - 1
        
        for i, coef in enumerate(self.coefficients):
            power = n - i
            if abs(coef) < 1e-10:
                continue
                
            # 处理系数显示
            if power == 0:
                term = f"{coef:g}"
            elif power == 1:
                if coef == 1:
                    term = "x"
                elif coef == -1:
                    term = "-x"
                else:
                    term = f"{coef:g}x"
            else:
                if coef == 1:
                    term = f"x^{power}"
                elif coef == -1:
                    term = f"-x^{power}"
                else:
                    term = f"{coef:g}x^{power}"
            
            terms.append(term)
        
        # 构建方程字符串
        if not terms:
            return "0 = 0"
            
        equation = terms[0]
        for term in terms[1:]:
            if term.startswith('-'):
                equation += " - " + term[1:]
            else:
                equation += " + " + term
        
        return equation + " = 0"
    
    def input_coefficients_natural(self):
        """自然顺序输入系数（从常数项开始）"""
        self.coefficients = []
        print("请输入方程系数（推荐从常数项开始）:")
        print("示例: 方程 2x² + 3x + 1 = 0")
        print("      常数项: 1")
        print("      x系数: 3") 
        print("      x²系数: 2")
        print("")
        
        coefficients_dict = {}
        max_power = -1
        
        while True:
            try:
                power_input = input("输入项的次数 (空行结束，如 0=常数项, 1=x, 2=x²): ").strip()
                if power_input == '':
                    break
                    
                power = int(power_input)
                if power < 0:
                    print("次数不能为负数")
                    continue
                    
                coef_input = input(f"x^{power} 的系数: ").strip()
                coef = float(coef_input)
                
                coefficients_dict[power] = coef
                max_power = max(max_power, power)
                print(f"✅ 已设置: {coef} * x^{power}")
                
            except ValueError:
                print("请输入有效的数字！")
            except KeyboardInterrupt:
                print("\n输入中断")
                return
        
        # 构建系数列表（从高次到低次）
        if coefficients_dict:
            self.coefficients = [coefficients_dict.get(i, 0) for i in range(max_power, -1, -1)]
            print(f"✅ 方程已设置: {self.display_equation()}")
        else:
            print("❌ 未输入任何系数")

    def set_search_range(self):
        """设置搜索范围"""
        print(f"\n当前搜索范围: [{self.search_range[0]}, {self.search_range[1]}]")
        print("设置新的搜索范围:")
        
        while True:
            try:
                left_input = input("左边界 (默认-100): ").strip()
                right_input = input("右边界 (默认100): ").strip()
                
                left = float(left_input) if left_input else -100
                right = float(right_input) if right_input else 100
                
                if left >= right:
                    print("左边界必须小于右边界！")
                    continue
                    
                self.search_range = (left, right)
                print(f"✅ 搜索范围已设置为: [{left}, {right}]")
                break
                
            except ValueError:
                print("请输入有效的数字！")
    
    def set_precision(self):
        """设置精度"""
        print(f"\n当前精度: {self.precision} 位小数")
        
        while True:
            try:
                precision_input = input("设置小数位数 (0-15, 默认6): ").strip()
                precision = int(precision_input) if precision_input else 6
                
                if 0 <= precision <= 15:
                    self.precision = precision
                    print(f"✅ 精度已设置为: {precision} 位小数")
                    break
                else:
                    print("请输入0-15之间的整数")
                    
            except ValueError:
                print("请输入有效的整数！")
    
    def show_status(self):
        """显示当前状态"""
        print(f"\n{'当前状态':-^40}")
        print(f"方程: {self.display_equation()}")
        print(f"搜索范围: [{self.search_range[0]}, {self.search_range[1]}]")
        print(f"精度: {self.precision} 位小数")
        print(f"系数: {self.coefficients}")
        print('-' * 40)

def main():
    solver = EquationSolver()
    
    print(f"{'🎯 高级方程求解平台':=^50}")
    print("支持一元任意次方程求解")
    print("=" * 50)
    
    while True:
        print("\n命令列表:")
        print("  [c] 输入系数    [s] 显示状态")
        print("  [r] 设置范围    [p] 设置精度") 
        print("  [solve] 求解    [clear] 清空")
        print("  [quit] 退出")
        
        try:
            command = input("\n请输入命令: ").strip().lower()
            
            if command in ['quit', 'exit', 'q']:
                print("再见！👋")
                break
                
            elif command in ['c', 'coefficient']:
                solver.input_coefficients_natural()
                
            elif command in ['s', 'status']:
                solver.show_status()
                
            elif command in ['r', 'range']:
                solver.set_search_range()
                
            elif command in ['p', 'precision']:
                solver.set_precision()
                
            elif command == 'solve':
                if len(solver.coefficients) < 2:
                    print("❌ 请先输入系数！")
                    continue
                    
                solver.show_status()
                print("\n正在求解...")
                
                roots = solver.find_roots()
                
                if roots:
                    print(f"\n🎉 找到 {len(roots)} 个实数根:")
                    for i, root in enumerate(roots, 1):
                        error = abs(solver.f(root))
                        print(f"  根 {i}: x = {root}")
                        if error > 1e-8:
                            print(f"     ⚠️  警告: 计算误差较大 ({error:.2e})")
                else:
                    print("\n❌ 在指定范围内未找到实数根")
                    print("💡 建议：尝试扩大搜索范围或检查方程")
                
            elif command == 'clear':
                solver.coefficients = []
                solver.search_range = (-100, 100)
                solver.precision = 6
                print("✅ 已重置所有设置")
                
            else:
                print("❌ 未知命令")
                
        except KeyboardInterrupt:
            print("\n\n再见！👋")
            break
        except Exception as e:
            print(f"❌ 发生错误: {e}")

if __name__ == "__main__":
    main()
