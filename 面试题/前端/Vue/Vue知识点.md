#  Vue知识点   老杜 p178

~~~html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div id="app1">
        <h2>aaaa</h2>
        <!-- <h2>{{ a }}</h2> -->
        <template id="tem">
            <h1 >temmmm</h1>
        </template>
    </div>
    <script src='../js/vue.js'></script>
    <script>
        const app = new Vue({
            // template: '<h1>数据来源：{{c[1]}}--=={{d.d1}}</h1>',
            template: '#tem',
            data: {
                a: '12345',
                b: "我是主",
                c: [1,2,3,4,5],
                d:{
                    d0: 'hah',
                    d1: 'ddd',
                    d2: 'cdfads',

                }
            }
        })
        app.$mount('#app1')
    </script>
</body>

</html>
~~~



## v-bind v-model

![image-20230605235354000](Vue知识点.assets/image-20230605235354000.png)



## Vue实例

![image-20230606073430089](Vue知识点.assets/image-20230606073430089.png)



## Object.defineProperty

![image-20230606074835961](Vue知识点.assets/image-20230606074835961.png)

![image-20230606075231428](Vue知识点.assets/image-20230606075231428.png)



**注意：这样会出现死循环，访问color会一直调用get方法，给color赋值也会一直调用set方法()**

![image-20230606075249192](Vue知识点.assets/image-20230606075249192.png)

![image-20230606075327843](Vue知识点.assets/image-20230606075327843.png) 

+ 解决方法--使用temp变量

  ![image-20230606075357834](Vue知识点.assets/image-20230606075357834.png)



## 数据代理机制的实现

![image-20230606080148506](Vue知识点.assets/image-20230606080148506.png)

![image-20230606080431181](Vue知识点.assets/image-20230606080431181.png)

### 这就是Vue可以通过 vm.target访问到值的原因---使用了动态数据代理

![image-20230606080714008](Vue知识点.assets/image-20230606080714008.png)

![image-20230606080834555](Vue知识点.assets/image-20230606080834555.png)

## Vue框架源代码解读

![image-20230606233021854](Vue知识点.assets/image-20230606233021854.png)

![image-20230606233107052](Vue知识点.assets/image-20230606233107052.png)



**如果程序员不想使用代理访问data,不推荐使用vm._data直接访问data里的数据，一般使用 vm.$data**





## 关于degfineProperty配置项

+ configurable

+ enumerable

  ![image-20230607071048882](Vue知识点.assets/image-20230607071048882.png)





## v-on:click    == @click

 ![image-20230607073845748](Vue知识点.assets/image-20230607073845748.png)

![image-20230607074000611](Vue知识点.assets/image-20230607074000611.png)

![image-20230607074031285](Vue知识点.assets/image-20230607074031285.png)







## this

+ 使用普通函数 this == vm

+ 箭头函数没有this

![image-20230607080757275](Vue知识点.assets/image-20230607080757275.png)

![image-20230607075551479](Vue知识点.assets/image-20230607075551479.png)



## methods实现原理

![image-20230607080643242](Vue知识点.assets/image-20230607080643242.png)





## 事件修饰符

+ self
+ stop
+ capture
+ once
+ prevent
+ passive 

 ![image-20230607220437140](Vue知识点.assets/image-20230607220437140.png)

![ ](Vue知识点.assets/image-20230607220602660.png)





## 按键修饰符

 ![image-20230607221918116](Vue知识点.assets/image-20230607221918116.png)





## 计算属性  - computed

![image-20230607231410668](Vue知识点.assets/image-20230607231410668.png)

![image-20230607231152694](Vue知识点.assets/image-20230607231152694.png)

+ 简写形式

  ![image-20230607231226498](Vue知识点.assets/image-20230607231226498.png)





## 监视---watch

![image-20230607232006631](Vue知识点.assets/image-20230607232006631.png)





### 深度监视

![image-20230608223329380](Vue知识点.assets/image-20230608223329380.png)

### 后期添加监视

![image-20230608223639192](Vue知识点.assets/image-20230608223639192.png)



### 简写形式省略handler(没有其他参数的情况，只有handler)

![image-20230608223911601](Vue知识点.assets/image-20230608223911601.png)



