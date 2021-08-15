#!/usr/bin/python3

from github import Github
from datetime import datetime
import pytz
import shutil
import os
import sqlite3


def createFile():
    #Get today timestamp as IST
    IST = pytz.timezone('Asia/Kolkata')
    datetime_ist = datetime.now(IST)
    istTime = datetime_ist.strftime('%Y_%m_%d_%H_%M_%S_%Z')
    destFolder = os.path.join("..","databaseBackup")
    #Copy the file and rename it timeStamp.sqlite3
    destFileName = os.path.join(destFolder, istTime+".sqlite3")
    # Checking folder is present if not create it 
    if not os.path.exists(destFolder):
        os.makedirs(destFolder)
    shutil.copyfile("db.sqlite3", destFileName)
    # Return the path of the file 
    print("Checking of file presence")
    if os.path.exists(os.path.join(os.getcwd(),destFileName)):
        print("file is present")
        return destFileName, istTime+".sqlite3"
    


def pushToGit(filePath, fileName):
    # Read the backedup file 
    if not os.path.exists(filePath):
        print("Send email it is not working ")
        return "failed"
    # Connect to github 
    print("Entering Github repo")
    g = Github('')
    repo = g.get_repo("bha123/todolistDbBackup")
    #connect it in the repo
    print(repo.name)
    # commit the file 
    filelist= [filePath]
    commit_message = "Backup the database "+ fileName
    file = open(filePath, 'rb')
    content = file.read()
    print(filePath)
    print(fileName)      
    repo.create_file(fileName, commit_message, content,  branch="main")
    os.remove(filePath)
    return "Completed upload of DB"


def main():
    destFilepath, destFilename = createFile()
    pushToGit(destFilepath,destFilename)

if __name__=="__main__":
    main()

