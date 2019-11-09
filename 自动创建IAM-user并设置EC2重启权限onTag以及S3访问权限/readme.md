# 自动创建 IAM User，并设置 EC2 和 S3 权限  

本 Demo 是自动创建一个 IAM User，并根据这个 user 名字来为创建的 EC2 打 Tag 标签"Owner=user名"，并创建一个对应的 S3 Bucket。    
这个 IAM User 只能对这个 Tag 对应的 EC2 做:  
StartInstances, StopInstances, RebootInstances  
只能访问这个 S3 Bucket 做  
ListBucket, GetObject, PutObject  
没有其他权限。

## 新建一个 IAM Policy 
名称为 ec2-start-stop-on-tags-s3-access，文件见附件的 JSON  
记录 ARN，下面步骤用

## 修改 Python 文件
* 设置 s3 bucket prefix  
* 设置 region
* 替换上面新建的那个 IAM Policy ARN

## 运行 Python 文件
python3 auto-create-user-ec2-s3-with-tag.py  
  
* 请按照提示输入要新建的 IAM User 名称（英文），如果是已经存在的 IAM User ，系统会提示已经存在并继续执行下面步骤。如果不存在，则会新建一个 IAM User，并授权。
* 请打开 AWS 控制台创建 EC2 ，记录下 instance id 
* 请回到 Python 运行的界面，根据提示输入 instance id，如果有多个，则每次输入一个，并回车。最后空回车则结束输入。  
=== 以下是自动执行的
* 自动完成对以上 EC2 打标签的工作，Key 为 Owner，Value 为 iam_user
* 自动新建一个 S3 Bucket，如果已经存在提示并则跳过