### 后期添加监视简写形式

![image-20230608224028495](Vue知识点.assets/image-20230608224028495.png)

![image-20230609071654408](Vue知识点.assets/image-20230609071654408.png)



## watch和computed如何选择

![image-20230609203435470](Vue知识点.assets/image-20230609203435470.png)

![image-20230609203525219](Vue知识点.assets/image-20230609203525219.png)





## class绑定之数组和对象形式

![image-20230609211427267](Vue知识点.assets/image-20230609211427267.png)





## v-if和v-show选择

![image-20230609223745443](Vue知识点.assets/image-20230609223745443.png)





## v-for

![image-20230609224145214](Vue知识点.assets/image-20230609224145214.png)





## diff算法和列表过滤

![image-20230615233223967](Vue知识点.assets/image-20230615233223967.png)







## V-model大全集

### 表单提交

![image-20230617071256671](Vue知识点.assets/image-20230617071256671.png)



### 对象转为json字符串

![image-20230617073233981](Vue知识点.assets/image-20230617073233981.png)





## filters

![image-20230617235915876](Vue知识点.assets/image-20230617235915876.png)

### 全局变量

![image-20230618000104603](Vue知识点.assets/image-20230618000104603.png)





## v-cloak  -避免延迟显示

![image-20230618093330135](Vue知识点.assets/image-20230618093330135.png)





## 自定义指令

![image-20230618104300629](Vue知识点.assets/image-20230618104300629.png)







## 响应式与数据劫持

![image-20230618144305900](Vue知识点.assets/image-20230618144305900.png)    

![image-20230618144129097](Vue知识点.assets/image-20230618144129097.png)







# Vue生命周期

![image-20230618161121686](Vue知识点.assets/image-20230618161121686.png)   

![image-20230618161159073](Vue知识点.assets/image-20230618161159073.png)





## 初始阶段：虚拟DOM生成

![image-20230618213655838](Vue知识点.assets/image-20230618213655838.png)

![image-20230618213829841](Vue知识点.assets/image-20230618213829841.png)





## 挂载阶段：真实DOM生成 

![image-20230618214951426](Vue知识点.assets/image-20230618214951426.png)





## 更新阶段：data变化重新渲染

![image-20230618222038577](Vue知识点.assets/image-20230618222038577.png)



## 销毁阶段：卸载所有，销毁vm

+ vm空间还在

![image-20230618222650086](Vue知识点.assets/image-20230618222650086.png)

![image-20230619072700969](Vue知识点.assets/image-20230619072700969.png)

![image-20230619072920367](Vue知识点.assets/image-20230619072920367.png)

![image-20230619073032957](Vue知识点.assets/image-20230619073032957.png)

![image-20230619073212806](Vue知识点.assets/image-20230619073212806.png)

![image-20230619073224230](Vue知识点.assets/image-20230619073224230.png)







# 组件化开发

![image-20230619074448004](Vue知识点.assets/image-20230619074448004.png) 



## 组件的使用

### 局部组件定义和使用

+ 三步

![image-20230620072139673](Vue知识点.assets/image-20230620072139673.png)





### 全局组件注册

Vue.component("组件名", "定义的组件变量")

![image-20230620073301703](Vue知识点.assets/image-20230620073301703.png)



### 小细节：

+ 在Vue当中是可以使用自闭合标签的，但是前提必须在脚手架环境中使用

+ 在创建组件的时候Vue.extend（）是可以省略，但是底层实际上还是会调用，在注册组件的时候会调用

+ 组件的名字

  - 第一种：全部小写
  - 第二种：首字母大写，后面都是小写
  - 第三种：kebab-case命令发（user-login)
  - 第四种：UserLogin-------但这种方式只允许在脚手架环境中使用

  - 在创建组件的时候，通过配置项配置一个name, 这个name不是组件的名字，是设置Vue开发着工具中显示的组件的名字



## 组件的嵌套

![image-20230620080756466](Vue知识点.assets/image-20230620080756466.png)

![image-20230620080858168](Vue知识点.assets/image-20230620080858168.png)





## vc和vm

![image-20230621075958671](Vue知识点.assets/image-20230621075958671.png) 

