# 第一章 Python基础
3. 公司线上和开发环境使用的什么系统？

4. Python和Java、PHP、C、C#、C++等其他语言的对比？

5. 简述解释型和编译型编程语言？

6. Python解释器种类以及特点？

7. 位和字节的关系？

8. b、B、KB、MB、GB 的关系？

9. 请列举你了解的PEP8 规范？

10. 求结果：or and

    ```python
    v1 = 1 or 3
    v2 = 1 and 3
    v3 = 0 and 2 and 1
    v4 = 0 and 2 or 1
    v5 = 0 and 2 or 1 or 4
    v6 = 0 or Flase and 1
    ```

11. ascii、unicode、utf-8、gbk 区别？

12. 字节码和机器码的区别？

13. 三元运算编写格式。

14. 列举你了解的所有Python2和Python3的区别？

15. 用一行代码实现数值交换：

     ```python
     a = 1
     b = 2
     ```

18. Python3和Python2中 int 和 long的区别？

19. xrange和range的区别？

20. 如何实现字符串的反转？如： name = "wupeiqi" 请反转为 name = "iqiepuw" 。

21. 文件操作时：xreadlines和readlines的区别？

22. 列举布尔值为False的常见值？

23. 列举字符串、列表、元组、字典每个常用的5个方法？

24. is和==的区别?

25. 1、2、3、4、5 能组成多少个互不相同且无重复的三位数

26. 什么是反射？以及应用场景？

27. 简述Python的深浅拷贝？

24. Python垃圾回收机制？ 

    引用计数器为主，标记清除和分代回收为辅。
    
    - 引用计数器
    Python中每个对象内部都维护了一个值，该值记录这此对象被引用的次数，如果次数为0，则Python垃圾回收机制会自动清除此对象。
    
30. 求结果

    ```python
    v = dict.fromkeys(['k1','k2'],[])
    v['k1'].append(666)
    print(v)
    v['k1'] = 777
    print(v)
    ```

31. 一行代码实现删除列表中重复的值 ?

32. 如何实现 “1,2,3” 变成 [‘1’,’2’,’3’] 

33. 如何实现[‘1’,’2’,’3’]变成[1,2,3] 

34. 比较： a = [1,2,3] 和 b = [(1),(2),(3) ] 以及 c = [(1,),(2,),(3,) ] 的区别？

35. 如何用一行代码生成[1,4,9,16,25,36,49,64,81,100] ?

36. 常用字符串格式化哪几种？

37. 什么是断言（assert）？应用场景？

38. 有两个字符串列表a和b，每个字符串是由逗号分隔的一些字符：

    ```python
    b= [ 'a,1',
        'b,3,22',
        'c,3,4',
    ]
    
    b = [
        'a,2',
        'b,1',
        'd,2',
    ]
    按每个字符串的第一个值，合并a和b到c
    
    c = [
        'a,1,2',
        'b,3,22,1',
        'c,3,4',
        'd,2'
    ]
    ```

39. 有一个多层嵌套的列表A=[1,2,[3,4,["434",...]]], 请写一段代码遍历A中的每一个元素并打印出来

40. a = range(10),a[::-3] 的结果是 \____________

41. 下面那个命令可以从虚拟环境中退出

    ```
    A.  deactivate
    B.  exit
    C.  quit
    D.  以上均可
    ```

42. 将列表内的元素,根据位数合并成字典

    ```python
    lst = [1,2,4,8,16,32,64,128,256,512,1024,32769,65536,4294967296]
    
    # 输出
    {
        1:[1,2,3,8],
        2:[16,32,64],
        3:[128,256,512],
        4:[1024,],
        5:[32769,65536],
        6:[4294967296]
    }
    ```

43. 请尽量用简洁的方法将二维数组转换成一维数组

    ```
    例: 转换前 lst=[[1,2,3],[4,5,6],[7,8,9]]
    
    转换后lst = [1,2,3,4,5,6,7,8,9]
    ```

44. 将列表按下列规则排序, 补全代码

    ```
    1.正数在前负数在后
    2.正数从小到大
    3.负数从大到小
    
    例: 
    
    排序前[7,-8,5,4,0,-2,-5]
    
    排序后[0,4,5,7,-2,-5,-8]
    
    补全代码:
    
    sorted(lst,key=lambda x:_____)
    ```

45. 哈希冲突回避算法有哪几种, 分别有什么特点？

46. 简述Python的字符串驻留机制？

47. 以下代码输出是什么? list=['a','b','c','d','e'] print list[10:]

    ```
    A.  []
    B.  程序异常
    C.  ['a','b','c','d','e']
    D.  输出空
    ```

48. Python语言什么那些类型的数据才能做为字典的key?

    ```
    A.  没有限制
    B.  字母数字下划线
    C.  字母
    D.  可被hash的类型
    ```

49. 以下两段代码的输出一样吗, 占用系统资源一样吗, 什么时候要用xrange代替range

    ```python
    for i  in range(1): print i
    
    for i in xrange(1): print i
    ```

50. 如下代码段

    ```
    a = [1,2,3,[4,5],6]
    b = a 
    c = copy.copy(a)
    d = copy.deepcopy(a)
    b.append(10)
    c[3].append(11)
    d[3].append(12)
    请问a,b,c,d的值为;
    ```

51. 现有字典d={"a":26,"g":20,"e":20,"c":24,"d":23,"f":21,"b":25} 请按照字段中的value字段进行排序。

52. 给定两个listA,B,请用Python找出A,B中相同的元素,A,B中不同的元素

53. 下列叙述中错误的是

    ```
    A.  栈是线性结构
    B.  队列是线性结构
    C.  线性列表是线性结构
    D.  二叉树是线性结构
    ```

54. 一个栈的输入序列为1,2,3,4,5, 则下列序列中不可能是栈的输出序列的是

    ```
    A.  1 5 4 3 2
    B.  2 3 4 1 5
    C.  1 5 4 2 3
    D.  2 3 1 4 5
    ```

55. 下图那些PEP被认为涉及到了代码规范

    ```
    1.  PEP7
    2.  PEP8
    3.  PEP20
    4.  PEP257
    ```

56. 下面那些是Python合法的标识符？那些是Python的关键字？

    ```
    1.  int32
    2.  40XL
    3.  saving$
    4.  ptint
    5.  this
    6.  self
    7.  0x40L
    8.  true
    9.  big-daddy
    10.  True
    11.  if
    12.  do
    13.  yield
    ```

57. 从0-99这100个数中随机取出10个, 要求不能重复, 可以自己设计数据结构

58. python 判断一个字典中是否有这些key: "AAA",'BB','C',"DD",'EEE'(不使用for while)

59. 有一个list["This","is","a","Boy","!"], 所有元素都是字符串, 对他进行大小写无关的排序

60. 描述下dict的item()方法与iteritems()的不同

61. 请列举你所知道的Python代码检测工具及他们间的区别？

62. 介绍一下try except的用法和作用?

63. 输入一个字符串, 返回倒序排列的结果 如: abcdef, 返回 fedcba

64. 阅读以下代码, 并写出程序的输出结果

    ```python
    alist = [2,4,5,6,7]
    for var in alist:
        if var %2 ==0:
            alist.remove(var)
    alist的最终结果是
    ```

65. 现有列表alist=[3,1,-4,-2],按期元素的绝对值大小进行排序?

66. 填空题

    ```python
    1. 表达式 3<4<5 是哪一个表达式的缩写___.
    2. 获取Python解释器版本的方法是:____.
    3. 如果模块是被导入的,__name__的值是____, 如果模块是被直接执行的__name__的值是___.
    4. Python的内存管理中, 为了追踪内存中的对象, 使用了____这一简单技术
    5. Python的标准解释器是有C语言实现的, 称为____, 有Java实现的被称为___.
    6. Python中, ___语句能直接显示的释放内存资源
    7. Python的乘方运算符是__
    ```

67. 现有字典mydict和变量onekey, 请写出从mydict中取出onekey值的方法(不止一种写法, 多写加分, 并请叙述不同写法的区别, mydict中是否存在onekey的键值, 不确定)

68. 现有一列表alist, 请写出两种去除alist中重复元素的方法, 其中：

    - 要求保持原有列表中元素的排列顺序。
    - 无需考虑原有列表中元素的排列顺序。

69. 请描述Unicode,utf-8, gbk等编码之间的区别?

70. 那些情况下, y != x - (x-y)会成立?

71. 用Python实现99乘法表(用两种不同的方法实现)

72. 获取list中的元素个数,和向末尾追加元素所用的方法分别是什么？

73. 判断dict中有没有某个key用的方法是什么？

74. 填空

    ```python
    l=range(100)
    
    1. 如何取第一到第三个元素用的是
    2. 如何取倒数第二个元素
    3. 如何取后十个
    ```

75. 如何判断一个变量是否是字符串？

76. list和tuple有什么不同？

77. a = dict(zip(("a","b","c","d","e"),(1,2,3,4,5)))   请问a是什么？

78. 一行代码生成列表 [1,4,9,16,25,36,49,64,81,100]。

79. 以下叙述正确的是

    ```
    A.  continue语句的作用是结束整个循环的执行
    B.  只能在循环体和switch语句体内使用break语句
    C.  在循环体内使用break语句或者continue语句的作用相同
    D.  从多层循环嵌套中退出时, 只能使用goto语句
    ```

80. 读代码

    ```
    for i in range(5,0,-1):
        print(i)
    请在下面写出打印结果
    ```

81. 写结果

    ```
    x= "foo"
    y = 2
    print x+y
    -------
    A.  foo
    B.  foo foo
    C.  foo 2
    D.  2
    E.  An exception is thrown
    ```

82. 求结果

    ```
    kvps = {"1":1,"2":2}
    theCopy = kvps
    kvps["1"] = 5
    sum = kvps["1"] + theCopy ["1"]
    print sum
    
    A.  1
    B.  2
    C.  7
    D.  10
    ```

83. python里如何实现tuple和list的转化

84. type(1+2L*3.14)的结果是

    ```
    A.  int
    B.  long
    C.  float
    D.  str
    ```

85. 若k为整型, 下列while循环执行的次数为

    ```
    k = 1000
    while k>1:
        print k
        k = k/2
    ```

