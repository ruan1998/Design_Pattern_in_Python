## Builder
- seperate components to initialize a class
	- via staticmethod of class
	- or a single class as builder
- return **self** in method to allow `fluent` call 
- multi builders for initializing complicated object 
	- call sub builders in base builder class
		- it violates the [[SOLID#OCP]]
	- inheriate builders step by step
		- open for extension
	
## Factory
- a wholesale(not piecewise) creation of object
### Factory Method
- create object with static method
	- good name for `method` to understand
	- good name for `arguments` to understand
- Group these methods into Factory class
	- can either be a external class or inner class
### Abstract Factory
- use a hierarchies of factories contains **all** the other factories

## Prototype
- reiterate exist design
- a partially or fully initialized object that you copy and make use of
	- partially construct an object and store it by e.g. [[#Factory]]
	- `deepcopy` the prototype
	- customize the resulting instance
	- a factory provide convinient API for using prototype in code

## Singleton
- a component which is instantiated only once
- use `allocator`(overwrite the \__new\__ ) maybe good, but when class need init, then it's useless
- use `decorator`, `metaclass` to manipulate sub class
	- metaclass 属于元编程，可以通过父类操作子类，父类的\__call\__ 方法会在子类调用生成实例时, **代替**type(顶级父类)或其它上层父类的\__call\__ 方法被调用
		- \__call\__, \__new\__ 都是静态方法, 规范使用cls作为其参数, \__call\__ 依次调用\__new\__, \__init\__
		- cls代表当前准备实例化的类, 如传到父类\__new\__ 中的子类(子类调用了父类的new方法), 或者如果子类自己重写了\__new\__ , 则cls就是子类自己
		- 注意**最大递归**问题, 比如自己调用自己的\__new\__
	- class静态变量可以保持(**在定义class时就已经生成**), 而`装饰器`中的变量则只作为**局部变量**