![image-20230621080134004](Vue知识点.assets/image-20230621080134004.png)







## 补充：原型和原型链

+ 显示原型属性和隐式原型属性

  ![image-20230623190700605](Vue知识点.assets/image-20230623190700605.png)

  ~~~javascript
  // 原型对象只有一个，其实原型对象都是共享的
  
  console.log(x === y) // true
  
  // 这个不是给Vip扩展属性
  // 是在给Vip的原型对象扩展属性
  Vip.prototype.counter = 1000
  
  // 通过a实例可以访问这个扩展的cunter属性吗？ 可以访问，为什么 原理是啥
  // 访问原理：首先去a实例去找counter属性，如果a实例上没有counter属性的话，会沿着__proto__ 这个原型对象去找
  console.log(a.counter) // 1000
  
  console.log(a.__prototype__.counter) // 1000
  ~~~

  

![image-20230623190754976](Vue知识点.assets/image-20230623190754976.png)





### 组件能访问counter

+ Vue.prototype.counter = 1000
+ 原因：

![image-20230623193242782](Vue知识点.assets/image-20230623193242782.png)

~~~javascript
console.log(user.prototype.__proto__ === Vue.prototype)  // true
~~~

![image-20230623194228193](Vue知识点.assets/image-20230623194228193.png)





+ 组件化开发

  ![image-20230623222120422](Vue知识点.assets/image-20230623222120422.png)





# 脚手架vue-cli

![image-20230623230758337](Vue知识点.assets/image-20230623230758337.png)

+ index.html   ---vue脚手架会自动导入main.js

  ![image-20230623234526843](Vue知识点.assets/image-20230623234526843.png)

+ main.js    这里等同于引入vue.js文件

  ![image-20230623234858809](Vue知识点.assets/image-20230623234858809.png)

+ App.vue组件

  ![image-20230623235027787](Vue知识点.assets/image-20230623235027787.png)





+ **为什么使用render**

  ![image-20230624001326503](Vue知识点.assets/image-20230624001326503.png)

  - **方案一：使用完整版的vue**

    ![image-20230624001216857](Vue知识点.assets/image-20230624001216857.png)

  + **方案2： render函数  es6语法 render: h => h(App)         h变量实际是一个创建元素的函数，传入App组件，单行不需要写return语句**

    ![image-20230624001621550](Vue知识点.assets/image-20230624001621550.png)



# props属性使用 ---父串子

+ 组件传参，子级使用

+ 避免直接更改prop，因为每当父组件重新渲染时，该值都会被覆盖

+ 不要修改prop中的数据

  ![image-20230624084347381](Vue知识点.assets/image-20230624084347381.png)



# ref -从父组件中获取子组件

+ 可以获取dom元素和组件，近而获得元素里的属性

  ![image-20230624085911498](Vue知识点.assets/image-20230624085911498.png)





# mixins混入

+ **当和methods冲突时，methods里的方法优先生效**

  ![image-20230624092840234](Vue知识点.assets/image-20230624092840234.png)

  ![image-20230624092723773](Vue知识点.assets/image-20230624092723773.png)

+ **当出现钩子函数导入的时候，先执行导入的mix3钩子函数，后执行定义的**

  ![image-20230624093252195](Vue知识点.assets/image-20230624093252195.png)

  ![image-20230624093230774](Vue知识点.assets/image-20230624093230774.png)



+ **全局混入**

  ![image-20230624093420048](Vue知识点.assets/image-20230624093420048.png)



# plugins配置（插件）

![image-20230624093520617](Vue知识点.assets/image-20230624093520617.png)



+ **定义插件**

![image-20230624102320037](Vue知识点.assets/image-20230624102320037.png)

+ **导入插件**

![image-20230624102253431](Vue知识点.assets/image-20230624102253431.png)



 

# 局部样式 scoped

![image-20230624120731460](Vue知识点.assets/image-20230624120731460.png)

![image-20230624121337199](Vue知识点.assets/image-20230624121337199.png)





# 案例：

## 兄弟组件传递数据

+ 借用父组件过度一下，数据放到父组件上 

## 子组件想改父组件的值

+ 父组件在data里定义的值，通过子组件props接收后，不可以直接改，

