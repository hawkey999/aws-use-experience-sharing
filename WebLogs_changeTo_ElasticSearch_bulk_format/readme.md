# Apache Logs file to ElasticSearch Bulk Format  
  
* 转换文件格式  
运行 weblog-to-Elasticsearch Python 代码，将通用格式的 Apache Weblog 日志文件批量转换为 ElasticSearch Bulk 上传的格式
```
python3 weblog-to-Elasticsearch.py
```
  
常见的 Web log 格式示例：  
```
101.111.111.111 - - [12/Dec/2015:18:25:11 +0100] "GET /ad/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
```
测试时，可以使用这个公开的数据集：https://s3.cn-north-1.amazonaws.com.cn/emrdata-huangzb/dataset-access/dataset-access.log

转换为 ES 批量导入的格式是：
```
{"index": {"_index": "access_log", "_type": "log", "_id": "666315ec5d691638ecc641f22bdec8c63dea5ff5704bc8624d50893b"}}
{"time": "2015-12-12T18:25:11Z", "ip": "101.111.111.111", "method": "GET", "uri": "/ad/", "code": "200", "size": "4263", "refer": "-", "agent": "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0"}
```

* 单个文件上传  
```
curl -XPOST https://es_endpoint/_bulk --data-binary @dataset.bulk -H 'Content-Type: application/json'
```
* 文件分拆  
对于稍大的数据文件，例如大于10MB，直接上传是会失败的。即使设置了 Truncated ，因为上传由网络层协议自动切分，会导致把 JSON 从中间截断，这样ES收到这个截断的数据就会识别失败。  
在实际生产环境中，原始的数据文件一般都比较大，需要分拆为小文件。以下 Python 示例是每1万条记录分拆为一个文件，文件名为原文件名+数字编号。  
修改以下脚本中 file_size 为每个文件包含的记录数值，注意每个记录是包含了两行的，包括了 Index 行和数据行。
```
sourcefile = './dataset.bulk'  # source file
file_size = 10000*2 # 修改file_size为每个文件包含的记录数值，注意每个记录是包含了两行
count = 0
filename = 0
data_str = ''
with open(sourcefile, 'r') as f:
    for line in f:
        count += 1
        data_str += line
        if count == file_size:
            with open(sourcefile+str(filename), 'w') as outp:
                outp.write(data_str)
            data_str = ''
            count = 0
            filename += 1
    if data_str != '':
        with open(sourcefile+str(filename), 'w') as outp:
            outp.write(data_str)

```

* 批量上传
以上分拆之后的多个数据文件，可以使用以下Shell脚本上传到ES集群。修改i的循环数值100，改为上面分拆之后最大的文件数即可
```
for((i=0;i<=100;i++));
do echo $i;
curl -XPOST https://es_endpoint/_bulk --data-binary @dataset.bulk$i -H 'Content-Type: application/json'
done
```