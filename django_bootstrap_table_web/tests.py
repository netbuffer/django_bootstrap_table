# Create your tests here.

from django.test import TestCase


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        print("django test")
