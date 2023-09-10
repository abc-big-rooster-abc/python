# elasticsearch

![image-20230426211708885](elasticsearch.assets/image-20230426211708885.png)

![image-20230426214431073](elasticsearch.assets/image-20230426214431073.png)



## 安装可视化界面es  head的插件

+ 下载地址

  ![image-20230426220400727](elasticsearch.assets/image-20230426220400727.png)

+ 启动

  ~~~linux
  npm install
  npm run start
  ~~~

+ 连接测试发现，存在跨域问题：配制es

  ~~~shell
  # 开启跨域  允许所有
  http.cors.enabled: true
  http.cors.allow-origin: "*"
  ~~~

+ 重启es服务

### 解决跨域问题：

+ es head 可视化 es跨域问题  9001连接9002

![image-20230426220201721](elasticsearch.assets/image-20230426220201721.png)

![image-20230426221218932](elasticsearch.assets/image-20230426221218932.png)



## ELK

![image-20230426221353889](elasticsearch.assets/image-20230426221353889.png)

## 安装Kibana

![image-20230426221635663](elasticsearch.assets/image-20230426221635663.png)

![image-20230426222356362](elasticsearch.assets/image-20230426222356362.png)



## ES核心概念

+ 一切都是json 
+ ![image-20230426230305057](elasticsearch.assets/image-20230426230305057.png)

![image-20230426223151372](elasticsearch.assets/image-20230426223151372.png)



![image-20230426230046889](elasticsearch.assets/image-20230426230046889.png)



## IK分词器

![image-20230426230433955](elasticsearch.assets/image-20230426230433955.png)

![image-20230426230853698](elasticsearch.assets/image-20230426230853698.png)

![image-20230426232758835](elasticsearch.assets/image-20230426232758835.png)

![image-20230426233508555](elasticsearch.assets/image-20230426233508555.png)

![image-20230426233539472](elasticsearch.assets/image-20230426233539472.png)



+ 发现问题：输入狂神说，被拆开了
+ 这种自己需要的词，需要自己加到我们分词器的字典中

![image-20230426234012395](elasticsearch.assets/image-20230426234012395.png)



## Rest风格说明

![image-20230427071259078](elasticsearch.assets/image-20230427071259078.png)

![image-20230427072651745](elasticsearch.assets/image-20230427072651745.png)

![image-20230427072811976](elasticsearch.assets/image-20230427072811976.png)

### 数据类型

![image-20230427072922071](elasticsearch.assets/image-20230427072922071.png)

### 创建索引和对应的type(类似于数据库中字段)

+ 创建规则

![image-20230427073112447](elasticsearch.assets/image-20230427073112447.png)

![image-20230427073137389](elasticsearch.assets/image-20230427073137389.png)

+ 获得这个规则，可以通过get请求。获取具体的信息

  ![image-20230427073409251](elasticsearch.assets/image-20230427073409251.png)

+ 查看默认的信息

  _doc默认的，（type将要被淘汰）

  ![image-20230427074532823](elasticsearch.assets/image-20230427074532823.png)

![image-20230427074604471](elasticsearch.assets/image-20230427074604471.png)

![image-20230427074941147](elasticsearch.assets/image-20230427074941147.png)

### 修改索引

+ 之前用法

  ![image-20230427075209452](elasticsearch.assets/image-20230427075209452.png)

+ 最新用法 使用POST方法，后面加_update

  ![image-20230427075314587](elasticsearch.assets/image-20230427075314587.png)



### 删除索引

+ 通过DELETE命令，根据你的请求判断是删除索引还是删除索引下的文档

![image-20230427075415206](elasticsearch.assets/image-20230427075415206.png)





## 关于文档的基本操作

### 复杂操作搜索

![image-20230427220200634](elasticsearch.assets/image-20230427220200634.png)



### 输出结果不想要很多 （类似于 select name desc form ***）

![image-20230427220445292](elasticsearch.assets/image-20230427220445292.png)



### 排序

![image-20230427220622853](elasticsearch.assets/image-20230427220622853.png)



### 分页 

![image-20230427221617638](elasticsearch.assets/image-20230427221617638.png)



### 布尔值查询

+ and  must

![image-20230427221924565](elasticsearch.assets/image-20230427221924565.png)

+ or should

  ![image-20230427222103347](elasticsearch.assets/image-20230427222103347.png)

+ not  must_not

  ![image-20230427222140682](elasticsearch.assets/image-20230427222140682.png)



+ 过滤器 filter

  ![image-20230427222314970](elasticsearch.assets/image-20230427222314970.png)



+ 条件查询

  ![image-20230427222741498](elasticsearch.assets/image-20230427222741498.png)



+ 精确查询

  term查询是直接通过倒排索引指定的词条进程精确查找的

  关于分词：

  - term,直接查询精确的

  ​	![image-20230427224803597](elasticsearch.assets/image-20230427224803597.png)

  - match,. 会使用分词器解析，（先分析文档，然后再通过分析的文档进行查询）

  ​	![image-20230427224901556](elasticsearch.assets/image-20230427224901556.png)

  

+ 两个类型 text  keyword

  + 创建文档

    ![image-20230427223158434](elasticsearch.assets/image-20230427223158434.png)

  + 插入数据

    ![image-20230427223317563](elasticsearch.assets/image-20230427223317563.png)

  + 查找testdb

    ![image-20230427224020898](elasticsearch.assets/image-20230427224020898.png)

  ![image-20230427224434347](elasticsearch.assets/image-20230427224434347.png)

  + 

  + 

  + 查找 GET

    + 没有被分析  keyword

    ![image-20230427223744645](elasticsearch.assets/image-20230427223744645.png)、

    + 分析了 默认

  ![image-20230427223810103](elasticsearch.assets/image-20230427223810103.png)





### 高亮查询 

![image-20230427225113980](elasticsearch.assets/image-20230427225113980.png)

![image-20230427225357611](elasticsearch.assets/image-20230427225357611.png)

![image-20230427225525422](elasticsearch.assets/image-20230427225525422.png)





## Python创建索引

![image-20230427230408231](elasticsearch.assets/image-20230427230408231.png)

![image-20230427230356957](elasticsearch.assets/image-20230427230356957.png)



## 插入数据

https://blog.csdn.net/JAY_jzj/article/details/105079415