+ 方法：通过把父组件的改data的methods方法传递给子组件，然后子组件改值

  ![image-20230702082319249](Vue知识点.assets/image-20230702082319249.png)

  ![image-20230702082137022](Vue知识点.assets/image-20230702082137022.png)



## 孙子组件想勾选/取消 勾选框

+ 方法

  ![image-20230702084112033](Vue知识点.assets/image-20230702084112033.png)

### 爷爷：

![image-20230702084222350](Vue知识点.assets/image-20230702084222350.png)



### 儿子：

![image-20230702084312963](Vue知识点.assets/image-20230702084312963.png)

### 孙子：

![image-20230702084355205](Vue知识点.assets/image-20230702084355205.png)







## 组件自定义事件

+ **this.$emit**
+ **子组件向父组件传递参数**                 以前通过app组件定义一个**函数**传到子组件，使用props，然后子组件调用这个函数(传入子组件的值，调用了父组件的函数)

![image-20230703075233125](Vue知识点.assets/image-20230703075233125.png)

![image-20230703075149524](Vue知识点.assets/image-20230703075149524.png)

![image-20230703075102393](Vue知识点.assets/image-20230703075102393.png)



+ 通过代码给子组件绑定事件

  ![image-20230709211942452](Vue知识点.assets/image-20230709211942452.png)

+ 解绑

  ![image-20230709212318937](Vue知识点.assets/image-20230709212318937.png)

+ 扩展  --this指向问题

  ![image-20230709213555954](Vue知识点.assets/image-20230709213555954.png)

## bug统计个数

+ buglist 还是通过父类传过来的

![image-20230709173030133](Vue知识点.assets/image-20230709173030133.png)

![image-20230709172816744](Vue知识点.assets/image-20230709172816744.png)

![image-20230709173227953](Vue知识点.assets/image-20230709173227953.png)



## 子选框全选，全选框也勾上

![image-20230709173823141](Vue知识点.assets/image-20230709173823141.png)

![image-20230709173841722](Vue知识点.assets/image-20230709173841722.png)



## 全选框功能

![image-20230709174847910](Vue知识点.assets/image-20230709174847910.png)

![image-20230709174704330](Vue知识点.assets/image-20230709174704330.png)

![image-20230709174932969](Vue知识点.assets/image-20230709174932969.png)



## 清除已解决功能

![image-20230709175317403](Vue知识点.assets/image-20230709175317403.png)

## 点击bug描述修改

## 

![image-20230709203107939](Vue知识点.assets/image-20230709203107939.png)

![image-20230709203503911](Vue知识点.assets/image-20230709203503911.png)







# 全局事件总线

![image-20230709220804742](Vue知识点.assets/image-20230709220804742.png)

+ 全局事件总线原理 -----------给Vue的显示原型链上绑定一个VC，这样其他组件都可以访问最高级的属性了

![image-20230709223935099](Vue知识点.assets/image-20230709223935099.png)

![image-20230709223803957](Vue知识点.assets/image-20230709223803957.png)

![](Vue知识点.assets/image-20230709224428629.png)





# 消息的订阅与发布机制

![image-20230709231855709](Vue知识点.assets/image-20230709231855709.png)

![image-20230709232011514](Vue知识点.assets/image-20230709232011514.png)

![image-20230709231543493](Vue知识点.assets/image-20230709231543493.png)









# Vue与AJAX

![image-20230710071058541](Vue知识点.assets/image-20230710071058541.png)

## 回顾ajax跨域

![image-20230710071419296](Vue知识点.assets/image-20230710071419296.png) ![image-20230710071747174](Vue知识点.assets/image-20230710071747174.png)

![image-20230710071955772](Vue知识点.assets/image-20230710071955772.png)

![image-20230710072446896](Vue知识点.assets/image-20230710072446896.png) 



## 跨域问题演示

![image-20230710073201783](Vue知识点.assets/image-20230710073201783.png)

![image-20230710073250602](Vue知识点.assets/image-20230710073250602.png)

![image-20230710073319733](Vue知识点.assets/image-20230710073319733.png)



## 解决跨域问题

![image-20230710073405732](Vue知识点.assets/image-20230710073405732.png)