86. 以下何者是不合法的布尔表达式

    ```
    A.  x in range(6)
    B.  3 = a
    C.  e>5 and 4==f
    D.  (x-6)>5
    ```

87. python不支持的数据类型有

    ```
    A.  char
    B.  int
    C.  float
    D.  list
    ```

88. 如何在Python中拷贝一个对象, 并说明他们之间的区别？

89. 99(10进制)的八进制表示是什么？

90. 下列Python语句正确的是

    ```
    1.  min = x is x<y=y
    2.  max = x>y?x:y
    3.  if(x>y) print x
    4.  while True:pass
    ```

91. list对象 alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'v','age':25},]按alist中元素的age由大到小排序。

92. 关于Python程序的运行性能方面, 有什么手段能提升性能？

93. Python是如何进行内存管理的? Python的程序会内存泄漏吗?说说有没有什么方面阻止或检测内存泄漏

94. 详细说说tuple,list,dict的用法, 他们的特点

95. 一个大小为100G的文件etl_log.txt, 要读取文件中的内容, 写出具体过程代码？

96. 已知Alist=[1,2,3,1,2,1,3],如何根据Alist得到[1,2,3]

97. 已知stra = 'wqedsfsdrfweedqwedqw'

    ```
    1.  如何获取最后两个字符
    2.  如何获取第二个和第三个字符
    ```

