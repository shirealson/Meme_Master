<?php
header("Content-Type: text/html;charset=utf-8");
if (!isset($_GET["text"]) || empty($_GET["text"])) {
    echo '{"success":false,"msg":"参数错误"}';
    return;
}
$params = $_GET["text"]; #传递给python脚本的入口参数 
$path = "python ./search.py "; //需要注意的是：末尾要加一个空格
$src = exec($path.$params);//等同于命令`python python.py 参数`，并接收打印出来的信息 
echo '{"success" : true,"src" : "'.$src.'"}';
?>