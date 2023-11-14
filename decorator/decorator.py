# import logging

# def use_logging(func):
#     def wrapper(*args, **kwargs):
#         logging.warning("%s is running" % func.__name__)
#         return func(*args, **kwargs)
#     return wrapper

# def bar():
#     print('i am bar')

# bar = use_logging(bar)
# bar()