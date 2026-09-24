#!/usr/bin/env python3

import sys

print(f"parameters: {len(sys.argv) - 1}")

if len(sys.argv) == 1:
    print("none")
else:
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")
