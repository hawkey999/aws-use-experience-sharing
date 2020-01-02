// ==UserScript==
// @name         ShowEC2Info
// @namespace    MichaelZh
// @version      0.7
// @description  Replace instance type to vCPU and Memory Info
// @author       Michael Zhang & James Huang
// @match        https://*.console.amazonaws.cn/ec2/*
// @match        https://*.console.aws.amazon.com/ec2/*
// @grant        none
// ==/UserScript==

var objInterval;

String.prototype.myReplace = function (f, e) { //吧f替换成e
    var reg = new RegExp(f, "g"); //创建正则RegExp对象
    return this.replace(reg, e);
}

function checkTable() {
    if (window.location.href.indexOf("#Instances:sort=") == -1) return; //防止误操作其他页面
    var body = document.getElementsByTagName("body")[0];
    if (body.innerHTML.indexOf("table") == -1) return;
    if ((-1 == body.innerHTML.indexOf("启动实例") && -1 == body.innerHTML.indexOf("Launch Instance")) ||
        (-1 == body.innerHTML.indexOf("实例类型") && -1 == body.innerHTML.indexOf("Instance Type")) ||
        (-1 == body.innerHTML.indexOf("实例 ID") && -1 == body.innerHTML.indexOf("Instance ID"))) {
        return;
    }//防止误操作其他Table

    for (var tbIndex = 0; tbIndex < document.getElementsByTagName("table").length; tbIndex++) {
        var tbl = document.getElementsByTagName("table")[tbIndex];
        if (tbl.rows.length <= 1) continue;
        if (tbl.innerHTML.indexOf("vCPU") != -1) continue;  //已经添加了vCPU信息的Table，直接跳过
        for (var i = 0; i < tbl.rows.length; i++) {
            for (var j = 0; j < tbl.rows[i].cells.length; j++) {
                var s = tbl.rows[i].cells[j].innerHTML;
                s = s.myReplace("t2.micro", "t2.micro (1vCPU 1GB)");
                s = s.myReplace("t2.small", "t2.small (1vCPU 2GB)");
                s = s.myReplace("t2.medium", "t2.medium (2vCPU 4GB)");
                s = s.myReplace("t2.large", "t2.large (2vCPU 8GB)"); alert
                s = s.myReplace("t2.xlarge", "t2.xlarge (4vCPU 16GB)");
                s = s.myReplace("t2.2xlarge", "t2.2xlarge (8vCPU 32GB)");
                s = s.myReplace("t3.micro", "t3.micro (2vCPU 1GB)");
                s = s.myReplace("t3.small", "t3.small (2vCPU 2GB)");
                s = s.myReplace("t3.medium", "t3.medium (2vCPU 4GB)");
                s = s.myReplace("t3.large", "t3.large (2vCPU 8GB)"); alert
                s = s.myReplace("t3.xlarge", "t3.xlarge (4vCPU 16GB)");
                s = s.myReplace("t3.2xlarge", "t3.2xlarge (8vCPU 32GB)");
                s = s.myReplace("m4.large", "m4.large (2vCPU 8GB)");
                s = s.myReplace("m4.xlarge", "m4.xlarge (4vCPU 16GB)");
                s = s.myReplace("m4.2xlarge", "m4.2xlarge (8vCPU 32GB)");
                s = s.myReplace("m4.4xlarge", "m4.4xlarge (16vCPU 64GB)");
                s = s.myReplace("m4.10xlarge", "m4.10xlarge (40vCPU 160GB)");
                s = s.myReplace("m4.16xlarge", "m4.16xlarge (64vCPU 256GB)");
                s = s.myReplace("m5.large", "m5.large (2vCPU 8GB)");
                s = s.myReplace("m5.xlarge", "m5.xlarge (4vCPU 16GB)");
                s = s.myReplace("m5.2xlarge", "m5.2xlarge (8vCPU 32GB)");
                s = s.myReplace("m5.4xlarge", "m5.4xlarge (16vCPU 64GB)");
                s = s.myReplace("m5.10xlarge", "m5.10xlarge (40vCPU 160GB)");
                s = s.myReplace("m5.16xlarge", "m5.16xlarge (64vCPU 256GB)");
                s = s.myReplace("m5.24xlarge", "m5.24xlarge (96vCPU 384GB)");
                s = s.myReplace("c4.large", "c4.large (2vCPU 3.75GB)");
                s = s.myReplace("c4.xlarge", "c4.xlarge (4vCPU 7.5GB)");
                s = s.myReplace("c4.2xlarge", "c4.2xlarge (8vCPU 15GB)");
                s = s.myReplace("c4.4xlarge", "c4.4xlarge (16vCPU 30GB)");
                s = s.myReplace("c4.8xlarge", "c4.8xlarge (36vCPU 60GB)");
                s = s.myReplace("c5.large", "c5.large (2vCPU 4GB)");
                s = s.myReplace("c5.xlarge", "c5.xlarge (4vCPU 8GB)");
                s = s.myReplace("c5.2xlarge", "c5.2xlarge (8vCPU 16GB)");
                s = s.myReplace("c5.4xlarge", "c5.4xlarge (16vCPU 32GB)");
                s = s.myReplace("c5.9xlarge", "c5.9xlarge (36vCPU 72GB)");
                s = s.myReplace("r4.large", "r4.large (2vCPU 15.25GB)");
                s = s.myReplace("r4.xlarge", "r4.xlarge (4vCPU 30.5GB)");
                s = s.myReplace("r4.2xlarge", "r4.2xlarge (8vCPU 61GB)");
                s = s.myReplace("r4.4xlarge", "r4.4xlarge (16vCPU 122GB)");
                s = s.myReplace("r4.8xlarge", "r4.8xlarge (32vCPU 244GB)");
                s = s.myReplace("r4.16xlarge", "r4.16xlarge (64vCPU 488GB)");
                s = s.myReplace("r5.large", "r5.large (2vCPU 16GB)");
                s = s.myReplace("r5.xlarge", "r5.xlarge (4vCPU 32GB)");
                s = s.myReplace("r5.2xlarge", "r5.2xlarge (8vCPU 64GB)");
                s = s.myReplace("r5.4xlarge", "r5.4xlarge (16vCPU 128GB)");
                s = s.myReplace("r5.8xlarge", "r5.8xlarge (32vCPU 256GB)");
                s = s.myReplace("r5.12xlarge", "r5.12xlarge (48vCPU 384GB)");
                s = s.myReplace("r5.16xlarge", "r5.16xlarge (64vCPU 512GB)");
                s = s.myReplace("r5.24xlarge", "r5.24xlarge (96vCPU 768GB)");
                s = s.myReplace("x1.16xlarge", "x1.16xlarge (64vCPU 976GB)");
                s = s.myReplace("x1.32xlarge", "x1.32xlarge (128vCPU 1952GB)");
                s = s.myReplace("d2.xlarge", "d2.xlarge (4vCPU 30.5GB)");
                s = s.myReplace("d2.2xlarge", "d2.2xlarge (8vCPU 61GB)");
                s = s.myReplace("d2.4xlarge", "d2.4xlarge (16vCPU 122GB)");
                s = s.myReplace("d2.8xlarge", "d2.8xlarge (36vCPU 244GB)");
                s = s.myReplace("i3.large", "i3.large (2vCPU 15.25GB)");
                s = s.myReplace("i3.xlarge", "i3.xlarge (4vCPU 30.5GB)");
                s = s.myReplace("i3.2xlarge", "i3.2xlarge (8vCPU 61GB)");
                s = s.myReplace("i3.4xlarge", "i3.4xlarge (16vCPU 122GB)");
                s = s.myReplace("i3.8xlarge", "i3.8xlarge (32vCPU 244GB)");
                s = s.myReplace("i3.16xlarge", "i3.16xlarge (64vCPU 488GB)");
                s = s.myReplace("g3.4xlarge", "g3.4xlarge (16vCPU 122GB)");
                s = s.myReplace("g3.8xlarge", "g3.8xlarge (32vCPU 244GB)");
                s = s.myReplace("g3.16xlarge", "g3.16xlarge (64vCPU 488GB)");
                s = s.myReplace("p2.xlarge", "p2.xlarge (4vCPU 61GB)");
                s = s.myReplace("p2.8xlarge", "p2.8xlarge (32vCPU 488GB)");
                s = s.myReplace("p2.16xlarge", "p2.16xlarge (64vCPU 732GB)");
                s = s.myReplace("p3.2xlarge", "p3.2xlarge (8vCPU 61GB)");
                s = s.myReplace("p3.8xlarge", "p3.8xlarge (32vCPU 244GB)");
                s = s.myReplace("p3.16xlarge", "p3.16xlarge (64vCPU 488GB)");
                if (s.indexOf("vCPU") != -1) {
                    tbl.rows[i].cells[j].innerHTML = s;
                }
            }
        }

    }
    //window.clearInterval(objInterval);
}

objInterval = window.setInterval(checkTable, 1000);