## COMP 3522 Assignment 3

#### Introduction

Assignment involves implementing decorators to customise optional behaviours.

In this assignment, we are creating decorators for pizzas.



#### Decorator Pattern

- Pizza Interface
- PlainPizza (implements Pizza Interface; aka concrete Pizza]
- BasePizzaDecorator (implements Pizza interface AND stores a Pizza object (one that implements the interface) as its attribute)
- Decorators that inherit from the BasePizzaDecorator (e.g. BaconPizzaDecorator, ChickenPizzaDecorator)



#### User Input

The user is prompted to select various menu options through its menu number.

These inputs are validated in several ways:

- Empty strings
- Spaces
- Strings
- Floats



#### Menu

The user can quit the program at any point.

The user is free to add cheese and toppings in any order.

The user cannot checkout their pizza unless it has at least one cheese topping.



#### Limitations

I didn't implement the bonus mark, so the program has low scalability.  Values are hard-coded instead of being generated programmatically. 