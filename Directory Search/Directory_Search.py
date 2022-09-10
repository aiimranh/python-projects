import os

rootdir = "F:\DownloadX\GitHub\python-projects"


# os.walk() return three-element-tuple ('relative-path', [directories], [files]) for every folder

# for tup in os.walk(rootdir):
# 	print(tup)


 
pdfiles = []

for relpath,dirs,files in os.walk(rootdir):
	for file in files:
		if file.endswith(".pdf") or file.endswith(".PDF"):
			pdfiles.append(file)
			
print(pdfiles)			