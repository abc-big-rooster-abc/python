# rest_framwork前后端分离 34

![image-20230514103135561](rest_framwork.assets/image-20230514103135561.png)

![image-20230514103154431](rest_framwork.assets/image-20230514103154431.png)



## CBV上权限校验

![image-20230514103759983](rest_framwork.assets/image-20230514103759983.png)

+ 类的下面的所有方法都去除权限校验了

  ![image-20230514103913031](rest_framwork.assets/image-20230514103913031.png)



-----------------------------------------------------------

## restful规范

### 状态码

![image-20230514112754763](rest_framwork.assets/image-20230514112754763.png)



### 你是如何理解rest framework的（面试题10点）

-------------------------



## rest-framework认证  --源码刨析

**流程图**  --返回三个error    元组     None

![image-20230514192642311](rest_framwork.assets/image-20230514192642311.png)

+ **源码   ---入口dispatch**

  ![image-20230514185932566](rest_framwork.assets/image-20230514185932566.png)

+ **封装了request**

  ![image-20230514130950232](rest_framwork.assets/image-20230514130950232.png)

  ![image-20230514131210347](rest_framwork.assets/image-20230514131210347.png)

![image-20230514130506629](rest_framwork.assets/image-20230514130506629.png)

+ **执行构造的authentication--必须返回元组并且是两个**

  ![image-20230514191127561](rest_framwork.assets/image-20230514191127561.png)

+ **可以配置文件里加--将权限校验的函数写到utils工具类里，所有方法都需要认证**

  ![image-20230514204438532](rest_framwork.assets/image-20230514204438532.png)

## day1作业-面试重点:

+ 中间件
  - process_request
  - process_view
  - process_respone
  - process_exception
  - process_render_template
+ csrf
  
+ ![image-20230514145406039](rest_framwork.assets/image-20230514145406039.png)
  
+ CBV本质

