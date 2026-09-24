import sys

params = sys.argv[1:]

if len(params) <= 1:
    print("none")
else:
    for param in params[::-1]:
        print(param)