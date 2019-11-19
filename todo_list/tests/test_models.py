from django.test import TestCase
from todo_list.models import Task
from datetime import date

# Create your tests here.
class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(
            title = 'My task title',
            description = 'The task description',
            end_date = date(2010, 10, 25)
            )
        
    def test_title(self):
        task = Task.objects.get(id = 1)
        #field_label = task._meta.get_field('title').verbose_name
        field_label = task._meta.get_field('title')
        print(field_label)
        field_label = field_label.verbose_name
        self.assertEquals(field_label, 'title')