from django.db import models

from users.models import User


class Client(models.Model):
    """Получатель рассылки"""

    email = models.EmailField(unique=True, verbose_name="Email")
    name = models.CharField(max_length=100, verbose_name="Ф.И.О.")
    comment = models.TextField(
        max_length=500, verbose_name="Комментарий", blank=True, null=True
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Владелец", null=True
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["name"]
        permissions = [
            ("can_view_all_clients", "Может просматривать всех клиентов"),
        ]

    def __str__(self):
        return self.name


class Message(models.Model):
    """Сообщение"""

    topic = models.CharField(max_length=150, verbose_name="Тема письма")
    text = models.TextField(max_length=1500, verbose_name="Сообщение")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Владелец", null=True
    )

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["topic"]
        permissions = [
            ("can_view_all_messages", "Может просматривать все сообщения"),
        ]

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
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Владелец", null=True
    )

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["status"]
        permissions = [
            ("can_view_all_mailings", "Может просматривать все рассылки"),
            ("can_disable_mailings", "Может отключать рассылки"),
        ]

    def __str__(self):
        return f"{self.message.topic} ({self.status})"


class Attempt(models.Model):
    SUCCESS = "success"
    FAILURE = "failure"

    STATUS_CHOICES = [
        (SUCCESS, "Успешно"),
        (FAILURE, "Неуспешно"),
    ]
    attempt_time = models.DateTimeField(auto_now_add=True, verbose_name="Время попытки")
    status = models.CharField(
        max_length=10, verbose_name="Статус попытки", choices=STATUS_CHOICES
    )
    server_response = models.TextField(
        blank=True, null=True, verbose_name="Ответ почтового сервера"
    )
    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, verbose_name="Рассылка"
    )

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"

    def __str__(self):
        return f"Попытка {self.id} - {self.status}"
