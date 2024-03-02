import os
from pathlib import Path
from sys import path

from django import setup
from django.db.models import F, Value
from django.db.models.functions import Replace
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

# from pathlib import Path
# from sys import path

BASE_DIR = Path(__file__).resolve().parent.parent
path.append(os.path.join(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
setup()


def convert_files(folder):
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.endswith('.wav'):
                try:
                    input_path = os.path.join(root, filename)
                    output_path = os.path.splitext(input_path)[0] + '.mp3'

                    sound = AudioSegment.from_wav(input_path)
                    sound.export(output_path, format="mp3")

                    print(f"File {filename} converted to MP3 successfully!")
                except CouldntDecodeError:
                    print(f"File {filename} failed!")

    from apps.content.models import Audio
    Audio.objects.filter(audio__endswith='.wav').update(
        audio=Replace(F('audio'), Value('.wav'), Value('.mp3'))
    )


convert_files('./media')
