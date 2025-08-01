from django.db import models


class Client(models.Model):
    """Получатель рассылки"""

    email = models.EmailField(unique=True, verbose_name="Email")
    name = models.CharField(max_length=100, verbose_name="Ф.И.О.")
    comment = models.TextField(
        max_length=500, verbose_name="Комментарий", blank=True, null=True
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Message(models.Model):
    """Сообщение"""

    topic = models.CharField(max_length=150, verbose_name="Тема письма")
    text = models.TextField(max_length=1500, verbose_name="Сообщение")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["topic"]

    def __str__(self):
        return self.topic


class Mailing(models.Model):
    """Рассылка"""

    CREATED = "created"
    STARTED = "started"
    COMPLETED = "completed"

    STATUS_CHOICES = [
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
        (COMPLETED, "Завершена"),
    ]
    start_send = models.DateTimeField(verbose_name="Время первой отправки")
    stop_send = models.DateTimeField(verbose_name="Время окончания отправки")
    status = models.CharField(
        max_length=10, verbose_name="Статус", default=CREATED, choices=STATUS_CHOICES
    )
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name="mailings",
        verbose_name="Сообщение",
    )
    clients = models.ManyToManyField(Client, verbose_name="Клиенты")

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["status"]

    def __str__(self):
        return f"{self.message.topic} ({self.status})"
