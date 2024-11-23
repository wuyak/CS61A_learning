
import sys

# 需要追踪的文件
TRACKED_FILES = ["scheme_classes.py", "scheme_eval_apply.py", "scheme_forms.py"]

# 已追踪的函数
called_functions = set()  # 用于记录已显示的函数调用

def trace_calls(frame, event, arg):
    if event != "call":  # 只处理函数调用事件
        return
    code = frame.f_code
    func_name = code.co_name
    func_filename = code.co_filename

    # 判断函数是否定义在目标文件中
    if any(tracked_file in func_filename for tracked_file in TRACKED_FILES):
        # 如果函数已经显示过，则跳过
        if func_name in called_functions:
            return None
        # 记录并显示该函数调用
        called_functions.add(func_name)
        print(f"Function called: {func_name} in {func_filename}")
        return trace_calls  # 继续追踪
    return None  # 忽略非目标文件中的函数

# 启用跟踪
sys.settrace(trace_calls)

# 执行目标脚本
if len(sys.argv) < 2:
    print("Usage: python3 trace_custom.py <script_path> [script_args...]")
    sys.exit(1)

script_path = sys.argv[1]
script_args = sys.argv[2:]
sys.argv = [script_path] + script_args

print(f"Tracing: {script_path} with arguments: {script_args}")

# 运行目标脚本
with open(script_path) as script_file:
    code = script_file.read()
    exec(code)
