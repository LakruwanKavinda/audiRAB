from django.test import TestCase
from audiobooks.models import Audiobook
from datetime import timedelta

class AudiobookModelTestCase(TestCase):

    def setUp(self):
        # Set up data for test
        self.audiobook = Audiobook.objects.create(
            title="Sample Audiobook",
            author="John Doe",
            narrator="Jane Smith",
            duration=timedelta(hours=1, minutes=30),
            audio_file="test_audio.mp3",
        )

    def test_audiobook_creation(self):
        # Test the audiobook is created successfully
        self.assertEqual(self.audiobook.title, "Sample Audiobook")
        self.assertEqual(self.audiobook.author, "John Doe")
        self.assertEqual(self.audiobook.narrator, "Jane Smith")
        self.assertEqual(self.audiobook.duration, timedelta(hours=1, minutes=30))
        self.assertEqual(self.audiobook.audio_file, "test_audio.mp3")



