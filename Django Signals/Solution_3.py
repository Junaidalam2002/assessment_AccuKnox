'''
Question 3:

By default do django signals run in the same database transaction as the caller? Please support your
answer with a code snippet that conclusively proves your stance. The code does not need to be elegant
and production ready, we just need to understand your logic.
'''

'''
Solution 3:
By default, Django signals are executed in a separate database transaction from the caller.
This ensures that the signal handlers can perform actions without affecting the integrity of the
original transaction.

Here's a more refined code example to illustrate this:
'''

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

from .models import model, related_model

@receiver(post_save, sender=model)
def handler(sender, instance, **kwargs):
    with transaction.atomic():
        related_model.objects.create(my_model=instance)

# Create a new MyModel instance
with transaction.atomic():
    model.objects.create(name="Example")

'''
In this example:

1. A 'post_save' signal is registered for the 'model' model.
2. The 'handler' function is the receiver.
3. The 'handler' function creates a new 'related_model' instance within a transaction.
4. The 'model' instance is created within a separate transaction.

The key point here is that the 'handler' function, which is the signal receiver, is executed in a
separate transaction. This guarantees that any changes made within the signal handler will be
committed or rolled back independently of the original transaction.
'''
