import zipfile as zf
files = zf.ZipFile("file.zip", 'r')
files.extractall(path of the file to be extracted)
files.close()
