class instance_or_class_method:
    """ Decorator to make make a method both an instance and a class method,
    depending on who calls it.

    Examples
    --------
    ```
    ```

    Rerefence
    ----------
    https://docs.python.org/3/howto/descriptor.html#class-methods
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, instance:object, cls:type=None):
        
        if cls is None:
            cls = type(instance)

        if instance is not None:
            caller = instance # call as a normal instance method
        else:
            caller = cls      # call as a classmethod

        if hasattr(instance, '__get__'):
            return self.func.__get__(caller)
        return MethodType(self.func, caller)
