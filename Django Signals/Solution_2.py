'''
Question 2:
Do django signals run in the same thread as the caller? Please support your answer with a
code snippet that conclusively proves your stance. The code does not need to be elegant and
production ready, we just need to understand your logic.
'''

'''
Answer 2:
Django signals typically run in the same thread as the caller. This means that when a signal is
emitted, the receiver functions are executed within the same thread as the code that triggered the
signal.

Here's a code snippet to demonstrate this:
'''

from django.db.models.signals import post_save
from django.dispatch import receiver
from threading import current_thread

from .models import model

@receiver(post_save, sender=model)
def handler(sender, instance, **kwargs):
    print(current_thread().name)

# Create a new MyModel instance
model.objects.create(name="Example")

'''
In this example:

1. A 'post_save' signal is registered for the 'model' model.
2. The 'handler' function is the receiver.
3. The 'handler' function prints the name of the current thread.

When the 'model' instance is created, the 'post_save' signal is emitted. The 'handler' function is
then executed, and the printed thread name will match the thread that created the 'model' instance.
This demonstrates that Django signals are typically executed in the same thread as the caller.
'''