![image-20230710074022134](Vue知识点.assets/image-20230710074022134.png)





### 高级开启代理

![image-20230710074817328](Vue知识点.assets/image-20230710074817328.png)

![image-20230710075140953](Vue知识点.assets/image-20230710075140953.png)



## 案例

![image-20230710214059797](Vue知识点.assets/image-20230710214059797.png)

![image-20230710214108705](Vue知识点.assets/image-20230710214108705.png)





# Vuex

![image-20230710230424181](Vue知识点.assets/image-20230710230424181.png) 

![image-20230710230434514](Vue知识点.assets/image-20230710230434514.png)

![image-20230710230743830](Vue知识点.assets/image-20230710230743830.png)

![image-20230710230921801](Vue知识点.assets/image-20230710230921801.png)

![image-20230710231008004](Vue知识点.assets/image-20230710231008004.png)





## Vuex环境搭建

![image-20230710231927254](Vue知识点.assets/image-20230710231927254.png)

+ 案例=点击增加数字

![image-20230711070327647](Vue知识点.assets/image-20230711070327647.png)

## store.js

![image-20230711071507098](Vue知识点.assets/image-20230711071507098.png)

![image-20230711071544332](Vue知识点.assets/image-20230711071544332.png)

![image-20230711071614133](Vue知识点.assets/image-20230711071614133.png)

## vuex工作原理

![image-20230711072533638](Vue知识点.assets/image-20230711072533638.png)

## 案例

+ 组件互传数据

![image-20230711080120330](Vue知识点.assets/image-20230711080120330.png)

![image-20230711080158162](Vue知识点.assets/image-20230711080158162.png)

![image-20230711080304955](Vue知识点.assets/image-20230711080304955.png)





## ES6扩展运算符

![image-20230711214548980](Vue知识点.assets/image-20230711214548980.png)



## 获取vuex mapState mapGetters

![image-20230711220206288](Vue知识点.assets/image-20230711220206288.png)

![image-20230711215939761](Vue知识点.assets/image-20230711215939761.png)

![image-20230711220059381](Vue知识点.assets/image-20230711220059381.png)

![image-20230711220931112](Vue知识点.assets/image-20230711220931112.png)





## mapActions  mapMutations

![image-20230711221944380](Vue知识点.assets/image-20230711221944380.png)

sore.js

![image-20230711222052171](Vue知识点.assets/image-20230711222052171.png)







## vuex的模块化开发

![image-20230711224206622](Vue知识点.assets/image-20230711224206622.png)

![image-20230711224236091](Vue知识点.assets/image-20230711224248493.png)

### a b c 抽成js 

![image-20230711224752166](Vue知识点.assets/image-20230711224752166.png)

![image-20230711224813767](Vue知识点.assets/image-20230711224813767.png)

+ 简写形式，加个模块参数

![image-20230711225635398](Vue知识点.assets/image-20230711225635398.png)









# 路由route

 ![image-20230711230610934](Vue知识点.assets/image-20230711230610934.png)

![image-20230711231414360](Vue知识点.assets/image-20230711231414360.png) 

![image-20230711231653000](Vue知识点.assets/image-20230711231653000.png)

![image-20230711231705322](Vue知识点.assets/image-20230711231705322.png)

![image-20230711233117574](Vue知识点.assets/image-20230711233117574.png)

![image-20230711233502144](Vue知识点.assets/image-20230711233502144.png)

![image-20230711233719859](Vue知识点.assets/image-20230711233719859.png)



## 子路由

 ![image-20230712071448134](Vue知识点.assets/image-20230712071448134.png)

![image-20230712071521136](Vue知识点.assets/image-20230712071521136.png)





## 路由组件位置-习惯存放位置pages

![image-20230712071722658](Vue知识点.assets/image-20230712071722658.png)

![image-20230712071733300](Vue知识点.assets/image-20230712071733300.png)



## query传参-路由组件 

+ 各个城市只有数据不同，格式一样，只需传递不同参数即可

![image-20230712072721817](Vue知识点.assets/image-20230712072721817.png)

![image-20230712073057099](Vue知识点.assets/image-20230712073057099.png)



+ 最终方案

