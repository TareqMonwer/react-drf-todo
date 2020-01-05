from django.test import TestCase

from .models import Todo


class TodoTest(TestCase):
    @classmethod
    def setUpTestData(self):
        Todo.objects.create(title='Test Todo', body='todo body')
    
    def test_todo_content(self):
        todo = Todo.objects.get(id=1)
        title = f'{todo.title}'
        body = f'{todo.body}'
        self.assertEquals(title, 'Test Todo')
        self.assertEquals(body, 'todo body')
