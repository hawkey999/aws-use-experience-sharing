import json, hashlib, re, datetime

logfile = './dataset-access.log' # source file
bulkfile = './dataset.bulk' # destination file
ip = r"?P<ip>[\d.]*"
date = r"?P<date>\d+"
month = r"?P<month>\w+"
year = r"?P<year>\d+"
log_time = r"?P<time>\S+"
method = r"?P<method>\S+"
request = r"?P<request>\S+"
status = r"?P<status>\d+"
bodyBytesSent = r"?P<bodyBytesSent>\d+"
refer = r"""?P<refer>
            [^\"]*
            """
userAgent = r"""?P<userAgent>
            [^\"]*
            """
p = re.compile(r"(%s)\ -\ -\ \[(%s)/(%s)/(%s)\:(%s)\ [\S]+\]\ \"(%s)?[\s]?(%s)?.*?\"\ (%s)\ (%s)\ \"(%s)\"\ \"(%s).*?\"" %
               (ip, date, month, year, log_time, method, request, status, bodyBytesSent, refer, userAgent), re.VERBOSE)

def parsetime(date, month, year, log_time):
    time_str = '%s%s%s%s' %(year, month, date, log_time)
    t = datetime.datetime.strptime(time_str, '%Y%b%d%H:%M:%S')
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")

with open(logfile, 'r') as f:
    with open(bulkfile, 'w') as outf:
        for line in f:
            try:
                s = re.findall(p, line)
                d={}
                d['time'] = parsetime(s[0][1], s[0][2], s[0][3], s[0][4])
                d['ip'] = s[0][0]
                d['method'] = s[0][5]
                d['uri']=s[0][6]
                d['code']=s[0][7]
                d['size']=s[0][8]
                d['refer']=s[0][9]
                d['agent']=s[0][10]
                doc_id = hashlib.sha224(json.dumps(
                    d).encode('ascii', 'ignore')).hexdigest()
                data_index = {
                    "index":{
                        "_index":"access_log",
                        "_type":"log",
                        "_id":doc_id
                    }
                }
                print('.',end='')
                #print(json.dumps(d), ' ', json.dumps(data_index))
                outf.writelines(json.dumps(data_index)+'\n')
                outf.writelines(json.dumps(d)+'\n')
            except Exception as e:
                print(e)