+ restful   规范

  - **10条**

    - 协议：API与用户的通信协议，总是使用[HTTPs协议

    - 域名：应该尽量将API部署在专用域名之下https://api.example.com或者 https://example.org/api/

    - 版本最好放在url后面  ： *https*://api.example.com/v1/

    - 路径：在RESTful架构中，每个网址代表一种资源（resource），所以网址中不能有动词，只能有名词，而且所用的名词往往与数据库的表格名对应。一般来说，数据库中的表都是同种记录的"集合"（collection），所以API中的名词也应该使用复数

      - https://api.example.com/v1/animals

    - HTTP动词

      GET（SELECT）：从服务器取出资源（一项或多项）。
      POST（CREATE）：在服务器新建一个资源。
      PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
      PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。
      DELETE（DELETE）：从服务器删除资源。

      （不太常用2个）

      ​	HEAD：获取资源的元数据。

      ​	OPTIONS：获取信息，关于资源的哪些属性是客户端可以改变的

    - 过滤信息（Filtering）

      ?limit=10：指定返回记录的数量
      ?offset=10：指定返回记录的开始位置。
      ?page=2&per_page=100：指定第几页，以及每页的记录数。
      ?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
      ?animal_type_id=1：指定筛选条件

    - 状态码

      200 OK - [GET]：服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。
      201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
      202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
      204 NO CONTENT - [DELETE]：用户删除数据成功。
      400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
      401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
      403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
      404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
      406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
      410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
      422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
      500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。

    - 错误处理

      如果状态码是4xx，就应该向用户返回出错信息。一般来说，返回的信息中将error作为键名，出错信息作为键值即可。

      {

      ​    error: "Invalid API key"

      }

    - 返回结果

      GET /collection：返回资源对象的列表（数组）
      GET /collection/resource：返回单个资源对象
      POST /collection：返回新生成的资源对象
      PUT /collection/resource：返回完整的资源对象
      PATCH /collection/resource：返回完整的资源对象
      DELETE /collection/resource：返回一个空文档

    - Hypermedia API

      RESTful API最好做到Hypermedia，即返回结果中提供链接，连向其他API方法，使得用户不查文档，也知道下一步应该做什么。

      比如，当用户向api.example.com的根目录发出请求，会得到这样一个文档

    - 其他

         (1)   API的身份认证应该使用[OAuth 2.0](http://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html)框架。

      （2）服务器返回的数据格式，应该尽量使用JSON，避免使用XML。

    

+ 面向对象的认识

  - 三大特性：封装继承多态

+ django请求声明周期

  + url请求
  + process_request（中间件）
  + 视图
  + process_view（中间件）

+ djangorestframework

  - 如何认证（基于数据库实现用户认证）
  - 源码流程

-------------

## day2 rest framwork之用户登录

![image-20230514155843868](rest_framwork.assets/image-20230514155843868.png)

![image-20230514155911563](rest_framwork.assets/image-20230514155911563.png)

![image-20230514232557190](rest_framwork.assets/image-20230514232557190.png)

![image-20230514233234533](rest_framwork.assets/image-20230514233234533.png)



### 权限

+ has_permission()   return False表示认证失败 True表示认证成功

  ![image-20230514235539436](rest_framwork.assets/image-20230514235539436.png)

+ **要想自定义会优先选择自定义的（self），否则使用全局的**

![image-20230514234641706](rest_framwork.assets/image-20230514234641706.png)

![image-20230514234710596](rest_framwork.assets/image-20230514234710596.png)

![image-20230515000557292](rest_framwork.assets/image-20230515000557292.png)

![image-20230516070211171](rest_framwork.assets/image-20230516070211171.png)

![image-20230516070200437](rest_framwork.assets/image-20230516070200437.png)



### 频率    

#### 自定义频率限制(节流 )

![image-20230516073858893](rest_framwork.assets/image-20230516073858893.png)

![image-20230516073830097](rest_framwork.assets/image-20230516073830097.png)

使用

![image-20230516074159597](rest_framwork.assets/image-20230516074159597.png)

![image-20230516074549664](rest_framwork.assets/image-20230516074549664.png)

![image-20230516074758821](rest_framwork.assets/image-20230516074758821.png)

 自定义全局配置节流

![image-20230516075006024](rest_framwork.assets/image-20230516075006024.png)

抽离

![image-20230516075053164](rest_framwork.assets/image-20230516075053164.png)

**如果继承BaseThrottle  --好处，规范了需要实现的方法，三个(多了一个get_index,该方法是获取ip地址)**

![image-20230516075422223](rest_framwork.assets/image-20230516075422223.png)

**最终替代  ---都是基于allow_request来实现的**

![image-20230516080344068](rest_framwork.assets/image-20230516080344068.png)

![image-20230516080445439](rest_framwork.assets/image-20230516080445439.png)

**用户限制   --没分钟登录10次**

![image-20230516080831106](rest_framwork.assets/image-20230516080831106.png)

![image-20230516081006248](rest_framwork.assets/image-20230516081006248.png)

## 面试题

![image-20230517224601303](rest_framwork.assets/image-20230517224601303.png)



# day3

![image-20230517230836278](rest_framwork.assets/image-20230517230836278.png)



## 多态---举例

![image-20230517231815158](rest_framwork.assets/image-20230517231815158.png)

### 复习面试题

![image-20230517234611968](rest_framwork.assets/image-20230517234611968.png)

## 

## 版本  

可以放在url、get请求里、请求头里、namespace  --一般放到url上

### URL中通过GET传参----方法一

http://127.0.0.1:8000/api/users/?version=v2

#### 自定义版本

![image-20230518072406434](rest_framwork.assets/image-20230518072406434.png)

![image-20230518072333055](rest_framwork.assets/image-20230518072333055.png)

#### 内部自己也实现了

+ view

![image-20230518073240379](rest_framwork.assets/image-20230518073240379.png)

+ QueryParamterVersioning源码

![image-20230518073007279](rest_framwork.assets/image-20230518073007279.png)

+ 三个变量都是在配置文件里写的

  ![image-20230518073058782](rest_framwork.assets/image-20230518073058782.png)

+ setting.py配置文件

![image-20230518073512539](rest_framwork.assets/image-20230518073512539.png)

### 通过URL中传参----方法二

内部实现

- 笨办法自己每个view里都配置

![image-20230518074114499](rest_framwork.assets/image-20230518074114499.png)

URLPathVersioning

![image-20230518074941903](rest_framwork.assets/image-20230518074941903.png)

urls.py

![image-20230518075238231](rest_framwork.assets/image-20230518075238231.png)

![image-20230518075359630](rest_framwork.assets/image-20230518075359630.png)



+ 可以写在配置文件里

  ![image-20230518075602042](rest_framwork.assets/image-20230518075602042.png)

  - setting.py

    ![image-20230518075642397](rest_framwork.assets/image-20230518075642397.png)

  - view.py  不需要在单独加URLPathVersioning，全局配置

    ![image-20230518075739259](rest_framwork.assets/image-20230518075739259.png)

  

### 版本总结

![image-20230520152119853](rest_framwork.assets/image-20230520152119853.png)

![image-20230520152231140](rest_framwork.assets/image-20230520152231140.png)







## 解析器 

### 局部配置 

![image-20230520161925265](rest_framwork.assets/image-20230520161925265.png)

![image-20230520164812190](rest_framwork.assets/image-20230520164812190.png)

### 全局配置

![image-20230520170114566](rest_framwork.assets/image-20230520170114566.png)

![image-20230520170336642](rest_framwork.assets/image-20230520170336642.png)



##  序列化

![image-20230520171714187](rest_framwork.assets/image-20230520171714187.png)

![image-20230520175032265](rest_framwork.assets/image-20230520175032265.png)

![image-20230520182549855](rest_framwork.assets/image-20230520182549855.png)

举例：![image-20230520182631758](rest_framwork.assets/image-20230520182631758.png)

### Serializer类--继承

![image-20230520190455906](rest_framwork.assets/image-20230520190455906.png)



### ModelSerializer---（Serializer的子类)

+ 添加了多的功能，不要写了，用 fields = "__all__"

  ![image-20230520192035561](rest_framwork.assets/image-20230520192035561.png)



### 总结

![image-20230520193616236](rest_framwork.assets/image-20230520193616236.png)

![image-20230520201336217](rest_framwork.assets/image-20230520201336217.png)

![image-20230520204510350](rest_framwork.assets/image-20230520204510350.png)

**补充：depth = 1  可以获取一对多的多表，和多对多的多表里的所有一级数据**

![image-20230520201107490](rest_framwork.assets/image-20230520201107490.png)

![ ](rest_framwork.assets/image-20230520201226095.png)

### 内容回顾





# day4

![image-20230521165459936](rest_framwork.assets/image-20230521165459936.png)





## 分页

![image-20230521213144099](rest_framwork.assets/image-20230521213144099.png)