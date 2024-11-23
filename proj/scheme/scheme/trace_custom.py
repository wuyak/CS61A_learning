
import sys
import trace

# 指定要追踪的文件
TRACKED_FILES = ["scheme_classes.py", "scheme_eval_apply.py", "scheme_forms.py"]

# 自定义追踪过滤器
def custom_trace_filter(filename):
    return any(tracked_file in filename for tracked_file in TRACKED_FILES)

# 配置 Trace
class CustomTrace(trace.Trace):
    def globaltrace_lt(self, frame, event, arg):
        if event != "call":
            return None
        code = frame.f_code
        func_filename = code.co_filename
        if custom_trace_filter(func_filename):
            return self.localtrace
        return None

tracer = CustomTrace(trace=True, count=False)

# 运行目标脚本
if len(sys.argv) < 2:
    print("Usage: python3 trace_custom.py <script_path> [script_args...]")
    sys.exit(1)

script_path = sys.argv[1]
script_args = sys.argv[2:]
sys.argv = [script_path] + script_args

print(f"Tracing: {script_path} with arguments: {script_args}")
with open(script_path) as script_file:
    code = script_file.read()
    tracer.run(code)
