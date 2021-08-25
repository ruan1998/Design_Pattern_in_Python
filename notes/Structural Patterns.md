## Adapter
- create a adapter to apapt the API been given

## Bridge
- prevent a `Cartesian product` complexity explosion
- **decouple** an interface(hierarchy) from an implementation(hierarchy)

## Composite
- lets us treat different types of objects uniformly
- some composed and singular objects need similar / idential <font color='#0f0'>behaviors</font>
	- 相同的行为常常在基类中定义
- 其它收获：实现\__iter\__ 是为了进入for循环入口(所有使用for循环的对象都必须定义\__iter\__), 实现\__next\__ 是为了在for循环内部使用next, yield自动定义了\__next\__ 

## Decorator
- keeps the reference to the decorated object(s)
	- **augment** the object's feature
	- may or may not forward calls to the underlying object
	- rewrite the \__getattr\__, \__setattr\__, \__delattr\__ to give the object more flexibility

## Façade
- french word, where ç called s
- balance the complexity and usability
- provide nice, convinient API for users to use 

## Flyweight
- avoid **redundancy**
- space optimization technique
- store the object as a list and refer to it

## Proxy
- protection proxy
	- add various `access control`
- virtual proxy
	- masquerading the underlying objects
	- appears like the objects it suppose to represent, but behind the scene it can offer additional functionality and behave differently,
	- materialized the object until first call its method or something

## Proxy vs. Decorator
- proxy provides identical interface, decorator provides enhanced interface
- decorator aggregates what it is decorating as a constructor argument, while proxy dosen't have to

