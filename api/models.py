from django.db import models


class Task(models.Model):
    """
    Represents a Task object with a name and description.

    This model stores information about Task objects, including their names,
    descriptions, creation times, and last update times. It is used to demonstrate
    basic Django model functionality within the Task-plugin.

    Attributes:
        name (CharField): The name of the Task object.
        description (TextField): A detailed description of the Task object.
        created_at (DateTimeField): The date and time when the object was created.
        updated_at (DateTimeField): The date and time when the object was last updated.
    """

    name = models.CharField(
        max_length=100,
        help_text="Enter the name of the Task object (max 100 characters)",
    )
    description = models.TextField(
        help_text="Provide a detailed description of the Task object"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the object was created (automatically set)",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the object was last updated (automatically updated)",
    )

    def __str__(self):
        return self.name