![image-20230712073422323](Vue知识点.assets/image-20230712073422323.png)

![image-20230712073446129](Vue知识点.assets/image-20230712073446129.png)

![image-20230712073521723](Vue知识点.assets/image-20230712073521723.png)



## prarm传参

![image-20230712075114879](Vue知识点.assets/image-20230712075114879.png)

![image-20230712075203189](Vue知识点.assets/image-20230712075203189.png)

![image-20230712075235710](Vue知识点.assets/image-20230712075235710.png)

+ 如果使用对象传参   --path不可用

![image-20230712075443693](Vue知识点.assets/image-20230712075443693.png)



## prop接收参数

![image-20230712080717012](Vue知识点.assets/image-20230712080717012.png)

![image-20230712080854406](Vue知识点.assets/image-20230712080854406.png)

![image-20230712080930975](Vue知识点.assets/image-20230712080930975.png)





## 编程式路由导航

![image-20230712201214664](Vue知识点.assets/image-20230712201214664.png)

![image-20230712201241272](Vue知识点.assets/image-20230712201241272.png)

### 前进后退

![image-20230712201716762](Vue知识点.assets/image-20230712201716762.png)

![image-20230712201727728](Vue知识点.assets/image-20230712201727728.png)



## 切换还保持状态  -include

![image-20230712202222280](Vue知识点.assets/image-20230712202222280.png) 

![image-20230712202328830](Vue知识点.assets/image-20230712202328830.png)



## activated和deactivated钩子

![image-20230712202828396](Vue知识点.assets/image-20230712202828396.png)

![image-20230712202946699](Vue知识点.assets/image-20230712202946699.png)

![image-20230712203122319](Vue知识点.assets/image-20230712203122319.png)

![image-20230712203240511](Vue知识点.assets/image-20230712203240511.png)

![image-20230712203224694](Vue知识点.assets/image-20230712203224694.png)





# 路由守卫

## 全局守卫

![image-20230712203410143](Vue知识点.assets/image-20230712203410143.png)

+ 全局前置守卫  - beforeEach

![image-20230712205146713](Vue知识点.assets/image-20230712205146713.png)



+ 全局后置守卫  -  router.afterEach

  ![image-20230712205858458](Vue知识点.assets/image-20230712205858458.png) 





## 局部守卫

+ path守卫 --   路由守卫  route

![image-20230712210956592](Vue知识点.assets/image-20230712210956592.png)



+ component守卫  -路由组件守卫 component

  ![image-20230712214356504](Vue知识点.assets/image-20230712214356504.png)



# 前端项目上线

![image-20230712214529492](Vue知识点.assets/image-20230712214529492.png)

![image-20230712214637171](Vue知识点.assets/image-20230712214637171.png)











# Vue3

![image-20230712223634187](Vue知识点.assets/image-20230712223634187.png)

![image-20230712223721650](Vue知识点.assets/image-20230712223721650.png)

![image-20230712224255468](Vue知识点.assets/image-20230712224255468.png)



+ **main.js  -- vue3**

  ![image-20230712225201600](Vue知识点.assets/image-20230712225201600.png)

+ **vue2 -main.js**

  ![image-20230712225507452](Vue知识点.assets/image-20230712225507452.png)

## create-vue创建Vue3工程

![image-20230712225732078](Vue知识点.assets/image-20230712225732078.png)

![image-20230712230955622](Vue知识点.assets/image-20230712230955622.png)





## Vite创建项目和webpack创建的区别

![image-20230712231641165](Vue知识点.assets/image-20230712231641165.png)

![image-20230719224050886](Vue知识点.assets/image-20230719224050886.png)

![image-20230719224133806](Vue知识点.assets/image-20230719224133806.png)



## setup()

![image-20230719225627561](Vue知识点.assets/image-20230719225627561.png)

![image-20230719225436508](Vue知识点.assets/image-20230719225436508.png)

![image-20230719225830364](Vue知识点.assets/image-20230719225830364.png)

![image-20230719231558969](Vue知识点.assets/image-20230719231558969.png)

![image-20230719231543302](Vue知识点.assets/image-20230719231543302.png)



![image-20230719233258471](Vue知识点.assets/image-20230719233258471.png)





