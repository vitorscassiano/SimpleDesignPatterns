from functools import wraps
# def decorator(f):
#   @wraps(f)
#   def wrapper(*args, **kwargs):
#       print(args)
#       f()
#       print(kwargs)
#   return wrapper

def decorator(f):
  def wrapper(*args, **kwargs):
    print("Before")
    f(*args, **kwargs)
    print("After")
    return
  return decorator

@decorator
def hello(name: str):
  return f"Hello {name}!"

# Main
msg = hello("Vitor")
print(msg())