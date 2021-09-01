import re
import shutil
import zipfile


def method1():
    n = int(input("HOW MANY FILES DO YOU HAVE : "))

    zip_name = input("ENTER NAME OF ZIPPED FILE : ")
    zip_name += ".zip"

    comp_file = zipfile.ZipFile(zip_name, 'w')

    for i in range(n):
        file_loc = input(f"FILE PATH OF {(i + 1)} FILE : ")
        comp_file.write(file_loc, compress_type=zipfile.ZIP_DEFLATED)

    comp_file.close()

    zip_loc = input("ENTER LOCATION WHERE YOU WANT YOUR FILE: ")

    shutil.move(zip_name,zip_loc)
    print()
    print()
    print("TASK DONE. \nTHANK YOU.")


def method2():
    file_loc = input("FILE PATH : ")
    zip_loc = input("ENTER LOCATION WHERE YOU WANT YOUR FILE: ")
    zip_name = input("ENTER NAME OF ZIPPED FILE : ")

    shutil.make_archive(zip_name,'zip',file_loc)
    zip_name += ".zip"
    shutil.move(zip_name, zip_loc)
    print()
    print()
    print("TASK DONE. \nTHANK YOU.")


def method3():
    file_loc = input("FILE PATH OF ZIPPED-FILE: ")
    zip_loc = input("ENTER LOCATION WHERE YOU WANT YOUR FILE: ")
    zip_name = input("ENTER NAME OF UN-ZIPPED FILE : ")

    shutil.unpack_archive(file_loc,zip_name,'zip')
    zip_name += ".zip"
    shutil.move(zip_name, zip_loc)

    print()
    print()
    print("TASK DONE. \nTHANK YOU.")


n = int(
    input(" WHAT IS YOUR TASK TODAY ? : \n1.ZIP INDIVIDUAL FILES \n2.ZIP FOLDER \n3.EXTRACT FILES FROM A ZIPPED FILE  "))
print()
print()

if n == 2:
    method2()

elif n == 1:
    method1()

elif n == 3:
    method3()
