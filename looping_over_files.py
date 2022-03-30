import sys

print(sys.argv)
for file_path in sys.argv[1:]:
    print("reading", file_path)
