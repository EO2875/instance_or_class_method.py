# instance_or_class_method.py

Decorator to make make a method both an instance and a class method, depending on who calls it. 

# Usage

```python
class Example:
    
    t = 'class'
    
    def __init__(self):
        self.t = 'instance'
    
    @instance_or_class_method
    def get_t(self):
        return self.t

e = Example()

Example.get_t() # 'class'
e.get_t()       # 'instance'
```

Rerefence
----------
https://docs.python.org/3/howto/descriptor.html#class-methods

```
```

Rerefence
----------
https://docs.python.org/3/howto/descriptor.html#class-methods
