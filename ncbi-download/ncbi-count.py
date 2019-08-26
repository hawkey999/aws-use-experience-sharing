import os

def count(filedir): # count a project, such as assembly_summary_bacteria
    filelist = os.listdir(filedir) # list all file name in this folder
    recordList = [] 
    emptyDir = 0 
    for f in filelist:
        if f[:3] == 'GCF': # if file name start with GCF then take it as a valid record
            recordName = f[:15] # cut out the record name
            if recordName not in recordList: # check the name is in list or not
                recordList.append(recordName) # add all valide file name into this list
                # Check if this is a empty folder, will make this tool run slow
                # try:
                #     checkDir = os.listdir('./'+filedir+'/'+f) 
                #     if len(checkDir) == 0:  # check this record's sub-folder is empty or not
                #         emptyDir+=1
                # except Exception as e:
                #     pass
    print(filedir, ' count: ', len(recordList), 'Empty Folder: ', emptyDir)
    return len(recordList)


dirlist = os.listdir('./') # list all file name in current dir
total = 0
for d in dirlist:
    dCharList = d.split('.') 
    if len(dCharList) == 1 : # if the file name not include '.' then it is a folder
        total+=count(d) # count all file in this folder
print('Total: ', total)
