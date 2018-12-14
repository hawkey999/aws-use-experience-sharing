# 设置跨帐号的 AWS S3 上传文件

要让所有AWS IAM User上传文件到S3进行收集，如果这些User都是不同的AWS Account下面的，怎么处理呢？  
基本原理是收集者在自己的AWS S3 Bucket设置策略，允许其他用户跨帐号上传文件，但有些地方要注意的

## 如何设置S3 Bucket的策略

* 收集方的Bucket Policy 要设置允许XXX账户的YYY用户至少有Put Object权限。需要的话，还可以允许List Bucket和Get Object权限

            {  
                "Version": "2012-10-17",  
                "Id": "Policy1544588154662",  
                "Statement": [  
                    {  
                        "Sid": "Stmt11111111a",  
                        "Effect": "Allow",  
                        "Principal": {  
                            "AWS": ["arn:aws-cn:iam::<accountNumber>:user/<username>"]  
                        },  
                        "Action": [  
                            "s3:AbortMultipartUpload",  
                            "s3:GetObject",  
                            "s3:ListMultipartUploadParts",  
                            "s3:PutObject",  
                            "s3:ReplicateObject"  
                        ],  
                        "Resource": "arn:aws-cn:s3:::<bucketname>/*"  
                    },  
                    {  
                        "Sid": "Stmt11111111b",  
                        "Effect": "Allow",  
                        "Principal": {  
                            "AWS": ["arn:aws-cn:iam::<accountNumber>:user/<username>"]  
                        },  
                        "Action": [  
                            "s3:GetBucketLocation",  
                            "s3:ListBucket",  
                            "s3:ListBucketMultipartUploads"  
                        ],  
                        "Resource": "arn:aws-cn:s3:::<bucketname>"  
                    }  
                ]  
            }  


* 上传方的IAM User Policy 要设置允许上传

        {  
                "Version": "2012-10-17",  
                "Statement": [  
                    {  
                        "Sid": "VisualEditor0",  
                        "Effect": "Allow",  
                        "Action": [  
                            "s3:PutObject",  
                            "s3:GetObject",  
                            "s3:ListBucket"  
                        ],  
                        "Resource": [  
                            "arn:aws-cn:s3:::<bucketname>/*",  
                            "arn:aws-cn:s3:::<bucketname>",  
                        ]  
                    }  
                ]  
            }  


存储桶策略示例
https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/dev/example-bucket-policies.html

## 文件上传了，Bucket owner是否就能读这些文件呢？

不是的！

上传文件的时候需要带上acl参数，否则跨账号上传的文件，连bucket owner都读不了的。（同一个AWS帐号下的用户上传就没这个问题）。详细参考文档：

访问控制列表 (ACL)
https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/dev/acl-overview.html#canned-acl

为什么要这样设计？
这就是AWS S3足够安全合规的体现了，试想一下，用户A将文件托管给另一个用户B，用户B负责对S3做维护、付费。但B不能读取A的文件，不能拷贝，只能删除。

## 如何上传时忘记加ACL了怎么办？

在一台跟Bucket同一Region的EC2上执行，把文件copy下来，再重新copy上去的时候带上ACL参数

    aws s3 cp s3://yyyyy/xxxxxx ./xxxxxx --recursive
    aws s3 cp ./xxxxxx s3://yyyyy/xxxxxx --recursive --acl bucket-owner-full-control

虽然更简便的方法是在S3上面直接复制覆盖

    aws s3 cp s3://yyyyy/xxxxxx s3://yyyyy/xxxxxx --recursive --acl bucket-owner-full-control

但有出现报错的情况，说metadata无变化，不能copy

参考文档：

存储桶拥有者针对不属于自己的对象授予跨账户权限
https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/dev/example-walkthroughs-managing-access-example4.html
