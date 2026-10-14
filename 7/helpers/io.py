import sys

def logger(message, level="INFO"):
    prefix = f"[{level}]"
    print(f"{prefix} {message}", file=sys.stdout)