## 响应式

![image-20230720065933517](Vue知识点.assets/image-20230720065933517.png)

![image-20230720070306213](Vue知识点.assets/image-20230720070306213.png)

![image-20230720070322231](Vue知识点.assets/image-20230720070322231.png) 





## Vue3中的props

 ![image-20230720072059956](Vue知识点.assets/image-20230720072059956.png)

![image-20230720072202173](Vue知识点.assets/image-20230720072202173.png)





## Vue3的生命周期

+ 组合式API  vue3特性
+ Options API Vue3   data, watch...

![image-20230720072301852](Vue知识点.assets/image-20230720072301852.png)

![image-20230720072442164](Vue知识点.assets/image-20230720072442164.png)



## 组合式使用生命钩子函数

![image-20230720074059837](Vue知识点.assets/image-20230720074059837.png)





## Vue3自定义事件  子传父

子：

![image-20230720074630047](Vue知识点.assets/image-20230720074630047.png)

父：

![image-20230720074653467](Vue知识点.assets/image-20230720074653467.png)





## Vu3全局事件总线

![image-20230720074806457](Vue知识点.assets/image-20230720074806457.png)

![image-20230720080303083](Vue知识点.assets/image-20230720080303083.png)

![image-20230720080038132](Vue知识点.assets/image-20230720080038132.png)





## 计算属性

+ **vue2**

  ![image-20230720220554326](Vue知识点.assets/image-20230720220554326.png)

  

+ **Vue3**

![image-20230720220316695](Vue知识点.assets/image-20230720220316695.png)

![image-20230720220838260](Vue知识点.assets/image-20230720220838260.png)



## 监听属性 watch



+ **Vue2**

  ![image-20230720221943282](Vue知识点.assets/image-20230720221943282.png)

### ref包裹

+ **Vue3**

  ![image-20230720222308054](Vue知识点.assets/image-20230720222308054.png)



### reactive包裹

![image-20230720223357824](Vue知识点.assets/image-20230720223357824.png)![image-20230720223824559](Vue知识点.assets/image-20230720223824559.png)





## watchEffect

![image-20230720224800338](Vue知识点.assets/image-20230720224800338.png)





## 自定义钩子函数 - hook函数

![image-20230720225411083](Vue知识点.assets/image-20230720225411083.png)

![image-20230720225505376](Vue知识点.assets/image-20230720225505376.png)





## shallowReactive和shallowRef

![image-20230720225555849](Vue知识点.assets/image-20230720225555849.png)

![image-20230720230149706](Vue知识点.assets/image-20230720230149706.png)

![image-20230720230102827](Vue知识点.assets/image-20230720230102827.png)

+ **shallowReactive** 

  ![image-20230720230756172](Vue知识点.assets/image-20230720230756172.png)



## 组合式API和选项式API





## 深只读

![image-20230720233751447](Vue知识点.assets/image-20230720233751447.png)

## 浅只读

![image-20230720233830075](Vue知识点.assets/image-20230720233830075.png)





## 响应式数据的判断

![image-20230721070711076](Vue知识点.assets/image-20230721070711076.png)



## toRef 和 toRefs

![image-20230721071622352](Vue知识点.assets/image-20230721071622352.png)

![image-20230721072051655](Vue知识点.assets/image-20230721072051655.png)

![image-20230721072413094](Vue知识点.assets/image-20230721072413094.png)



## 转换为原始&标记为原始

![image-20230721072506522](Vue知识点.assets/image-20230721072506522.png)

![image-20230721072824101](Vue知识点.assets/image-20230721072824101.png)



## Fragment

![image-20230721073621391](Vue知识点.assets/image-20230721073621391.png)

![image-20230721073526338](Vue知识点.assets/image-20230721073526338.png)





## Teleport

![image-20230721073651117](Vue知识点.assets/image-20230721073651117.png)

![image-20230721075444410](Vue知识点.assets/image-20230721075444410.png)

![image-20230721075604103](Vue知识点.assets/image-20230721075604103.png)





## provide inject

![image-20230721080001032](Vue知识点.assets/image-20230721080001032.png)

![image-20230721080043850](Vue知识点.assets/image-20230721080043850.png)