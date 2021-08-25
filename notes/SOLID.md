`Design Principles` introduced by *Robert C.*

## `SRP`
- Single Responsibility Principle
- also mentioned as **SOC**(seperation of concern)
- this principle is the opposite of <font color='red'>multi pattern</font>(bad idea)
- prevent you from creating a **God Object**
- a class should have only a reason to change
	- that reason is related to its primary responsibility

### Examples
- class Jounal
	- do something like store and remove entries from items
- if we add other responsibilities: `persistence`
	- save 
	- load
- not good !!!
	- then if you want to check before save
	- you have to change in each  class that contains this method
- what is good ?
	- create a class **PersistenceManager** 

## `OCP`
- Open-Close principle
	- open for extension, close for modification
	- extend means **inherit** from base class(overide the method of base class)
- prevent the <font color='red'>complexity explosion</font> when `criteria` increase
- [[Enterprise Pattern]]
	- `specification` pattern will help us to avoid modification 

## LSP
-  [Liskov Substitution Principle](http://www.cnblogs.com/gaochundong/p/liskov_substitution_principle.html)
-  derived class should have the `same behavior`with base class
-  以基类实例作为参数的**函数**，应该能在没有预见派生类的情况下正确运行
-  在行为上，一个Square对象不是一个Rectangle对象
	-  square对象会同时改变长宽，这是一个额外的、破坏性的行为

## ISP
- Interface Segregation Principle
- don't put a bunch of interface in a single class
	- demand first, don't implement or expose interface don't need 
- `@abstractmethod` is a python decorator to help define interface

## DIP
- Dependence Inversion Principle
- High-level classes/ module should not dependent on low-level classes / modules directly, instead should depend on `abstraction` 
	- otherwise, function of high-level classes should change once the data structure of low-level classes change(lets say from list to dict)

