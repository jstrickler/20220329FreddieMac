#!/usr/bin/env python

from zipfile import ZipFile, ZIP_DEFLATED
import os.path

# reading & extracting from zip file
zip_in = ZipFile("../DATA/textfiles.zip")  # <1>
print(zip_in.namelist())  # <2>
tyger_text = zip_in.read('tyger.txt').decode()  # <3>
print(tyger_text[:100], '\n')
zip_in.extract('parrot.txt')  # <4>

# creating a zip file
file_names = ["parrot.txt", "tyger.txt", "knights.txt", "alice.txt", "poe_sonnet.txt", "spam.txt"]
zip_out = ZipFile("example.zip", mode="w", compression=ZIP_DEFLATED)  # <5>
for file_name in file_names:
    file_path = os.path.join("../DATA", file_name)
    print("adding {}".format(file_path))
    zip_out.write(file_path, file_name)  # <6>
