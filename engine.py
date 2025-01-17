
import glob
import os
import argparse
def data():
 parser = argparse.ArgumentParser(description="A script that demonstrates help functionality.")
 parser.add_argument("--type", type=str, help="Specify your name.",default="txt")
 parser.add_argument("--place", type=str, help="Specify your age.",default=".")
 args = parser.parse_args()
 place=args.place
 type=args.type
 if place==".":
    place=os.getcwd()
 result=[]
 return type,place,result

def checkFolders(directory):
 folders = [item for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item))] 
 if len(folders)>0:
  for i in folders:
    newDir=f"{directory}/{i}"
    getFiles(newDir,data()[0],data()[2])
    folders = [item for item in os.listdir(newDir) if os.path.isdir(os.path.join(newDir, item))] 
  return checkFolders(newDir)
 else:
  return
 
def getFiles(place,type,result):
  path = f'{place}/*.{type}'
  files = glob.glob(path)
  for i in files:
   result.append(i)
  print(result)

getFiles(data()[1],data()[0],data()[2]) 
checkFolders(data()[1])
