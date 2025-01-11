result=[]
import glob,os
type=input("file type  : ")
place=input("file place : ")
if place==".":
    place=os.getcwd()
path=""

def checkFolders(o):
 directory = o
 folders = [item for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item))] 

 if len(folders)>0:
  # print(folders,"foldreto")
  for i in folders:
    newDir=f"{directory}/{i}"
    getFiles(newDir)
    folders = [item for item in os.listdir(newDir) if os.path.isdir(os.path.join(newDir, item))] 
    # print(folders)
    # print(newDir)
    
  return checkFolders(newDir)
 else:
  print("nothing")
  return "nothing"
 

def getFiles(place):
  
  path = f'{place}/*.{type}'
  files = glob.glob(path)
  for i in files:
   result.append(i)
  # print(result)


getFiles(place) 
checkFolders(place)

print(result,"reso")