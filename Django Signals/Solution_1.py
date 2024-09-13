'''
Question 1: 
By default are django signals executed synchronously or asynchronously? Please support your
answer with a code snippet that conclusively proves your stance. The code does not need to be elegant
and production ready, we just need to understand your logic.
'''

'''
Answer 1:
By default, Django signals are executed synchronously. This means that when a signal is emitted,
the receiver functions are called immediately within the same execution context.

Here's a simple code snippet to demonstrate this:

'''

from django.db.models.signals import post_save
from django.dispatch import receiver
from time import sleep

from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal received")
    sleep(5)
MyModel.objects.create(name="Example")

'''
In this example:
1. A 'post_save' signal is registered for the 'MyModel' model.
2. The 'my_handler' function is the receiver.
3. The 'my_handler' function includes a sleep call to simulate a long-running task.

When the 'MyModel' instance is created, the 'post_save' signal is dispatched. The 'my_handler' function
is then executed immediately, and the program will wait for 5 seconds due to the sleep call. If signals
were executed asynchronously, the program would continue executing without waiting for the signal handler
to finish.

This demonstrates that Django signals are synchronous by default, meaning that the receiver
functions are executed sequentially within the same context.

'''