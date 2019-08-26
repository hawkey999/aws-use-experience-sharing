import os, time
from concurrent import futures
MaxThread = 10 # const of Max download thread

def downloadThread(command, id): # a download thread
    try:
        print('ThreadID=',id)
        os.system(command) # run the ascp download in this thread
        #time.sleep(10)
    except Exception as e:
        print(e)
    return


def download(filename): 
    with open(filename, 'r') as file: # open a txt index file to download all ftp links
        with futures.ThreadPoolExecutor(max_workers=MaxThread) as pool:
            ThreadID = 0
            for line in file: 
                try:
                    if line.strip('\n').split(' ')[0] != '#': # skip the '#' record
                        ftpsite = line.strip('\n').split('\t')[19] # split the record with \t and cut out the ftp link
                        ftplink = ftpsite[27:] # cut out the ftp link without site name
                        command = 'ascp -i /home/ec2-user/.aspera/connect/etc/asperaweb_id_dsa.openssh -T -k1 -l500M anonftp@ftp.ncbi.nlm.nih.gov:' + \
                            ftplink+' ./'+filename[:-4]+'/'
                        # download one link with submiting one Python thread
                        pool.submit(downloadThread, command, ThreadID)
                        ThreadID +=1
                        if ThreadID == MaxThread:
                            ThreadID = 0
                except Exception as e:
                    print(e)
    return

filelist = os.listdir('./') # list all txt index file in current folder
for filename in filelist:
    if filename[-3:] == 'txt': # if it is txt file, start to download
        print('downloading', filename)
        download(filename)
