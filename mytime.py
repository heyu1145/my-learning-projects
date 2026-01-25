import functools
from datetime import datetime

def timer(func=None, *, unit='auto'):
    if func is None:
        return functools.partial(timer, unit=unit)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now().timestamp()
        result = func(*args, **kwargs)
        end = datetime.now().timestamp()
        
        elapsed = end - start
        
        # 自动选择合适的时间单位
        if unit == 'auto':
            if elapsed < 0.001:  # < 1ms
                display_time = elapsed * 1_000_000
                unit_str = 'μs'
            elif elapsed < 1:    # < 1s
                display_time = elapsed * 1000
                unit_str = 'ms'
            else:                # >= 1s
                display_time = elapsed
                unit_str = 's'
        else:
            # 手动指定单位
            conversions = {
                'ns': (1_000_000_000, 'ns'),
                'us': (1_000_000, 'μs'),
                'ms': (1000, 'ms'),
                's': (1, 's')
            }
            multiplier, unit_str = conversions.get(unit, (1000, 'ms'))
            display_time = elapsed * multiplier
        
        print(f"Run time: {display_time:.4f} {unit_str}")
        return result
    
    return wrapper
