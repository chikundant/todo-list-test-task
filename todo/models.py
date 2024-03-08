from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.CharField(blank=True, max_length=15)  # max_length=15 is enough for content field?
    created_at = models.DateTimeField(auto_now_add=True)
    # Minor but for the future testing/monitoring better to add not only created_at, but updated_at field as well
    # You can specify mixin for this purpose
    deadline = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = ["created_at", "is_done"]

    def __str__(self):
        return f"Content: {self.content}"
