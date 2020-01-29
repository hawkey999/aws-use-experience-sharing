# 使用 Session Manager 代替 SSH 访问 EC2，替代 Bastion 堡垒机
* 方便登录：不使用 EC2 Key 密钥，不需要通过堡垒机的情况下 SSH 连接到您的 EC2 实例，无论实例是在公有还是私有子网中。即实例不能访问公网也可以通过 VPC endpoint ssmmessage 来实现 SSH 登录。无需 SSH 客户端。
* 全程审计：在 Amazon S3 存储桶或 CloudWatch Logs 中记录会话命令和详细信息。
* 安全加密：使用 AWS Key Management Service 密钥保护会话。

# 前置准备
* 本机安装 aws cli 
https://aws.amazon.com/cli/
* 本机安装 session-manager-plugin 
https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html
* EC2 实例上有 SSM Agent，Amazon Linux 自带有，其他OS安装见
https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html
* EC2 实例需配置一个 Role (角色)，该 Role 包括的托管策略为：
AmazonSSMManagedInstanceCore
注意：虽然 Amazon Linux 自带了 Agent，但不配置对应的角色，则该 Agent 是不能工作的。  
* 网络连接有两种选择：
1. 推荐采用 VPC Endpoint，不需要经过公网。即在 VPC 的私有子网中建以下几个 endpoint。并且安全组是允许 VPC 中地址访问 endpoint 的 443 端口。
 - com.amazonaws.region.ssm
 - com.amazonaws.region.ec2messages
 - com.amazonaws.region.ssmmessages
2. 如果 EC2 本身是可以对外访问公网的，例如服务器在私有子网，但有路由经过 NAT Gateway 访问公网，则同样可以通过 Session Manager 访问。

# 使用
* 本机终端输入命令即可登录到服务器。替换下面的 ec2 id:
```bash
aws ssm start-session --target "YOUR_EC2_ID"
```
# 权限
* 限制用户 IAM 权限只能通过 Session Manager 访问该 EC2 ，访问不了其他服务器，或其他服务。参考这个角色配置：  
user_iam_role.json

# 文档
https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started.html