98. 已知Alist = ["a","b","'c'],将Alist转化为'a,b,c'的实现过程

99. 已知ip='192.168.0.100' 代码实现提取各部分并写入列表。

100. python代码如何获取命令行参数？

101. 写代码

     ```
     tupleA = ("a","b","c","d","e")
     tupleB = (1,2,3,4,5)
     RES = {"a":1,"b":2,"c":3,"d":4,"e":5}
     
     写出由tupleA和tupleB得到res的及具体实现过程
     ```

102. 选出一下表达式表述正确的选项

     ```
     A.  {1:0,2:0,3:0}
     B.  {'1':0,'2':0,'3':0}
     C.  {(1,2):0,(4,3):0}
     D.  {[1,2]:0,[4,3]:0}
     E.  {{1,2}:0,{4,3}:0}
     ```

103. what gets printde() ?

     ```
     kvps = {"1":1,'2':2}
     theCopy = kvps.copy()
     kvps["1"] = 5
     sum = kvps["1"] + theCopy["1"]
     print sum
     
     A.  1
     B.  2
     C.  6
     D.  10
     E.  An execption is thrown
     ```

104. what gets printde() ?

     ```
     numbers = [1,2,3,4]
     numbers.append([5,6,7,8])
     print len(numbers)
     
     A.  4
     B.  5
     C.  8
     D.  12
     E.  An exception is thrown
     ```

105. what getsprintde() ?

     ```
     names1 = ["Amir","Barry","Chaies","Dao"]
     if "amir" in names1:
        print 1
     else:
        print 2
     
     A.  1
     B.  2
     C.  An exception is thrown
     ```

106. what getsprintde() ? Assuming ptrhon version2.x()

     ```
     print(type(1/2))
     
     A.  int
     B.  float
     C.  0
     D.  1
     E.  0.5
     ```

107. 以下用来管理Python库管理工具的是

     ```
     A.  APT
     B.  PIP
     C.  YUM
     D.  MAVEN
     ```

108. which numbers are printed ()?

     ```
     for i in range(2):
         print i
     
     for i in range(4,6):
         print i
     
     A.  2,4,6
     B.  0,1,2,4,5,6
     C.  0,1,4,5
     D.  0,1,4,5,6,7,8,9
     E.  1,2,4,5,6
     ```

109. 求结果

     ```
     import math
     print (math.floor(5.5))
     
     A.  5
     B.  5.0
     C.  5.5
     D.  6
     E.  6.0
     ```

110. 关于Python的内存管理, 下列说法错误的是

     ```
     A.  变量不必事先声明
     B.  变量无需先创建和赋值而直接使用
     C.  变量无需指定类型
     D.  可以使用del释放资源
     ```

111. 下面那个不是Python合法的标识符

     ```
     A.  int32
     B.  40xl
     C.  self
     D.  name
     ```

112. 下列哪种说法是错误的

     ```
     A.  除字典类型外, 所有标准对象均可用于布尔测试
     B.  空字符串的布尔值是False
     C.  空列表对象的布尔值是False
     D.  值为0的任何数字对象的布尔值是False
     ```

113. 下列表达是的值为True的是

     ```
     A.  5+4j >2-3j
     B.  3>2>2
     C.  (3,2)<("a","b")
     D.  " abc" > 'xyz'
     ```

114. 关于Python的复数, 下列说法错误的是

     ```
     A.  表示复数的语法是 real+imagej
     B.  实部和虚部都是浮点数
     C.  虚部后缀必须是j, 且必须小写
     D.  方法conjugate返回复数的共轭复数
     ```

115. 关于字符串下列说法错误的是

     ```
     A.  字符应视为长度为1的字符串
     B.  字符串以\0标志字符串的结束
     C.  既可以用单引号, 也可以用双引号创建字符串
     D.  在三引号字符串中可以包含换行回车等特殊字符
     ```

116. 以下不能创建一个字典的语句是

     ```
     A.  dic1 = {}
     B.  dic2 = {3:5}
     C.  dic3 = {[1,2,3]:"usetc"}
     D.  dic4 = {(1,2,3):"usetc"}
     ```

117. python里面如何拷贝一个对象?(赋值,浅拷贝,深拷贝的区别)

118. 描述在python中的元祖,列表,字典的区别,并且分别写一段定义,添加,删除操作的代码片段。

119. 选择结果

     ```
     names1 = ["Amir","Barry","Chales","Dao"]
     names2 = names1
     names3 = names1[:]
     name2[0] = "Alice"
     names3[1] =  "Bob"
     sum = 0
     for ls in (names1,names2,names3):
         if ls[0] == "Alice":
             sum+=1
         if ls[1]=="Bob":
             sum+=10
     
     print sum
     
     
     A.  11
     B.  12
     C.  21
     D.  22
     E.  23
     ```

120. 下面程序的输出结果是

     ```
     x = True
     y = False
     z = False
     
     if x or y and z:
         print 'yes'
     else:
         print 'no'
     ```

121. 1 or 2 和1 and 2输出分别是什么? 为什么

122. 1 <(2==2)和1 <2==2的结果分别是什么, 为什么

123. 如何打乱一个排好序的list对象alist

124. 如何查找一个字符串中特定的字符?find和index的差异？

125. 把aaabbcccd这种形式的字符串压缩成a3b2c3d1这种形式。

126. Python 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。 

127. 输入一个字符串, 输出该字符串中字符的所有组合. 

     ```
     例如: 输入字符串"1,2,3", 则输出为1,2,3,12,13,23,123(组合数, 不考虑顺序, 所以12和21是等价的)
     ```

128. 执行以下代码后, i和n的值为

     ```
     int i=10;
     int n=i++%5
     
     
     A.  10, 0
     B.  10, 1
     C.  11, 0
     B.  11, 1
     ```

129. 执行以下代码段后,x的值为

     ```
     int x=10;
     x+=x-=x-x;
     
     
     A.  10
     B.  20
     C.  30
     D.  40
     ```

130. 对于一个非空字符串,判断其是否可以有一个子字符串重复多次组成,字符串只包含小写字母且长度不超过10000

     ```
     示例1:
     
     1.  输入"abab"
     2.  输出True
     3.  样例解释: 输入可由"ab"重复两次组成
     
     示例2:
     
     1.  输入"abcabcabc"
     2.  输出True
     3.  样例解释: 输入可由"abc"重复三次组成
     
     示例3:
     
     1.  输入"aba"
     2.  输出False
     ```



# 第二章 函数

1. 通过代码实现如下转换：

   ```python
   二进制转换成十进制：v = “0b1111011”
   十进制转换成二进制：v = 18
   八进制转换成十进制：v = “011”
   十进制转换成八进制：v = 30
   十六进制转换成十进制：v = “0x12”
   十进制转换成十六进制：v = 87
   ```

2. Python递归的最大层数？

3. 列举常见的内置函数？

4. filter、map、reduce的作用？

5. 一行代码实现9\*9乘法表

6. 什么是闭包？

7. 简述 生成器、迭代器、装饰器以及应用场景？

8. 使用生成器编写fib函数, 函数声明为fib(max), 输入一个参数max值, 使得该函数可以这样调用。

   ```python
   for i in range(0,100):
       print fib(1000)
   
   并产生如下结果(斐波那契数列),1,1,2,3,5,8,13,21...
   ```

9. 一行代码, 通过filter和lambda函数输出以下列表索引为基数对应的元素。

   ```python
   list_a=[12,213,22,2,2,2,22,2,2,32]
   ```

10. 写一个base62encode函数, 62进制。

    ```python
    即:0123456789AB..Zab..z(10个数字+26个大写字母+26个小写字母)。
    	base62encode(1)=1
    	base62encode(61) = z 
    	base62encode(62)=10
    ```

11. 请实现一个装饰器, 限制该函数被调用的频率, 如10秒一次

12. 请实现一个装饰器, 通过一次调用使函数重复执行5次。

13. python一行print出1~100偶数的列表, (列表推导式, filter均可)

14. 解释生成器与函数的不同, 并实现和简单使用generator.

15. 列表推导式和生成器表达式 [i % 2 for i in range(10)] 和 (i % 2 for i in range(10)) 输出结果分别是什么？

16. map(str,[1,2,3,4,5,6,7,8,9]) 输出是什么？

17. python中定义函数时如何书写可变参数和关键字参数?

18. Python3.5中enumerate的意思是什么？

19. 说说Python中的装饰器,迭代器的用法:描述下dict的item方法与iteritems方法的不同

20. 是否使用过functools中的函数？其作用是什么？

21. 如何判断一个值是函数还是方法？

22. 请编写一个函数实现将IP地址转换成一个整数。

    ```
    如 10.3.9.12 转换规则为：
            10            00001010
             3            00000011
             9            00001001
            12            00001100
            
    再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？
    ```

23. lambda表达式格式以及应用场景？

24. pass的作用？

25. *arg和**kwarg作用?

26. 如何在函数中设置一个全局变量 ?

27. 请写出打印结果：

    ```
    # 例 1
    def func(a,b=[]):
      b.append(a)
        print(b)
    func(1)
    func(1)
    func(1)
    func(1)
    
    
    # 例 2
    def func(a,b={}):
      b[a] = 'v'
      print(b)
    func(1)
    func(2)
    
    ```

28. 求结果： lambda

    ```
    def num():
      return [lambda x:i*x for i in range(4)]
    print([m(2) for m in num()])
    
    ```

29. 简述 yield和yield from关键字。

30. 有processFunc变量 ,初始化为processFunc = collapse and (lambda s:" ".join(s.split())) or (lambda s:s)

    调用上下文如下

    ```
    collapse = True
    processFunc = collapse and (lambda s:" ".join(s.split())) or (lambda s:s)
    print processFunc("i\tam\ntest\tobject !")
    
    collapse = False
    processFunc = collapse and (lambda s:" ".join(s.split())) or (lambda s:s)
    print processFunc("i\tam\ntest\tobject !")
    
    ```

    以上代码会在控制台输出什么?

31. 请给出下面代码的输出结果

    ```
    a = 1
    def fun(a):
        a = 2
    
    fun(a)
    print a
    
    a = []
    def fun(a):
        a.append(1)
    
    fun(a)
    print a
    
    ```

32. 全局变量和局部变量的区别, 如何给function里面的一个全局变量赋值

33. 什么是lambda函数, 下面这段代码的输出是什么

    ```
    nums = range(2,20)
    for i in nums:
        nums = filter(lambda x:x==i or x % i, nums)
    nums
    
    ```

34. 指出下面程序存在的问题

    ```
    def Lastllindextem(src, index):
        '''请返回传入src使用空格或者"\"切分后的倒数第index个子串'''
        return src.split("\")[-index]
    
    ```

35. 有一个数组[3,4,1,2,5,6,6,5,4,3,3] 请写一个函数, 找出该数组中没有重复的数的总和. (上面数据的么有重复的总和为1+2=3)

36. 求打印结果

    ```
    arr = [1,2,3]
    def bar():
        arr+=[5]
    
    bar()
    print arr
    ---------------------
    A.  error
    B.  [5]
    C.  [1,2,3]
    D.  [1,2,3,5]
    
    
    ```

37. 请写一个函数, 计算出如下几个字母代表的数字

    ```
    AB-CD=EF
    EF+GH = PPP
    ```
    
38. 请给出下面代码片段的输出

    ```python
    def say_hi(func):
        def wrapper(*args,**kwargs):
            print("HI")
            ret = func(*args,**kwargs)
            print("BYE")
            return ret
        return wrapper
    
    def say_yo(func):
        def wrapper(*args,**kwargs):
            print("YO")
            return func(*args,**kwargs)
        return wrapper
    
    @say_hi
    @say_yo
    def func():
        print("ROCK & ROLL")
    
    func()
    ```

39. 请简述标准库中functools.wraps的作用

40. 请给出下面代码片段的输出

    ```python
    def test():
        try:
            raise ValueError("something wrong")
        except ValueError as e:
            print("Error occurred")
            return
        finally:
            print("Done")
    
    test()
    ```

41. 下面的函数,那些会输出1,2,3三个数字

    ```
    for i in range(3):
        print i
    
    ```

    ```
    alist = [0,1,2]
    for i in alist:
        print i+1
    
    ```

    ```
    i = 1
    while i<3:
        print i
        i+=1
    ​```
    
    ​```
    for i in range(3):
        print i+1
    ​```
    
    ```

42. 以下函数需要在其中引用一个全局变量k, 请填写语句

    ```
    def fun():
       __________
       k = k+1
    
    ```

43. 请把以下函数转化为python lambda匿名函数

    ```
    def add(x,y):
        return x+y
    
    ```

44. 阅读以下代码, 并写出程序的输出结果

    ```
    my_dict = {"a":0,"b":1}
    
    def func(d):
        d["a"]=1
        return d
    
    func(my_dict)
    my_dict["c"]=2
    print my_dict
    
    ```

45. 填空题

    ```python
    # 有函数定义如下
    def calc(a,b,c,d=1,e=2):
        return (a+b)*(c-d)+e
    
    # 请分别写出以下标号代码的输出结果, 如果出错请写出Error
    print calc(1,2,3,4,5) # ____
    print calc(1,2,3) # ____
    print calc(1,2) # ____
    print calc(1,2,3,e=4) # ____
    print calc(e=4, c=5, a=2,b=3) # ____
    print calc(1,2,3, d=5,4) # ____
    ```

46. def(a, b=[])这种写法有什么陷阱？

47. 函数

    ```
    def add_end(l=[]):
        l.append("end")
        return l
    
    add_end() # 输出什么
    add_end() # 再次调用输出什么? 为什么
    
    ```

48. 函数参数 *args,**kwargs的作用是什么

    ```
    def func(a,b,c=0,*args,**kwargs):
        pass
    
    
    ```

49. 可变参数定义 `*args`,`**kwargs`的区别是什么?并且写出下边代码的输入内容

    ```
    def foo(*args,**kwargs):
    	print("args=",agrs)
    	print("kwargs=",kwargs)
    	print("-----------------")
    	
    if __name__ =='__main__':
    	foo(1,2,3,4)
    	foo(a=1,b=2,c=3)
    	foo(1,2,3,4,a=1,b=2,c=3)
    	foo("a",1,None,a=1,b="2",c=3)
    
    ```

50. 请写出log实现(主要功能时打印函数名)

    ```
    @log
    def now():
        print "2013-12-25"
    
    now()
    输出
    call now()
    2013-12-25
    
    ```

51. Python如何定义一个函数

    ```
    A.  class <name>(<Type> arg1, <type> arg2, ...)
    B.  function <name>(arg1,arg2,...)
    C.  def <name>(arg1, arg2,...)
    D.  def <name>(<type> arg1, <type> arg2...)
    
    ```

52. 选择代码运行结果

    ```
    country_counter ={}
    
    def addone(country):
        if country in country_counter:
            country_counter[country ]+=1
        else:
            country_counter[country ]= 1
    
    addone("China")
    addone("Japan")
    addone("china")
    print len(country_counter )
    
    
    A.  0
    B.  1
    C.  2
    D.  3
    E.  4
    
    ```

53. 选择输出结果

    ```
    def doff(arg1,*args):
        print type(args)
    
    doff("applea","bananas","cherry")
    
    
    A.  str
    B.  int
    C.  tuple
    D.  list
    E.  dict
    
    ```

54. 下面程序的输出结果是

    ```
    d = lambda p:p*2
    t = lambda p:p*3
    
    x = 2
    x = d(x)
    x = t(x)
    x = d(x)
    print x
    
    ```

55. 什么是lambda表达式？

56. 以下代码输出是什么,请给出答案并解释

    ```
    def multipliers():
        return [lambda x:x*i for i in range(4)]
    
    print([m(2) for m in multipliers()])
    请修改multipliers的定义来产生期望的结果
    ```
    
57. 有 0 < x <= 10, 10 < x <= 20, 20 < x <= 30, .，190 < x〈= 200,200 < x这样的21个区间分别对应1-21二十一个级别，请编写一个函数 level (x)根据输入数值返回对应级别。

58. 写函数

    有一个数据结构如下所示，请编写一个函数从该结构数据中返画由指定的 字段和对应的值组成的字典。如果指定字段不存在，则跳过该字段。

    ```python
    data:{
        "time":"2016-08-05T13:13:05",
        "some_id":"ID1234",
        "grp1":{"fld1":1, "fld2":2,},
        "xxx2":{"fld3":0, "fld4":0.4,},
        "fld6":11,
        "fld7": 7,
        "fld46":8
    }
    
    fields:由"|"连接的以fld开头的字符串, 如fld2|fld7|fld29
    
    def select(data,fields):
        return result
    ```

59. 补全代码

    ```
    若要将N个task分配给N个worker同时去完成, 每个worker分别都可以承担这N个task,但费用不同. 下面的程序用回溯法计算总费用最小的一种工作分配方案, 在该方案中, 为每个worker分配1个task.
    
    程序中,N个task从0开始顺序编号, N个worker也从0开始顺序编号, 主要的变量说明如下:
    
    - ci:将任务i分配给worker j的费用
    - task[i]: 值为0表示task i未分配, 值为j表示task i分配给worker j
    - worker[k] 值为0表示未分配task, 值为1表示worker k已分配task;
    - mincost: 最小总费用
    
    程序
    
        N=8
        mincosr = 65535
        worker = []
        task = []
        temp = []
        c = []
        def plan(k, cost):
            global  mincosr
            if __(1)__ and cost<mincosr:
                mincosr = cost
                for i in xrange(N):
                    temp[i] = task[i]
            else:
                for i in xrange(N):
                    if worker[i] ==0 and __(2)__:
                        worker[i] = 1
                        task[k] = __(3)__
                        plan(__(4)__,cost+c[k][i])
                        __(5)__
                        task[k] = 0
        def main():
            for i in xrange(N):
                worker.append(0)
                task.append(0)
                temp.append(0)
                c.append(0)
                for j in xrange(N):
                    print "请输入 worker"+str(i)+"完成 task" + str(j)+"的花费"
                    input_value = input()
                    c[i].append(int(input_value))
        plan(0,0)
        print('\n 最小费用: '+str(mincosr))
        for i in xrange(N):
            print "Task"+str(i)+"is assigned to Worker" + str(temp[i])
        if __name__ == "__main__":
            main()
    ```

60. 写个函数接收一个文件夹名称作为参数, 显示文件夹中文件的路径, 以及其中包含文件夹中文件的路径。



# 第三章 模块

1. 列举常用的模块。

2. 如何安装第三方模块？

3. re的match和search区别？

4. 什么是正则的贪婪匹配？或 正则匹配中的贪婪模式与非贪婪模式的区别？

5. 如何生成一个随机数？

6. 如何使用python删除一个文件？

7. logging模块的作用？以及应用场景？

8. json序列化时，可以处理的数据类型有哪些？如何定制支持datetime类型？

9. json序列化时，默认遇到中文会转换成unicode，如果想要保留中文怎么办？

10. 写代码实现查看一个目录下的所有文件。

11. 用Python匹配HTML tag的时候,<.*>和<.*?>有什么区别?

12. 如何判断一个邮箱合法

13. 请写出以字母或下划线开始, 以数字结束的正则表达式

14. 下面那些是Python开发网络应用的框架

    ```
    1.  Django
    2.  Yii
    3.  Struts
    4.  Rails
    5.  Uliweb
    6.  CodeIgniter
    7.  gevent
    8.  Flask
    9.  web2py
    10.  Pylons
    11.  Tornado
    12.  Twisted
    13.  TurboGears
    ```

15. 写Python爬虫都用到了那些模块, 分别是做什么用的?

16. sys.path.append("/root/mods")的作用？

17. 列举出Python中比较熟知的爬虫框架

18. 输入某年某日, 判断这是这一年的第几天?(可以用Python的内置模块)

19. 使用过Python那些第三方组件？

# 第四章 面向对象

1. 简述面向对象的三大特性。

2. 什么是鸭子模型？

3. super的作用？

4. mro是什么？

5. 什么是c3算法？

6. 列举面向对象中带双下划线的特殊方法。

7. 双下划线和单下划线的区别？

8. 实例变量和类变量的区别？

9. 静态方法和类方法区别？

10. isinstance和type的作用？

11. 有用过with statement（语句）吗？它的好处是什么？

12. 下列数据结构中,哪一种是不可迭代的

    ```
    A.  dict
    B.  object
    C.  set
    D.  str
    ```

13. 实现一个Singleton单例类, 要求遵循基本语言编程规范（用尽量多的方式）。

14. 请描述with的用法, 如果自己的类需要支持with语句, 应该如何书写?

15. python中如何判断一个对象是否可调用? 那些对象可以是可调用对象?如何定义一个类, 使其对象本身就是可调用对象?

16. 请实现一个栈。

17. 关于Python类的继承不正确的说法是?(多选)

    ```python
    A.  Python类无法继承
    B.  可以继承, 无法执行父类的构造函数
    C.  可以有多个父类
    D.  只能有一个父类
    ```

18. 实现一个hashtable类, 对外暴露的有add和get方法, 满足以下测试代码

    ```
    def test():
        import uuid
        name = {"name", "web", "python"}
        ht = HashTable()
        for key in names:
            value = uuid.uuid4()
            ht.add(key,value)
            print("add元素",key,value)
    
        for key in names:
            v = ht.get(key)
            print("get 元素",key, v)
    ```

19. 请用两个队列来实现一个栈(给出伪代码即可)

20. 已知如下链表类, 请实现单链表逆置

    ```
    class Node:
        def __init__(self, value, next):
            self.value = value
            self.next = next
    ```

21. 类的加载顺序(类中有继承有构造有静态)？

22. 参考下面代码片段

    ```
    class Context:
        pass
    
    with Content() as ctx:
        ctx.do_something()
    请在Context类下添加代码完成该类的实现
    ```

23. 以下代码输出是什么? 请给出答案并解释。

    ```
    class Parent(object):
        x = 1
    
    class Child1(Parent):
        pass
    
    class Child2(Parent):
        pass
    
    print Parent.x, Child1.x, Child2.x
    
    Child1.x = 2
    print Parent.x, Child1.x, Child2.x
    
    Parent.x = 3
    print Parent.x, Child1.x, Child2.x
    ```

24. 函数del_node(self,data)的功能: 在根节点指针为root的二叉树(又称二叉排序树)上排除数值为K的节点,若删除成功,返回0,否则返回-1, 概述节点的定义类型为

    ```
    class Node(object):
        def __init__(self,data):
            self.data = data # 节点的数值
            self.left_child = Node # 指向左右子树的指针
            self.right_child = Node
    
        def set_data(self,data):
            self.data = data
    
    
    ```

25. 请给出下面代码片段的输出，请简述上面代码需要改进的地方？

    ```
    class Singleton:
        _instance = None
        def __new__(cls, *args, **kwargs)
            print("New")
            if cls._instance is None:
                print("Create")
                cls._instance = super().__new__(cls,*args, **kwargs)
            return cls._instance
    
        def __init__(self):
            print("Initalize")
            self.prop  = None
    
    s1 = Singleton()
    s2 = singleton()
    ```

26. 请简单解释Python中的static method(静态方法)和class method(类方法),并将以下代码填写完整。

    ```
    class A(object):
        def foo(self,x)
            print 'executing foo(%s, %s)'%(self,x)
    
        @classmethod
        def class_foo(cls,x):
            print 'executing class_foo(%s, %s)'%(cls,x)
    
        @staticmethod
        def static_foo(x):
            print 'executing static_foo(%s)'%(x)
    
    a= A()
    # 调用foo函数,参数传入1
    ____________________
    # 调用class_foo函数,参数传入1
    ____________________
    # 调用static_foo函数,参数传入1
    ____________________
    
    ```

27. 已知一个订单对象（tradeOrder）有如下字段：

    | 字段英文名   | 中文名       | 字段类型               | 取值                                                 |
    | ------------ | ------------ | ---------------------- | ---------------------------------------------------- |
    | Id           | 主键         | Long                   | 123456789                                            |
    | Name         | 姓名         | String                 | 张三                                                 |
    | Items        | 商品列表集合 | List<商品>（关联商品） | 查找商品对象，一个订单有两个商品。商品字段任意取值。 |
    | IsMember     | 是否是会员   | Boolean                | True                                                 |
    | CouponAmount | 优惠券金额   | Bigdecimal             | Null                                                 |

    商品对象

    | 字段英文名称 | 中文名   | 字段类型 | 取值      |
    | ------------ | -------- | -------- | --------- |
    | Id           | 主键     | Long     | 987654321 |
    | Name         | 商品名称 | String   | 手机      |

    问题：若将订单对象转成JSON格式，请书写出转换后的JSON字符串。

28. 写代码(栈与队列)

    编程实现一个先进先出的队列类, 能指定初始化时的队列大小, 以及enqueue,dequeue,is_empty, is_full四种方法

    使用方法如下

    ```
    s = Queue(2) # 初始化一个大小为2的队列
    s.is_empty() # 初始化后, 队列为空, 返回True
    s.enqueue(1) # 将1加入队列
    s.enqueue(2) # 将2加入队列
    s.isfull() # 加入了两个元素, 队列已满, 返回True
    s.dequeue() # 移除一个元素, 返回1
    s.dequeue() # 移除一个元素, 返回2
    s.is_empty() # 队列已经为空, 返回True
    ```

29. 编程实现一个后进先出的栈类, 能指定初始化时的队列大小, 以及push, pull ,is_empty, is_full四种方法

    使用方法如下

    ```
    s = Stack(2) # 初始化一个大小为2的队列
    s.is_empty() # 初始化后, 队列为空, 返回True
    s.push(1) # 将1加入栈
    s.push(2) # 将2加入栈
    s.isfull() # 加入了两个元素, 队列已满, 返回True
    s.pull() # 移除一个元素, 返回2
    s.pull() # 移除一个元素, 返回1
    s.is_empty() # 队列已经为空, 返回True
    ```


# 第五章 网络和并发编程

1. python的底层网络交互模块有哪些？

2. 简述 OSI 七层协议。

3. 什么是C/S和B/S架构？

4. 简述 TCP 三次握手、四次挥手的流程。

5. 什么是arp协议？

6. TCP和UDP的区别？为何基于tcp协议的通信比基于udp协议的通信更可靠？

7. 什么是局域网和广域网？

8. 什么是socket？简述基于tcp协议的套接字通信流程。

9. 什么是粘包？ socket 中造成粘包的原因是什么？ 哪些情况会发生粘包现象？

10. IO多路复用的作用？

11. 什么是防火墙以及作用？

12. select、poll、epoll 模型的区别？

13. 简述 进程、线程、协程的区别 以及应用场景？

14. 什么是GIL锁？

15. Python中如何使用线程池和进程池？

16. threading.local的作用？

17. 进程之间如何进行通信？

18. 什么是并发和并行？

19. 解释什么是异步非阻塞？

20. 路由器和交换机的区别？

21. 什么是域名解析？

22. 如何修改本地hosts文件？

23. 生产者消费者模型应用场景？

24. 什么是cdn？

25. 程序从Flag A执行到Flag B的时间大致为多少秒

    ```python
    import threading
    import time
    def _wait():
        time.sleep(60)
    #FlagA
    t = threading.Thead(target=_wait, daemon=False)
    t.start()
    #FlagB
    ```

26. 有A.txt和B.txt 两个文件, 使用多进程和进程池的方式分别读取这两个文件

27. 以下那些是常见的TCP Flags?(多选)

   ```
   A.  SYN
   B.  RST
   C.  ACK
   D.  URG
   ```

28. 下面关于网络七层和四层的描述, 那条是错误的?

    ```
    A.  SNMP工作在四层
    B.  四层是指网络的传输层, 主要包括IP和端口信息
    C.  七层是指网络的应用层(协议层), 比如http协议就工作在七层
    D.  四层主要应用于TCP和UDP的代理, 七层主要应用于HTTP等协议的代理
    ```

29. tracerroute 一般使用的是那种网络层协议

    ```
    A.  VRRP
    B.  UDP
    C.  ARP
    D.  ICMP
    ```

30. iptables知识考察, 根据要求写出防火墙规则?

    ```
    A.  屏蔽192.168.1.5访问本机dns服务端口
    B.  允许10.1.1.0/24访问本机的udp 8888 9999端口
    ```

31. 业务服务器192.168.1.2访问192.168.1.3数据接口, 无法正常返回数据, 请根据以上信息写出排查思路。

32. 请实现一个简单的socket编程, 要求

    ```
    1.  实现server端的功能即可
    2.  遵循基本语言编程规范
    ```

33. 谈一下对于多线程编程的理解, 对于CPU密集型怎样使用多线程, 说说线程池, 线程锁的用法, 有没有用过multiprocessing或concurrent.future？

34. 关于守护线程的说法, 正确的是

    ```
    A.  所有非守护线程终止, 即使存在守护线程, 进程运行终止
    B.  所有守护线程终止, 即使存在非守护线程, 进程运行终止
    C.  只要有守护线程或者非守护线程其中之一存在, 进程就不会终止
    D.  只要所有的守护线程和非守护线程中终止运行之后, 进程才会终止
    ```

35. TCP协议在每次建立或者拆除连接时, 都要在收发双方之间交换()报文

    ```
       一个
       两个
       三个
       四个
    ```

36. 描述多进程开发中join与deamon的区别

37. 请简述GIL对Python性能的影响

38. 曾经在哪里使用过：线程、进程、协程？

39. 请使用yield实现一个协程？

40. 请使用python内置async语法实现一个协程？

41. 简述线程死锁是如何造成的？如何避免？

42. asynio是什么？

43. gevent模块是什么？

44. 什么是twisted框架？

45. 什么是LVS？

46. 什么是Nginx？

47. 什么是keepalived?

48. 什么是haproxy？

49. 什么是负载均衡？

50. 什么是rpc及应用场景？

51. 什么是反向代理？

52. 什么是正向代理？

# 第六章 数据库和缓存
1. 列举常见的关系型数据库和非关系型都有那些？

2. MySQL常见数据库引擎及区别？

3. 简述事务及其特性？ 

4. 简述触发器、函数、视图、存储过程？ 

5. MySQL索引种类

6. 索引在什么情况下遵循最左前缀的规则？

7. MySQL常见的函数？

8. 列举 创建索引但是无法命中索引的情况。

9. 数据库导入导出命令（结构+数据）？

10. 你了解那些数据库优化方案？

11. char和varchar的区别？

12. 简述MySQL的执行计划的作用及使用方法？

13. 1000w条数据，使用limit offset 分页时，为什么越往后翻越慢？如何解决？

14. 什么是索引合并？

15. 什么是覆盖索引？

16. 简述数据库读写分离？

17. 简述数据库分库分表？（水平、垂直）

18. 数据库锁的作用？

19. where子句中有a,b,c三个查询条件, 创建一个组合索引abc(a,b,c)，以下哪种会命中索引

    ```
    (a)
    (b)
    (c)
    (a,b)
    (b,c)
    (a,c)
    (a,b,c)
    ```

20. mysql下面那些查询不会使用索引

    ```
    between, like "c%" , not in, not exists, !=, <, <=, =, >, >=,in
    ```

21. mysql中varchar与char的区别以及varchar(50)中的50代表的含义

22. 请简述项目中优化sql语句执行效率的方法

23. 从delete语句中省略where子句, 将产生什么后果?

    ```
    A.  delete语句将失败因为没有记录可删除
    B.  delete语句将从表中删除所有的记录
    C.  delete语句将提示用户进入删除的标准
    D.  delete语句将失败,因为语法错误
    ```

24. 叙述mysql半同步复制原理

25. sql查询

    存在的表有

    ```
    1.  products(商品表)    columns 为 id, name, price
    2.  orders(商城订单表) columns 为id, reservation_id, product_id, quentity(购买数量)
    3.  reservations(酒店订单表) columns 为id,user_id, price, created
    ```

    需要查询的:

    ```
    1.  各个商品的售卖情况, 需要字段 商品名 购买总量 商品收入
    2.  所有用户在2018-01-01至2018-02-01下单次数, 下单金额, 商城下单次数, 商城下单金额
    3.  历月下单用户数: 下单一次用户数, 下单两次用户数, 下单三次及以上用户数
    ```

26. 考虑如下表结构, 写出建表语句

    ```
    ID(自增主键)      NAME(非空)               Balance(非空)
    1                     A                      19.50
    2                     A                      20.50
    3                     A                      100.00
    ```

27. 假设学生Students和教师Teachers关系模型如下所示

    ```
    1.  Student:(学号,姓名,性别,类别,身份证号)
    2.  Teacher:(教师号,姓名,性别,身份证号,工资)
    
    其中,学生关系中的类别分别为"本科生"和"研究生两类", 性别分为"男"和"女"两类.
    
    查询研究生教师平均工资(显示为平均工资), 最高工资与最低工资之间的差值(显示为差值)的SQL语句
    
    select (1) as 平均工资, (2) as 差值 from Students,Teacher where (3);
    
    查询工资少于10000元的女研究生教师的身份证号和姓名的SQL语句(非嵌套查询方式);
    
    select 身份证号,姓名 from Students where (4) (5)
    
    select 身份证号,姓名 from Teachers where (6)
    ```

28. mysql中怎么创建索引？

29. 请简述sql注入的攻击原理及如何在代码层面防止sql注入？

30. 使用Python实现将数据库的student表中提取的数据写入db.txt？

31. 简述left join和right join的区别？

32. 索引有什么作用,有那些分类, 有什么好处和坏处？

33. 写sql语句

    ```
    tableA
    id  name  kecheng fenshu
    1  张三    语文         81
    2  张三    数学         75
    3  李四    语文         76
    4  李四    数学         90
    5  王五    语文         81
    6  王五    数学         100
    7  王五    英语         90
    tableB
    	id name
        1  张三
        2  李四
        3  王五
        4  赵六
    查询:
    1.  查询出每门课程都大于80分的学生姓名
    2.  查询出语文成绩醉的大学生姓名
    3.  查询没有成绩的学生姓名
    ```

34. 试列出至少三种目前流行的大型关系型数据库的名称

    ```
    试列出至少三种目前流行的大型关系型数据库的名称
    其中您最熟悉的是
    什么时候开始使用
    ```

35. 数据库查询

    ```
    有表List, 共有字段a,b,c. 类型都是整数, 表中有如下几条记录
    
    1.  a    b    c
    2.  2    7    9
    3.  5    6    4
    4.  3    11   9
    
    现在对该表依次完成一下操作
    
    1.  查询出b和c列的值, 要求按b列的升序排列
    2.  写入一条新的记录, 值为(7,9,8)
    3.  查询c列,要求消除重复的值,按降序排列
    ```

36. 用一条sql语句查询出每门课程都大于80分的学生姓名. 表score如下:

    ```
    name  kechegn      fenshu
    
    张三     语文         81
    
    张三     数学         75
    
    李四     语文         76
    ```

37. 设计表, 关系如下: 教师, 班级, 学生, 科室. 科室与教师为一对多关系, 教师与班级为多对多关系, 班级与学生为一对多关系, 科室中需体现层级关系

    ```
    1.  写出各张表的逻辑字段
    2.  根据上述关系表
        1.  查询教师id=1的学生数
        2.  查询科室id=3的下级部门数
        3.  查询所带学生最多的教师的id
    
    ```

38. 有staff表,字段为主键Sid,姓名Sname,性别Sex(值为"男"或"女"),课程表Course,字段为主键Cid,课程名称Cname,关系表SC_Relation,字段为Student表主键Sid和Course表主键Cid,组成联合主键,请用SQL查询语句写出查询所有选"计算机"课程的男士的姓名

39. 什么是MySQL慢日志？

40. 数据库题（要求写出逻辑字段）

    ```
    1. 写出建表语句完成如下操作，列名自由定义(id自增)：
    	新建 A，B，C三张表；
    	A表自关联；
    	A、B表为 1:n表；
    	B、C表为 m:n 表
    2. 写出插入语句完成如下操作：
    	在C表中插入记录c1，并使其关联B表中 id为1和2的两条记录。
    3. 写出删除语句完成如下操作：
    	删除A表中的记录 a1(id=1)，并级联删除 A、B、C表中的其他相关记录。
    4. 写出查询语句完成如下操作(3条SQL)：
    	A表中存在记录a2(id=2)，分别查询 A、B、C表中与a2相关联的记录数据。
    ```

41. 在对name做了唯一索引前提下，简述以下区别：  

    ```
    select * from tb where name = ‘Oldboy-Wupeiqi’
    select * from tb where name = ‘Oldboy-Wupeiqi’ limit 1
    ```

42. redis和memcached的区别？

43. 如何高效的找到redis中所有以oldboy开头的key？

44. 什么是一致性哈希？

45. redis是单进程单线程的吗？

46. redis中数据库默认是多少个db 及作用？

47. 如果redis中的某个列表中的数据量非常大，如果实现循环显示每一个值？

48. redis如何实现主从复制？以及数据同步机制？

49. redis中的sentinel的作用？

50. 如何实现redis集群？

51. redis中默认有多少个哈希槽？

52. 简述redis的有哪几种持久化策略及比较？

53. 列举redis支持的过期策略。

54. MySQL 里有 2000w 数据，redis 中只存 20w 的数据，如何保证 redis 中都是热点数据？

55. 写代码，基于redis的列表实现 先进先出、后进先出队列、优先级队列。

56. 如何基于redis实现消息队列？

57. 如何基于redis实现发布和订阅？

58. 什么是codis？

59. 什么是twemproxy？

60. redis如何实现事务。

61. redis中的watch的命令的作用？

62. 简述redis分布式锁和redlock的实现机制。

63. 请设计一个商城商品计数器的实现方案？

# 第七章 前端

1. JavaScript(或jQuery)如何选择一个id为main的容器

2. JavaScript(或jQuery)如何选择一个class为menu的容器

3. 简述什么是浏览器时间流

4. 用css如何隐藏一个元素

5. 一行css实现padding上下左右分别为1px, 2px,3px, 4px

6. 前后端分离的基本原理。

7. 前后端分离的通信数据安全

8. 给ul设置样式为:背景色黑色,给ul下的ui设置样式为: 宽度30px, 背景红色

9. 用bootstrap写一个响应式栅格, 一个页面分左右两栏, 大屏情况下分6/6, 小屏情况下分为12/12 (大屏: 屏幕>=992px, 小屏;992px>=屏幕>=768px)

10. 写一个正则表达式获取HTML源码中的编码, 如下的编码是;utf-8怎么通过Python的热模块获得?

    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>404</title>
    </head>
    ```

11. 如何创建响应式布局？

12. 你曾经使用过哪些前端框架？

13. 什么是ajax请求？并使用jQuery和XMLHttpRequest对象实现一个ajax请求。

14. 如何在前端实现轮训？

15. 如何在前端实现长轮训？

16. vuex的作用？

17. vue中的路由的拦截器的作用？

18. axios的作用？

19. 列举vue的常见指令。

20. 简述jsonp及其原理？

21. 简述cors及其原理？

22. 看javascript代码写结果：

    ```javascript
    var name = '武沛齐';
    function func(){
    	var name = 'alex';
        function inner(){
            console.log(name);
        }
        return inner;
    }
    var ret = func();
    ret()
    ```

23. 看javascript代码写结果：

    ```javascript
    function main(){
        if(1==1){
            var name = "武沛齐";
        }
        console.log(name);
    }
    ```

24. 看javascript代码写结果：

    ```javascript
    var name = "武沛齐";
    function func(){
        var name = "alex";
        function inner(){
            var name = "老男孩";
            console.log(name);
        }
        return inner();
    }
    func();
    ```

25. 看javascript代码写结果：

    ```javascript
    function func(){
        console.log(name);
        var name = "武沛齐";
    }
    ```

26. 看javascript代码写结果：

    ```javascript
    var name = "武沛齐";
    function Foo(){
        this.name = "alex"；
        this.func = function(){
            console.log(this.name);
        }
    }
    var obj = new Foo();
    obj.func();
    ```

27. 看javascript代码写结果：

    ```javascript
    var name = "武沛齐";
    var info = {
        name: 'alex';
        func:function(){
            console.log(this.name);
            (function(){
    	        console.log(this.name);
            })()
        }
    }
    info.func();
    ```

28. 看javascript代码写结果：

    ```javascript
    var name = "武沛齐";
    var info = {
        name: 'alex';
        func:function(){
            console.log(this.name);
            var that = this;
            (function(){
    	        console.log(that.name);
            })()
        }
    }
    info.func();
    ```



# 第八章 django

1. 简述http协议及常用请求头。

2. 列举常见的请求方法。

3. 列举常见的状态码。

4. http和https的区别？

5. 简述websocket协议及实现原理。

6. django中如何实现websocket？

7. Python web开发中, 跨域问题的解决思路是?

8. 请简述http缓存机制。

9. 谈谈你所知道的Python web框架。

10. Http和Https的区别？

11. django、flask、tornado框架的比较？

12. 什么是wsgi？

13. 列举django的内置组件？

14. 简述django下的(內建的)缓存机制

15. django中model的SlugField类型字段有什么用途

16. django中想要验证表单提交是否格式正确需要用到form中的那个方法

    ```
    A.  form.save()
    B.  form.save(commit=False)
    C.  form.verify()
    D.  form.is_valid()
    ```

17. django常见的线上部署方式有哪几种？

18. django对数据查询结果排序怎么做, 降序怎么做？

19. 下面关于http协议中的get和post方式的区别, 那些是错误的?(多选)

    ```
    A.  他们都可以被收藏, 以及缓存
    B.  get请求参数放在url中
    C.  get只用于查询请求, 不能用于数据请求
    D.  get不应该处理敏感数据的请求
    ```

20. django中使用memcached作为缓存的具体方法? 优缺点说明?

21. django的orm中如何查询 id 不等于5的元素？

22. 使用Django中model filter条件过滤方法,把下边sql语句转化成python代码

    ```
    select * from company where title like "%abc%" or mecount>999
    order by createtime desc;
    ```

23. 从输入http://www.baidu.com/到页面返回, 中间都是发生了什么？

24. django请求的生命周期？

25. django中如何在model保存前做一定的固定操作,比如写一句日志？

26. 简述django中间件及其应用场景？

27. 简述django FBV和CBV？

28. 如何给django CBV的函数设置添加装饰器？

29. django如何连接多个数据库并实现读写分离？

30. 列举django orm 中你了解的所有方法？

31. django中的F的作用？

32. django中的Q的作用？

33. django中如何执行原生SQL？

34. only和defer的区别？

35. select_related和prefetch_related的区别？

36. django中filter和exclude的区别

37. django中values和values_list的区别？

38. 如何使用django orm批量创建数据？

39. django的Form和ModeForm的作用？

40. django的Form组件中，如果字段中包含choices参数，请使用两种方式实现数据源实时更新。

41. django的Model中的ForeignKey字段中的on_delete参数有什么作用？

42. django中csrf的实现机制？

43. django如何实现websocket？

44. 基于django使用ajax发送post请求时，有哪种方法携带csrf token？

45. django缓存如何设置？

46. django的缓存能使用redis吗？如果可以的话，如何配置？

47. django路由系统中name的作用？

48. django的模板中filter、simple_tag、inclusion_tag的区别？

49. django-debug-toolbar的作用？

50. django中如何实现单元测试？

51. 解释orm中 db first 和 code first的含义？

52. django中如何根据数据库表生成model类？

53. 使用orm和原生sql的优缺点？

54. 简述MVC和MTV

55. django的contenttype组件的作用？

56. 使用Django中model filter条件过滤方法,把下边sql语句转化成python代码

    ```
    select * from company where title like "%abc%" or mecount>999
    order by createtime desc;
    ```


# 第九章 Flask

1. 请手写一个flask的 Hello World。

2. Flask框架的优势？

3. Flask框架依赖组件？

4. Flask蓝图的作用？

5. 列举使用过的Flask第三方组件？

6. 简述Flask上下文管理流程?

7. Flask中的g的作用？

8. 如何编写flask的离线脚本？

9. Flask中上下文管理主要涉及到了那些相关的类？并描述类主要作用？

10. 为什么要Flask把Local对象中的的值stack 维护成一个列表？

11. Flask中多app应用如何编写？

12. 在Flask中实现WebSocket需要什么组件？

13. wtforms组件的作用？

14. Flask框架默认session处理机制？

15. 解释Flask框架中的Local对象和threadinglocal对象的区别？

16. SQLAlchemy中的 session和scoped_session 的区别？

17. SQLAlchemy如何执行原生SQL？

18. ORM的实现原理？

19. DBUtils模块的作用？

20. 以下SQLAlchemy的字段是否正确？如果不正确请更正.

21. SQLAchemy中如何为表设置引擎和字符编码？

22. SQLAchemy中如何设置联合唯一索引？

23. 简述tornado框架特点及应用场景。 


# 第十章 tornado

1. tornado中的gen.coroutine的作用？

2. tornado框架中Future对象的作用？

3. tornado框架中如何编写webSocket程序？

4. tornado中静态文件是如何处理的？

5. tornado操作MySQL使用的模块？

6. tornado操作redis使用的模块？

7. ni 

# 第十一章 api

1. 什么是webservice？

2. 什么是rpc？

3. 谈谈你对restfull 规范的认识？

4. 什么是接口的幂等性？

5. 为什么要使用django rest framework框架？

6. django rest framework框架中都有那些组件？

7. 使用django rest framework框架编写视图时都继承过哪些类？

8. django rest framework框架如何对Queryset进行序列化？

9. 简述 django rest framework框架的认证流程。

10. django rest framework如何实现的用户访问频率控制？（匿名用户和注册用户）  


# 第十二章 git

1. 你在公司如何做的协同开发？

2. git常见命令。

3. 简述以下git中stash命令作用以及相关其他命令。

4. git 中 merge 和 rebase命令 的区别。

5. 公司如何基于git做的协同开发？

6. 如何基于git实现代码review？

7. git如何实现v1.0 、v2.0 等版本的管理？

8. 什么是gitlab？

9. github和gitlab的区别？

10. 如何为github上牛逼的开源项目贡献代码？

11. git中 .gitignore文件的作用?

# 第十三章 爬虫

1. 写出在网络爬取过程中, 遇到防爬问题的解决办法。

2. 如何提高爬虫的效率？

3. 你的爬虫 爬取的数据量有多少?

4. 列举您使用过的python网络爬虫所用到的模块。

5. 简述 requests模块的作用及基本使用？

6. 简述 beautifulsoup模块的作用及基本使用？

7. 简述 seleninu模块的作用及基本使用?

8. 简述scrapy框架中各组件的工作流程？

9. 在scrapy框架中如何设置代理（两种方法）？

10. scrapy框架中如何实现大文件的下载？

11. scrapy中如何实现限速？

12. scrapy中如何实现暂定爬虫？

13. scrapy中如何进行自定制命令？

14. scrapy中如何实现的记录爬虫的深度？

15. scrapy中的pipelines工作原理？

16. scrapy的pipelines如何丢弃一个item对象？

17. 简述scrapy中爬虫中间件和下载中间件的作用？

18. scrapy-redis组件的作用？

19. scrapy-redis组件中如何实现的任务的去重？

20. scrapy-redis的调度器如何实现任务的深度优先和广度优先？


# 第十四章 算法和数据结构

1. 顺序表、链表的区别及应用场景。

2. 哈希树的构造与应用场景。

3. B Tree和B+ Tree的区别？

4. 什么是中序遍历？

5. 具有三个节点的二叉树有几种形态：

   ```
   A.  1
   B.  3
   C.  5
   D.  7
   ```

6. 无向图G中的边的集合E=[(a,b), (a,e),(a,c),(b,e),(e,d),(d,f),(f,c)], 则从顶点a出发进行深度优先遍历可以得到一种顶点序列为

   ```
   A.  aedfcb
   B.  acfebd
   C.  aebcfd
   D.  aedfbc
   ```

7. 一颗具有n个节点的平衡二叉树, 其平局查找长度为

   ```
   A.  O(1)
   B.  O(log2n)
   C.  O(n log2n)
   D.  O(n2)
   ```

8. 以下序列中不是二叉堆的是

   ```
   A.  100,86,48,73,35,39,42,57,66
   B.  12,70,33,65,92,41,40,81,75,99
   C.  103,97,56,38,89,23,45,10,37,52,6
   D.  7,32,10,53,90,27,41,70,61,82
   ```

9. 快速排序按排序思想分类属于

   ```
   A.  基数排序
   B.  选择排序
   C.  插入排序
   D.  交换排序
   ```

10. 奇偶交换排序

   ```
   如下所述: 
   	第一趟对所有奇数i ,将a[i]和a[i+1]进行比较; 
   	第二趟对所有偶数i, 将a[i]和a[i+1] 进行比较, 若a[i]>a[i+1], 则两者交换; 
   	第三趟对奇数i, 第四趟对偶数i, 以此类推, 直至整个序列有序为止. 若有初始序列为逆序, 规模为7的有序序列, 欲通过奇偶交换排序获得正序序列, 则排序过程中所需的数据交换次数为多少？
   
   A.  6
   B.  20
   C.  21
   D.  28
   ```

11. 对长度为N的线性表进行顺序查找, 在最坏情况下所需要的比较次数为

    ```
    A.  N+1
    B.  N
    C.  ( N+1)/2
    D.  N/2
    ```

12. 一直青蛙可以跳上一级台阶, 也可以跳上两级台阶, 求该青蛙跳上一个十级台阶共有多少中跳法.

    ```
    A.  15
    B.  89
    C.  144
    D.  512
    ```

13. 合并两个有序的数组, 数组都是非递减的, 合并后的数组依然有序

    ```
    class Solution:
        def merge(self, nums1, m, nums2,n)
            '''
            :type nums1:list[int]
            :type m:int
            :type nums2:list[int]
            :type n1:int
            :rtype nums:list[int]
    ```

14. 反转数字, 例子:

    输入123, 输出321; 输入-123, 输出-321; 输入1032100, 输出12301

    ```
    class Solution:
        def reversr(self,x)
            '''
            :type x:int
            :rtype :int
            '''
    ```

15. 实现一个二分查找

16. 采用递归的方式用javascrapt写一下快速排序

17. 一个数组, 找到和为n的所有数对. 如[1,7,3,5,6,2,9,5,4,8] n=11,问 数对(7,4),(2,9),(5,6)...效率尽可能高

18. 简单描述下快速排序的原理。

19. 12个大小一样的球, 其中一个的重量与其他的不一样, 如何只称三次找出这只球

20. Given a string s, find the lonest palindromic substring in s,  you may assume that the maximum length of s in 1000;

    ```
    Example:
    Input: "babad"
    Output:"bab"
    Note:"aba" is also avalid answewr
    
    Example:
    Input: "cbbd"
    Output:"bb"
    ```

21. Divide two integers without using muitiplication, division and mod operator. id it is overflow, return MAX_INT;

    ```
    For example, given:["eat", "tea","tan","ate","nat","bat"]
    return :
    [
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
    ]
    
    Note: All inputs will be in lower-case
    ```

22. 括号匹配

    Given a astring containing just the characters'(',')','{','}','[',and ']', determine if the input string is valid.

    The brackets must close in the correct order, "()" and "()[]{()}" are all valid but "(]" and "([)]"are not

23. 给定一个int list a, 满足a[i+1]>=a[i], 满足a[i+1]>=a[i], 给定int key, 找出list a中第一个大于等于key元素的index, 无满足要求的元素则返回-1

    ```
    函数定义:
    
    def findindex(int_list, int_key)
    ```

24. 假设在n进制下, 567*456=150216成立, 请问n的值是

    ```
    A.  9
    B.  12
    C.  14
    D.  18
    ```

25. 给一个链表, 将其中的节点两两交换后, 返回链表的头结点

    ```
    实例:
    给出1->2->3->4
    你的程序应该返回这样一个链表: 2->1->4->3
    注意: 不能修改链表的节点的值
    ```

26. 给定一个整数数组, 返回两个数字的索引, 使得他们相加和一个目标值相等. 可以假设每个输入都有且只有一个解 例如 数组nums = [2,7,11,15], 目标值是9 因为nums[0]+nums[1]= 2+7=9 所以返回[0,1]

27. we have a list of number

    ```
    l = [1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]
    
    we want to make a dictionary with the number of digits as the key and list of numbers the value:
    
    {1:[1,2,4,8],2:[16,32,64],3:[128,256,512],4:[1024],5:[32768],10:[4294967296]}
    ```

28. 

    ```
    for a given pair of numbers (row x column), create an array. for example, for (4,5) pair, we want to create the following 4x5 matrix:
    
    [[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8],[0,3,6,9,12]]
    ```

29. we want to define a function with a generator which can iterate the numbers, which are divisible by 7 within range(n)

30. 布尔运算

    ```
    已知x=43, ch="A",y=1, 则表达式(x>=y and ch<'B' and y)的值是
    
    1.  0
    2.  1
    3.  出错
    4.  True
    ```

31. 编程实现斐波那契数列(注:使用递归)

32. 请用自己的算法, 按升序合并如下两个list, 并去除重复元素

    ```
    list1=[2,3,8,4,9,5,6]
    list2=[5,6,10,17,11,2]
    ```

33. 现有编号分别为A,B,C,D,E的5个盒子, 某方法每次调用都输出盒子的一个编号, 输出这五个盒子的概率分别是10%, 20%, 25%, 15%, 30%,请实现该方法.

34. 填充代码

    ```
    import random
    
    def get_card(config):
        ...
        ...
    
    card_config = [['card1',10],['card2',30],['card',15]]
    card_name = get_card(card_config )
    print card_name
    ```

    ```
    现需要编写一个抽取卡牌的函数, 按照给定的权重分布来随机抽取, 输入的配置示例为[['card1',10],['card2',30],['card',15]], 其中字符串为卡牌名, 数字为权重, 返回'card1'的概率是10/(10+30+15), 请完成代码中省略的部分
    ```

35. 在数组中找到具有最大和的连续子数组(至少包含一个数字)

    ```
    例如, 给定数组[-2,1,-3,4,-1,1,1,-5,4]
    
    连续子阵列[4,-1,2,1]具有最大的sum=6
    ```

36. 算法是值

    ```
    A.  数学的计算公式
    B.  程序设计语言的语句序列
    C.  对问题的精准描述
    D.  解决问题的精准步骤
    ```

37. 斐波那契数列

    ```
    1,2,3,5,8,13
    
    求出400万以内的最大的斐波那契数, 并求出他是第几个
    ```

38. 写代码(数桃子)

    ```
    海滩上有一堆桃子, 五只猴子来分,第一只猴子把这堆桃子平均分成了五份, 多了一个, 这只猴子把多的一个扔到了海里, 拿走了一份,第二只猴子把剩下的盒子了一起,有平均分成了五分,又多了一个, 同样把多的一个扔到了海里, 拿走了一份, 第三只,第四只,第五只都是这样做的, 问海滩上原来最少是有多少桃子
    ```

39. 写程序

    ```
    上机编程实现一个小程序, 给出一个罗马数字,先判断是否是罗马数字, 如果是, 转换为阿拉伯数字,不是的话报错.本题只考虑3999以内的数
    
    I(1) V (5) X(10) L(50) C(100) D(500) M(1000)
    
    计数规则
    
    1.  若干相同数字连写表示的数是这些罗马数字的和,如III=3
    2.  小数字在大数字前面表示的数使用大数字减去小数字, 如IV=4
    3.  小数字在大数字后面表示的数是大数字加上小数字, 如VI=6
    
    组合规则:
    
    1.  基本数字I,X,C中的任何一个, 自身连用构成数目, 或者放在大数的右边连用构成数目, 都不能超过三个;放在大数的左边只能用一个
    2.  不能把基本数字V,L,D中的任何一个作为小数放在大数的左边采用相减的方式构成数目;放在大数的右边采用相加的方式构成数目,只能使用一个
    3.  V和X左边的小数字只能用I
    4.  L和C左边的小数字只能用X
    5.  D和M左边的小数字只能用C
    ```

40. 请列举出三种常用的排序算法

41. 用4,9,2,7四个数字, 用加减乘除, 和每个数字(必须且只能用一次), 使表达式结果为24

42. 一个数组的中位数定义为: 数组中元素排序后在中间位置的数, 如果数组长度为偶数, 则为中间两个数的平均数.

    ```
    请写出两个函数,分别实现:
    
    *   向数组插入新元素
    *   找出插入元素后新数组中的中位数
    
    提示: 插入新元素的方法影响找中位数的复杂度, 我们希望找减少求中位数的复杂度
    ```

43. 有一个容量为N的背包,和M个物品, 这些物品的体积可以用一个数组[a1,a2,a3...am]表示, 假设背包的容量不足以装下所有的物品, 请编程实现: 找出一个最佳的背包方案, 使得背包的空间利用率最大

44. 在一个二位坐标体系中有多个任意位置的点,请编程找出其中多有的边缘点. 边缘点的定义为在该点的右上象限内没有其他的点

45. 语言不限

    ```
    1.  链表的冒泡排序
    2.  树的顺序遍历
    3.  顺序表
    ```

     


# 第十五章 Linux

1. 下面的linux命令中, 那个不能显示出文件的内容

   ```
   A.  tac
   B.  more
   C.  head
   D.  man
   ```

2. 默认情况下管理员创建了一个用户, 就会在()目录下创建一个用户主目录

   ```
   A.  /usr
   B.  /home
   C.  /root
   D.  /etc
   ```

3. 你使用命令"vi /etc/inittab"查看该文件的内容, 你不小心改动了一些内容, 为了防止系统出问题, 你不想保存所修改的内容, 你应该如何操作

   ```
   A.  在末行模式下, 键入:q!
   B.  在末行模式下, 键入:x!
   C.  在末行模式下, 键入:wq
   D.  在末行模式下, 键入"ESC"键直接退出vi
   ```

4. 用"rm -i", 系统会提示什么来让你确认

   ```
   A.  命令行的每个选择
   B.  是否真的删除
   C.  是否有写的权限
   D.  文件的位置
   ```

5. 在CentOS7.2中, 用一句话将所有的test.py进程全部杀死

6. 在CentOS7.2中, 如何查看程序执行所消耗的CPU, 内存等硬件资源

7. 写一个Bash Shell脚本来得到当前的日期,时间, 用户名和当前的工作目录

8. 如何查看当前登录用户

9. 如何定位占用端口8080的服务

10. 如何切换用户

11. 查找/tmp/path下的以A开头的文件

12. 如有两台机器a/b, a的ip地址包括45.32.12.222, 10.10.121.22 b的ip地址包括45.32.12.226,10.10.121.69,两台机器的ssh监听端口为11111

    ```
    请写出远程登录机器a的命令
    
    请写出从a远程登录b的命令
    
    请说明从b机器访问qq.com时的详细过程, 以及到qq.com记录到的ip
    ```

13. 计划任务---如何让abc.sh每周一执行一次 若执行失败的原因是什么

14. 如何查看发往本机8080端口的流量

15. 现有一文件文件内容为ip地址及路径, 例如192.168.31.9 /tmp/destpath, 现需要将本机的hello.txt文件发送到文件记录的机器相应的目录中, 编程实现(shell)

16. 在linux中, 如何批量的删除多个Python进程

17. 下面那个函数能够在linux下创建一个子进程

    ```
    A.  os.popen
    B.  os.fork
    C.  os.system
    D.  os.link
    ```

18. 文件内容实例如下

    ```
    192.168.0.20--[0B/Sep/2015:20:05:30+0800] "GET /android/login/?method=get_server HTTP/1.1" -200 22268 "-" "-" "-" 0.055 0.139
    
    请写出命令行下(shell 默认bash), 提取请求时间($request_time) 大于0.1秒的请求($request), 并写入access_long_time.log文件中的命令
    ```

19. 你最熟悉的unix环境是?

20. 你最熟悉的unix环境是

21. unix下查询环境变量的命令是

22. 查询脚本定时任务的命令是

23. Apache服务器默认的接听连接端口号是

    ```
    A.  1024
    B.  800
    C.  80
    D.  8
    ```

24. 建立一个新文件可以使用的命令为

    ```
    A.  chmod
    B.  more
    C.  cp
    D.  touch
    ```

25. /etc/ethX表示

    ```
    A.  系统会送接口
    B.  以太网接口设备
    C.  令牌环网设备
    D.  PPP设备
    ```

26. 显示用户的ID, 以及所属组的ID, 要使用的命令是

    ```
    A.  su
    B.  who
    C.  id
    D.  man
    ```

27. 显示用户的ID, 以及所属组的ID, 要使用的命令是

    ```
    A.  su
    B.  who
    C.  id
    D.  man
    ```

28. 为了修改文件test的许可模式, 使其文件属性具有读写和运行的权限, 组和其他用户可以读和运行, 可以采用

    ```
    A.  chmod 755 test
    B.  chmod 700 test
    C.  chmod +rwx test
    D.  chmod g-w test
    ```

29. 取ls -l 输出结果的第5列的值的正确写法是

    ```
    A.  ls -l |awk "{print$5}"
    B.  ls -l |awk '{print$5}'
    C.  ls -l |awk {print$5}
    D.  ls -l |awk 'print$5'
    ```

30. 什么命令解压缩tar.gz文件

    ```
    A.  tar -czcf filename.tar.gz
    B.  tar -xzvf filename.tar.gz
    C.  tar -tzvf filename.tar.gz
    D.  tar -dzvf filename.tar.gz
    ```

31. 以下哪个命令是vi编辑器中执行存盘退出的

    ```
    A.  q
    B.  zz
    C.  :q!
    D.  :wq
    ```

32. 简述 saltstack、ansible、fabric、puppet工具的作用？

33. uwsgi和cgi的区别？

34. supervisor的作用？

35. 解释 PV、UV 的含义？

36. 解释 QPS的含义？

# 第十六章 设计题

1. 设计一个办公室摄像头的web后台管理系统

   ```
   假设功能如下:
   	1.  可以 开启关闭重启每个摄像头
   	2.  可以调整摄像头的方向
   	3.  可以设置摄像头每天的工作时间
   	4.  后台可以查看每个摄像头的历史录像, 并且可以删除, 设置保存最大保存时间
   	5.  后台可以随时查看实时监控
   
   要求:
   	1.  设计系统架构, 考虑全系统无单点, 画出设计图, 标出所需选用的所有技术和所有组件及关系
   	2.  设计系统数据结构, 设计一套基于mysql的数据库表
   	3.  API设计, 写出符合以上功能的所有用户API及主要的内部工程逻辑
   	4.  设计用户和权限系统, 考虑只有两种角色即可, 一种是普通用户只有功能5, 也就是只能看实时录像, 另一个是管理员可以拥有1-5的全部功能权限
   ```

2. 编写一个脚本, 5分钟检查一次日志, 发现有暴力ssh破解现象的, 提取此类ip地址, 并去重, 并按降序排序。

   ```
   要求:
   
   1.  同一个ip暴力破解超过10次, 自动屏蔽IP地址
   2.  指定办公室ip地址(192.168.100.100)为可信任ip地址, 不受屏蔽规则限制, 以下为日志格式
   
   日志样板如下:
   
   May 4 03;43:07 tz-monitor sshd[14003]: Failed password for root from 124.232.135.84 port 25251 ssh2
   
   May 4 03:43:07 tz-monitor sshd[14082]: Invalid user postgres from 124.232.135.84
   ```

3. 一个文本文件,大约有一万行, 每行一个词, 要求统计出其中最频繁的前10个词, 请给出设计思路。

4. 请为公司设计一个并发处理key-value引擎, 要求每条请求的数据小于16k, 数据总量为1T,QPS为50。

   ```
   要求:
   1.  请给出该系统需要配备多少资源, 服务其数量, 服务器内存大小及硬盘空间等
   2.  要求系统平滑可扩展
   3.  尽可能的降低系统复杂度
   ```

5. 请设计秒杀系统, 大并发下如何不会超卖？

6. 如果有一个订单系统,包含订单信息,商品信息, 价格信息,并且要记录那些状态, 在设计系统时, 你会提供那些建议？

7. 现在要开发一款游戏, 根据游戏的分数做出这款游戏的用户排名, 用户信息可以通过第三方接口获取, 用户的好友信息可以通过第三方获取. 游戏排名分为世界排名和好友排名..(参考例子跳一跳) 请简要设计数据库模型。

8. 写代码

   ```
   有一个3G大小的文件, 文件每行一个string, 内容为酒店的id和一个图片的名字, 使用"\t"分割示例,ht_1023134+"\t"+hiadwqerscnsdjkfhwe.jpg
   
   表示的是一个酒店包含的一张图片, 统计含有图片数量为[20,无穷大]的酒店的id, 含有图片数量范围[10,20]的酒店id, 含有图片数量为[5,10]的酒店的id,图片数量为[0,5]的酒店的id, 并将结果输出到文件中
   
   文件格式:
   
   0-5+"\t"+id1+"\t"+id2
   
   5-10+"\t"+id1+"\t"+id2
   
   10-20+"\t"+id1+"\t"+id2
   
   20-无穷大+"\t"+id1+"\t"+id2
   ```

9. 现在小明一家过一座桥, 过桥时是黑夜, 所以必须有灯. 现在小明过桥要1秒, 小明的弟弟要三秒, 小明的爸爸要6秒, 小明的妈妈要8秒, 小明的爷爷要12秒, 而过桥的时间依过桥最慢者而定, 而且等在点然后36秒就会熄灭, 问小明一家如何过桥。


# 第十七章 客观题

1. 请列举最近关注的一些技术？

2. 请列举你认为不错的一些技术书籍和你最近再看的书籍(不限于技术)？

3. 请列举你阅读过源码的一些项目？

4. 请给出你对这份笔试题的看法？

5. 作为项目负责人的你, 你应该要做那些除编码外的工作来更快的推动项目开发？

6. 请列举经常访问的计数网站或博客

7. 对您最有影响的或是您认为最有价值的软件方面的几本书。

8. 在软件开放方面, 您最擅长的是

   ```
   1.  管理
   2.  需求分析
   3.  系统分析
   4.  设计
   5.  代码
   6.  测试
   7.  软件工程
   ```

9. 在中国东北有这样两个存款, 赵村所有的村民都是白天祭祀祖先, 而李庄的人都是晚上祭祀祖先, 能肯定的没人在白天和晚上都祭祀祖先的. 我么也知道李明是晚上祭祀祖先的人, 那么以下哪个选项是正确的

   ```
   A.  李明是赵村的人
   B.  李明不是赵村的人
   C.  李明是李庄的人
   D.  李明不是李庄的人
   E.  李明既不是李庄的人也不是赵庄的人
   ```

10. 相传在古时候某国的国民都分别居住在两个怪城里, 一座真城, 一座假城, 真城的人各个都说真话, 假城的人各个都说假话, 一位知道情况的外国游客来到其中一个城市, 他只问了一个问题就知道自己来到的是哪个城了, 下面那句话最恰当

  ```
  A.  你是真城人吗
  B.  你是假城人吗
  C.  你是说真话的人吗
  D.  你是说假话的人吗
  E.  你是这个城市的人吗
  ```

11. 设'并非无奸不商'为真, 则下面哪一个选项一定为真

    ```
    A.  所有商人都是奸商
    B.  所有商人都不是奸商
    C.  并非所有商人不是奸商
    D.  并非所有商人是奸商
    E.  有的商人不是奸商
    ```

12. 小赵比小钱个子高: 小孙不如小李个子高,; 小李个子不如小周高; 小钱和小周个子正好一样高.如果上面这些陈述都是对的, name下列哪个选项是对的

    ```
    A.  小孙比小周个子高
    B.  小孙比小赵个子高
    C.  小钱比小孙个子矮
    D.  小赵比小李个子高
    E.  小钱比小李个子矮
    ```

# 第十八章 其他

1. 什么是rpc？
2. 简述 RabbitMQ、Kafka、ZeroMQ的区别？
3. RabbitMQ如果在消费者获取任务后未处理完前就挂掉时，保证数据不丢失？
4. RabbitMQ如何对消息做持久化？
5. RabbitMQ如何控制消息被消费的顺序？
6. 以下RabbitMQ的exchange type分别代表什么意思？如：fanout、direct、topic。
7. 简述 celery 是什么以及应用场景？
8. 简述celery运行机制。
9. celery如何实现定时任务？
10. 简述 celery多任务结构目录？
11. celery中装饰器 @apptask 和 @shared_task的区别？
12. 谈谈你们公司的上线流程？
13. 公司用的什么做的bug管理？

