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



