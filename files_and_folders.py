import os
from datetime import datetime

folder = "DATA"
file_name = "alice.txt"

file_path = os.path.join(folder, file_name)
print("file_path: {}".format(file_path))

print("os.path.dirname(file_path): {}".format(os.path.dirname(file_path)))
print("os.path.basename(file_path): {}".format(os.path.basename(file_path)))
print("os.path.splitext(file_path): {}".format(os.path.splitext(file_path)))
print("os.path.split(file_path): {}".format(os.path.split(file_path)))

print("os.path.abspath(file_path): {}".format(os.path.abspath(file_path)))
file_size = os.path.getsize(file_path)
print("file_size: {}".format(file_size))

raw_timestamp = os.path.getmtime(file_path)
print("raw_timestamp: {}".format(raw_timestamp))
timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp: {}".format(timestamp))
for obj in folder, file_name, file_path:
    print(obj)
    print("  os.path.isfile(obj): {}".format(os.path.isfile(obj)))
    print("  os.path.isdir(obj): {}".format(os.path.isdir(obj)))
print("os.path.exists('DATA/funwithwombats.txt'): {}".format(os.path.exists('DATA/funwithwombats.txt')))
print("os.path.exists({}): {}".format(file_path, os.path.exists(file_path)))








