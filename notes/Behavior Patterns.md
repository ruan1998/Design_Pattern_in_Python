## Chain
### Chain of Responsibility
- we can process an object by chain
- a chain of components who call get a chance to process a command or a query, optionally having **default** processing implementation and an ability to terminate the processing chain
- by calling function of super() in python

### Command Query Separation
- Command
	-  Asking for an action or change
- Query
	- Asking for some information
- CQS
	- Having seperate means of sending commands and queries
- centralized construct
	- e.g. use [[Behavior Patterns# Observer| oberver pattern]] 
	- use python context
		- in \__enter\__ to add object
		- in \__exit\__ to remove object

## Command
- Encapsulate all details of an operation in a separate object
- define instruction for applying the command
- optionally define instructions fro undoing the command
- can create composite commands

## Interpreter
- lexing 
- parsing

## Iterator
- Specified how you can traverse an object
- use `yield` in python if return value and then resume from breakpoint is necessary 

## Mediator
- create the mediator and have each object in system refer to it
	- mediator engages in bidirectional communication with it connect components
	- mediator has method the components can call
- components have function the mediator can call
- event processing libraries make communication easier to implement

## Memento
- roll back state arbitrarily
- a token / handle class with no function of its own, just save piece of datas
- can be used to undo and redo operations

## Observer
- an intrusive approach
	- an observable must provide an event to subscribe to
- subsciption and unsubscription handle with `addition` and `remove` of items in a list
- property(`@property` in python) observer are easy to implement, however if it depends on other properties, that might be rather tricky
- can be used together with other pattern
	- [[Behavior Patterns#Mediator]]
	- [[Behavior Patterns#Command]]
	- [[Behavior Patterns#State]]

## State
- object behavior is determined by its state
- an object transition from one state to another

## Strategy
- define an algorithm at a high level(can be reused in low level)
- define the interface you expect each strategy to follow 
- provide for dynamic composition of strategies in the resulting object