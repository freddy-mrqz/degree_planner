from django.db import models


class Course(models.Model):
    id = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    subject = models.CharField(max_length=4, blank=True, null=True)
    class_section = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    credit_hours = models.IntegerField(max_length=1, blank=True, null=True)

    def __string__(self):
        return "{}".format(self.number)

    def create_course(cls, id, number, description, subject, class_section, title, credit_hours):
        return cls.objects.create(
            self.id=id,
            self.number=number,
            self.description=description,
            self.subject=subject,
            self.class_section=class_section,
            self.title=title,
            self.credit_hours=credit_hours
        )

    class Meta:
        app_label = "catalog"

class Combinations(models.Model):
    LOGICAL_OPERATORS = (
        ('OR', 'OR'),
        ('AND', 'AND')
    )
    id = models.IntegerField()
    logical_operator = models.CharField(choices=LOGICAL_OPERATORS)
